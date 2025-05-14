#!/bin/python3
# -*- coding: utf-8 -*-
# Actividad 1.2.2 - Cliente MQTT
# Autor: Alejandro Castro
# Fecha: 2023-10-02
# Descripción: Este script crea un cliente MQTT que se conecta a un broker y publica mensajes en el topic "redes2".
# Importar librerías necesarias

import paho.mqtt.client as mqtt
import time

# Función cuando se conecta al broker
def on_connect(client, userdata, flags, rc):
    print("Conectado con código: " + str(rc))

# Crear cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect

# Conectar con el broker MQTT (lo harás a Docker más adelante)
client.connect("localhost", 1883, 60)

# Publicar mensajes al topic "redes2"
while True:
    client.publish("redes2", "Hola desde el cliente Paho")
    print("Mensaje enviado")
    time.sleep(5)
