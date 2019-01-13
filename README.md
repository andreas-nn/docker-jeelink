<H2>Receive Information from technoline thermometers</H2>

Put an Jeelink-Stick (LaCrosse) to an USB-Port.
This stick receives the information via 868 MHz from the thermometers.
The script jeelink.py decodes it and send it to your mosquitto-server.
jeelink/sensorxy => {"temperature":99.99,"humidity":99,"battery":100|0}


<H4>Please defin your parameters in config.json</H4>
(JSON-style)

tty-port  => ttyUSB0 (normally used)
mqtt-server => your_server_ip
mqtt-port => 1883 (normally used)
client-id => a name (what you want)
username => username for login in mqqt-server | or ""
password => password for login in mqqt-server | or ""
