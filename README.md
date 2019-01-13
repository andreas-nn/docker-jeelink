<H2>Receive Information from technoline thermometers</H2>

Put an Jeelink-Stick (LaCrosse) to an USB-Port.<BR>
This stick receives the information via 868 MHz from the thermometers.<BR>
The script jeelink.py decodes it and send it to your mosquitto-server.<BR>
jeelink/sensorxy => {"temperature":99.99,"humidity":99,"battery":100|0}
<BR>
<BR>
<H4>Please defin your parameters in config.json</H4>
(JSON-style)

tty-port  => ttyUSB0 (normally used)<BR>
mqtt-server => your_server_ip<BR>
mqtt-port => 1883 (normally used)<BR>
client-id => a name (what you want)<BR>
username => username for login in mqqt-server | or ""
password => password for login in mqqt-server | or ""
