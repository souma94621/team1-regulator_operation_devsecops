# handlers/firmware_handler.py
import logging
from datetime import datetime
from ..models import FirmwareRequest, FirmwareResult
from ..certificate_manager import CertificateManager
from ..security_test_runner import SecurityTestRunner
from ..coverage_controller import CoverageController
from ..broker_client import BrokerClient
from ..config import Config

logger = logging.getLogger(__name__)

class FirmwareHandler:
    def __init__(self, cert_manager: CertificateManager, test_runner: SecurityTestRunner,
                 coverage_controller: CoverageController, broker: BrokerClient):
        self.cert_manager = cert_manager
        self.test_runner = test_runner
        self.coverage_controller = coverage_controller
        self.broker = broker
    
    async def handle(self, message: dict):
        try:
            req = FirmwareRequest(**message)
            logger.info(f"Processing firmware request {req.request_id}")
            
            # 1. Запуск тестов безопасности
            test_result = await self.test_runner.run_tests(req.firmware)
            if not test_result["passed"]:
                result = FirmwareResult(
                    request_id=req.request_id,
                    timestamp=datetime.utcnow(),
                    status="REJECTED",
                    certificate=None
                )
                await self.broker.publish(Config.TOPIC_FIRMWARE_RESULT, result.dict())
                logger.warning(f"Firmware {req.request_id} rejected: security tests failed")
                return
            
            # 2. Проверка покрытия (если требуется – по усмотрению, можно делать только для доверенных)
            # В учебном проекте пропускаем
            # if self.is_trusted_firmware(req):
            #     coverage = await self.coverage_controller.get_coverage(...)
            #     if coverage < Config.COVERAGE_THRESHOLD_INTEGRITY:
            #         reject...
            
            # 3. Создание сертификата
            cert = self.cert_manager.create_certificate(
                subject_type="firmware",
                subject_id=req.firmware.get("commit_hash", req.request_id),
                security_goals=["FW-SEC-01", "FW-SEC-02", "FW-SEC-05"]  # из запроса
            )
            
            # 4. Формирование результата
            result = FirmwareResult(
                request_id=req.request_id,
                timestamp=datetime.utcnow(),
                status="CERTIFIED",
                certificate=cert.dict()
            )
            await self.broker.publish(Config.TOPIC_FIRMWARE_RESULT, result.dict())
            logger.info(f"Firmware {req.request_id} certified as {cert.certificate_id}")
        except Exception as e:
            logger.error(f"Error processing firmware request: {e}", exc_info=True)