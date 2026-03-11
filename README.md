# team1 (ПК)
Наша команда отвечает за:
* регулятор
* эксплуатанты
* DevSecOps

## Взаимодействие между разработчиком БАС регулятором и эксплуатантом
<img width="681" height="341" alt="эксплуатант" src="https://github.com/user-attachments/assets/2b9ecffb-a62a-44f5-b9f9-dbe7af674e98" />

### Топики
* firmware.certification.request
Поля:
```json
{
  "request_id": "req-fw-001",
  "timestamp": "2026-03-10T10:00:00Z",

  "developer_id": "DroneTech",

  "firmware": {
    "repository_url": "https://github.com/AMCP-Drones/drones",
    "commit_hash": "d71763e430b45ee01012b005751861627d7b4147",
    "version": "3.2.1"
  },

  "drone_type": "DeliveryDrone-X2"
}
```
