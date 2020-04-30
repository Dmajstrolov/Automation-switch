import getpass
import telnetlib
import time

HOST = "192.168.1.200"
""" 
user = input("Enter your username: ")
password = getpass.getpass() """

tn = telnetlib.Telnet(HOST,23)
tn.set_debuglevel(8)

tn.write(b"y")
time.sleep(2)
tn.write(b"operator\n")
time.sleep(2)
tn.write(b"cisco\n")
time.sleep(2)

tn.write(b"enable\n")
tn.write(b"copy tftp startup-config 192.168.1.20 hp_switch_config\n")
time.sleep(2)
tn.write(b"y")
time.sleep(2)
tn.write(b"y\n")
tn.close()

print(tn.read_all().decode('ascii'))