<H2>Receive Information from technoline thermometers</H2>

Put an Jeelink-Stick (LaCrosse) on a free USB-Port.<BR>
This stick receives the information via 868 MHz from the thermometers.<BR>
The script jeelink.py decodes it and sends it to your mosquitto-server.<BR>
<BR>
i.e. jeelink/sensor[xy] => {"temperature":99.99,"humidity":99,"battery":100|0}
<BR><BR>
Just now the images are available for arm64 and armhf<BR>
I am using pine64 with archlinuxarm. But a build at an other platform is possible.<BR>
Feel free for changing jeelink.py to your conditions.<BR>
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
<PRE>docker run \
  --device=/dev/ttyUSB0 \
  -v &lt;your-path&gt;/app:/app \
  --name jeelink \
  --network &lt;your network&gt; \
  --restart unless-stopped \
  -d \
  andreasnn/jeelink:arm64 \
  jeelink.py
</PRE>
Both files "jeelink.py" and "config.json" must be in subdir "./app".
