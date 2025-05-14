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
