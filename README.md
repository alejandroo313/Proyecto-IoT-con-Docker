# 🌐 Ecosistema IoT con Docker: MQTT + Node-RED + InfluxDB + Grafana  
_Actividad para la asignatura Redes de Comunicaciones II_

Este proyecto construye un entorno IoT desacoplado y funcional utilizando contenedores Docker. Permite la publicación y visualización de datos en tiempo real a través de múltiples tecnologías clave del Internet de las Cosas.


## 🧩 Componentes

- **Mosquitto** – Broker MQTT ligero para comunicación entre dispositivos.
- **Node-RED** – Plataforma visual de flujos para procesamiento y redireccionamiento de datos.
- **InfluxDB** – Base de datos optimizada para almacenar series temporales.
- **Grafana** – Herramienta potente de visualización y análisis de métricas.

## 📌 Objetivos del proyecto

- Conectar un cliente MQTT (como Paho) con Mosquitto.
- Procesar y almacenar los mensajes recibidos en InfluxDB usando Node-RED.
- Visualizar las métricas recogidas mediante dashboards en Grafana.

## 🧰 Requisitos

- Docker
- Docker Compose
- Cliente MQTT (ej. [Paho MQTT en Python](https://www.eclipse.org/paho/index.php?page=clients/python/index.php))

## 🚀 Instrucciones de uso

1. Clona este repositorio.

```bash
git clone https://github.com/alejandroo313/Proyecto-IoT-con-Docker
cd Proyecto-IoT-con-Docker
```
2. Ejecuta:

```bash
docker-compose up -d
```
3. Crea un entorno virtual python e instala los paquetes de ```requirements.txt```.
4. Ejecuta el cliente MQTT que publicará mensajes de prueba:
```bash
python cliente-mqtt.py
```
5. Abre Node-red en ```http://localhost:1880``` y pega el flujo JSON incluido ```nodered-flow.json```.
6. Abre grafana en ```http://localhost:3000``` (user/pass: admin/admin).
7. Crea un dashboard con el origen de datos InfluxDB.

## Estructura del proyecto
.  
├── docker-compose.yml         # Orquestación de servicios  
├── nodered-flow.json                 # Flujo de Node-RED exportado  
├── README.md  
├── cliente-mqtt.py            # Cliente que generara mensajes para probar el entorno  
├── requirements.txt           # Requisitos para el entorno virtual python  
└── (opcional) .env

## Ejemplo de flujo
[mqtt in] → [function] → [influxdb out]  
                    ↓  
                 [debug]  

## Ejemplo de posible dashboard Grafana
![Dashboard](image.png)

## Autor
Alejandro Castro  
Github: [@alejandroo313  ](https://github.com/alejandroo313)  
Email: alejandrocastro3333@gmail.com
