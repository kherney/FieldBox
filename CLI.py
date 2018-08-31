from telnetlib import Telnet
CN=Telnet('80.0.0.3',5024)
print CN.interact()
