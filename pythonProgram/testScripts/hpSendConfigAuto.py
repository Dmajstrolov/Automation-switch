import getpass
import telnetlib
import time

HOST = "192.168.1.200"


tn = telnetlib.Telnet(HOST,23)

tn.write(b"y")
time.sleep(2)
tn.write(b"operator\n")
time.sleep(2)
tn.write(b"cisco\n")

time.sleep(2)

tn.write(b"enable\n")
tn.write(b"copy running-config tftp 192.168.1.20 hp_switch_config\n")
tn.write(b"exit\n")
tn.write(b"exit\n")
tn.write(b"y")

print(tn.read_all().decode('ascii'))
