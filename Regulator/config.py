# config.py
import os

class Config:
    # Брокер сообщений
    BROKER_URL = os.getenv("BROKER_URL", "amqp://guest:guest@localhost/")
    EXCHANGE_NAME = "amq.topic"
    
    # Топики входящие
    TOPIC_FIRMWARE_REQUEST = "v1.firmware.certification.request"
    TOPIC_DRONE_REQUEST = "v1.drone.registration.request"
    TOPIC_OPERATOR_REQUEST = "v1.operator.op1.certificate_request"
    TOPIC_INSURER_REQUEST = "v1.Insurer.reg1.insurer-service.requests"
    TOPIC_CERT_VERIFY_REQUEST = "v1.regulator.certificate.verify.request"   # опционально
    TOPIC_CERT_REVOKE_REQUEST = "v1.regulator.certificate.revoke.request"   # опционально
    
    # Топики исходящие
    TOPIC_FIRMWARE_RESULT = "v1.firmware.certificate.result"
    TOPIC_DRONE_RESULT = "v1.drone.registration.result"
    TOPIC_OPERATOR_RESULT = "v1.operator.op1.certificate_result"
    TOPIC_INSURER_RESPONSE = "v1.Insurer.reg1.insurer-service.responses"
    TOPIC_CERT_VERIFY_RESPONSE = "v1.regulator.certificate.verify.response"
    TOPIC_CERT_REVOKE_RESPONSE = "v1.regulator.certificate.revoke.response"
    
    # Хранилище сертификатов (файл или БД)
    CERT_STORAGE_PATH = "data/certificates.json"
    CRL_STORAGE_PATH = "data/crl.json"
    
    # Ключи
    PRIVATE_KEY_PATH = "keys/regulator_private.pem"
    PUBLIC_KEY_PATH = "keys/regulator_public.pem"
    
    # Параметры покрытия
    COVERAGE_THRESHOLD_TRUSTED = 60      # БТ5
    COVERAGE_THRESHOLD_INTEGRITY = 70    # БТ6
    
    # Для учебного проекта – всегда успешные тесты
    MOCK_SECURITY_TESTS = True
    MOCK_COVERAGE = True