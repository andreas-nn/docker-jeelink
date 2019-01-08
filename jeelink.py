#!/usr/bin/env python
import time
import serial
import sys
import json,requests

ser_jee = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=57600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
#++++++++++++++++++++++++++++++++++++++++
#JEE
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

def IpsRpc(methodIps, paramIps):
    url = "http://192.168.12.25:82/api/"
    headers = {'content-type': 'application/json'}
    payload = {
        "method": methodIps,
        "params": paramIps,
        "jsonrpc": "2.0",
        "id": 0,
    }
#    print json.dumps(payload)
    try:
        response = requests.post(url, timeout=0.5, data=json.dumps(payload), headers=headers)
    except requests.exceptions.RequestException as e:
      a=1
#	print ("Fehler")
#    print(response)


#++++++++++++++++++++++++++++++++++++++++
zeile_jee=""
while True:
    time.sleep(0.2)

    zeichen_jee=ser_jee.in_waiting
    if zeichen_jee>0:
      zeichen=ser_jee.read(zeichen_jee)
      zeile_jee=zeile_jee+str(zeichen,'ascii')

    position=zeile_jee.find("\n")
    if position >= 0:
        zeile=zeile_jee[:position-1]
        print("+"+zeile+"+")
        zeile_jee=zeile_jee[position+1:]
# JSON-RPS zu IPS definieren
        IpsRpc("SetValue", [43706, "Jeelink:"+zeile])

#Ende