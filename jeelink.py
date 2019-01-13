#!/usr/bin/env python
import time
import serial
import sys
import json,requests
import paho.mqtt.client as mqtt

#Einlesen der Konfiguration
with open('/app/config.json') as json_data_file:
  data = json.load(json_data_file)

#Oeffnen des seriellen Ports zum Jeelink
ser_jee = serial.Serial(
    port=data["tty-port"],
    baudrate=57600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
#++++++++++++++++++++++++++++++++++++++++
#auf Jeelink warten und Konfiguration setzen
time.sleep(5)
init = "                                                       "
ser_jee.write(bytes(init, 'utf-8'))
init = "0a 0c 0d 0r 868295f v\n"
ser_jee.write(bytes(init, 'utf-8'))
#Setup
# 0a - LED aus
# 0c - Sendebaudrate 17241
# 0r - Empfangsbaudrate 17241
# 868300f - Frequenz 868.300 MHz
# v - Ausgabe der Konfiguration
#/JEE
#++++++++++++++++++++++++++++++++++++++++
#Kontakt zum mqtt-Server aufbauen
mqtt_c = mqtt.Client(client_id=data["client-id"])
# username_pw_set(username, password=None)
mqtt_c.username_pw_set(data["username"],data["password"])
mqtt_c.reconnect_delay_set(min_delay=1, max_delay=120)
mqtt_c.connect(data["mqtt-server"], port=data["mqtt-port"], keepalive=60)

#main_loop
zeile_jee=""
while True:
    # auf Zeichen warten
    time.sleep(0.2)

    zeichen_jee=ser_jee.in_waiting
    #Zeichen uebernehmen
    if zeichen_jee>0:
      zeichen=ser_jee.read(zeichen_jee)
      zeile_jee=zeile_jee+str(zeichen,'ascii')

    # bei newline Verarbeitung beginnen
    position=zeile_jee.find("\n")
    if position >= 0:
      zeile=zeile_jee[:position-1]
      zeile_jee=zeile_jee[position+1:]

      # Inhalte der Temperaturgeber entschluesseln
      pl_ziel="-1"
      pl_items=zeile.split(" ")
      pl_anz=len(pl_items)
      #wenn korrekter Inhalt gelesen wurde
      if (pl_anz > 6) and (pl_items[0]=="OK"):

        pl_ziel='{'

        # Temperatur dekodieren
        temp ="{:.2f}".format((float(pl_items[4])*256 + float(pl_items[5]) - 1000) / 10 )
        pl_ziel=pl_ziel + '"temperature":' + temp

        # Feuchtigkeit dekodieren, falls im Datensatz vorhanden
        humid =divmod(float(pl_items[6]),128)[1]
        if (humid != 106):
          pl_ziel=pl_ziel + ','
          pl_ziel=pl_ziel + '"humidity":' + "{:.0f}".format(humid)

        # Batterie-OK dekodieren
        batt =divmod(float(pl_items[6]),128)[0]
        if (batt == 0):
          pl_ziel=pl_ziel + ',"battery":100'
        else:
          pl_ziel=pl_ziel + ',"battery":0'

        pl_ziel=pl_ziel + '}'

        # JSON-Daten sind fertig kodiert in pl_ziel
        if (pl_ziel!="-1"):
          # Daten an mqtt-Server senden
          topic = "jeelink/sensor"+ pl_items[2]
          mqtt_c.publish(topic, payload=pl_ziel, qos=0, retain=False)

#Ende
mqtt_c.disconnect()
