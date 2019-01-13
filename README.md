<H2>Receive Information from technoline thermometers</H2>

Put an Jeelink-Stick (LaCrosse) to an USB-Port.<BR>
This stick receives the information via 868 MHz from the thermometers.<BR>
The script jeelink.py decodes it and send it to your mosquitto-server.<BR>
<BR>
jeelink/sensorxy => {"temperature":99.99,"humidity":99,"battery":100|0}
<BR>
<BR>
<H3>Please define your parameters in config.json</H3>
(JSON-style)<BR>
<BR>
tty-port  => ttyUSB0 (normally used)<BR>
mqtt-server => your_server_ip<BR>
mqtt-port => 1883 (normally used)<BR>
client-id => a name (your choice)<BR>
username => username for login in mqqt-server | or ""<BR>
password => password for login in mqqt-server | or ""<BR>
<BR>
<H3>Docker-command</H3>
<PRE>docker run --device=/dev/ttyUSB0 \
  -v \<your-path\>/app:/app \
  --name jeelink \
  --network \<your network\> \
  --restart unless-stopped \
  -d \
  andreasnn/jeelink:arm64 \
  jeelink.py
</PRE>
