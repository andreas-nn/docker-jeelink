<H2>Receive Information from technoline thermometers</H2>

Put an Jeelink-Stick (LaCrosse) to an USB-Port.
This stick receives the information via 868 MHz from the thermometers.

The script jeelink.py decodes it and send it to your mosquitto-server.

jeelink/sensorxy => {"temperature":99.99,"humidity":99,"battery":100|0}
