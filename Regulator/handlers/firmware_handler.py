import asyncio
import logging
from unittest.mock import AsyncMock, MagicMock

# Импортируем твои классы
from certificate_manager import CertificateManager
from handlers.firmware_handler import FirmwareHandler

# Настройка логов
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

async def run_test():
    print("=== ЗАПУСК ТЕСТА FIRMWARE_HANDLER (ЭМУЛЯЦИЯ) ===\n")

    # 1. Готовим зависимости
    # Убедись, что файл keys/regulator_private.pem создан!
    try:
        cert_manager = CertificateManager(
            storage_path="certificates.json", 
            private_key_path="keys/regulator_private.pem"
        )
    except FileNotFoundError:
        print("[-] ОШИБКА: Создай файл keys/regulator_private.pem сначала!")
        return

    # Создаем "заглушки" для остальных компонентов, чтобы не запускать всю систему
    test_runner = MagicMock()
    test_runner.run_tests = AsyncMock(return_value={"passed": True})
    
    coverage_controller = MagicMock()
    broker = MagicMock()
    broker.publish = AsyncMock()

    # 2. Создаем сам Обработчик
    handler = FirmwareHandler(cert_manager, test_runner, coverage_controller, broker)

    # 3. Тестовые данные (имитируем сообщение от дрона)
    test_payload = {
        "request_id": "REQ-AGRO-2026",
        "firmware": {
            "commit_hash": "abc12345",
            "repository_url": "http://github.com"
        }
    }

    print(f"[*] Отправка тестового запроса: {test_payload['request_id']}")

    # 4. ЗАПУСК
    try:
        await handler.handle(test_payload)
        print("\n[OK] Обработка завершена!")
        print("[*] Проверь файл 'certificates.json' — там должен появиться новый сертификат.")
    except Exception as e:
        print(f"\n[!] ОШИБКА в коде: {e}")

if __name__ == "__main__":
    asyncio.run(run_test())
