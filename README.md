# Actividad Redes de Comunicaciones II
## Entorno IoT con Docker: MQTT + Node-RED + InfluxDB + Grafana

### Componentes
- Mosquitto (Broker MQTT)
- Node-RED (Procesamiento de datos)
- InfluxDB (Base de datos de series temporales)
- Grafana (Visualización de métricas)

### Como usar

1. Clona este repositorio.
2. Ejecuta:

```bash
docker-compose up -d
```

3. Abre Node-red en ```http://localhost:1880``` y pega el flujo JSON incluido.
4. Abre grafana en ```http://localhost:3000``` (user/pass: admin/admin).
5. Crea un dashboard con el origen de datos InfluxDB.