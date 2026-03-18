## Архитектура эксплуатанта
<img width="2040" height="1006" alt="Диаграмма без названия drawio" src="https://github.com/user-attachments/assets/bc22233c-1973-4e99-952c-9b1c5880affb" />

### Топики
* v1.orvd.component - в процессе

Предлагаемый формат сообщения регистрации миссии:


```
{
  "drone_id": "DRN-77-XY",
  "mission_id": "MSN-1024",
  "mission_route": [
    {"lat": 55.7558, "lon": 37.6173, "alt": 100},
    {"lat": 55.7580, "lon": 37.6200, "alt": 120},
    {"lat": 55.7600, "lon": 37.6300, "alt": 100}
  ],
  "timestamp": "2026-03-18T10:50:00Z"
}
```
* v1.drone_port.orchestretor - в процессе
* v1.gcs.1.orchestrator находится в https://github.com/Kaitrye/DronePortGCS?tab=readme-ov-file#внешний-контракт
* v1.Insurer.op1.insurer-service.requests и v1.Insurer.op1.insurer-service.responses находится в https://github.com/DashDashh/Insurer
* v1.operator.op1.certificate
* v1.aggregator_insurer.local.operator.responses и v1.aggregator_insurer.local.operator.requests находятся на https://github.com/DashDashh/Agregator
