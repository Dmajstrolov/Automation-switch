import getpass
import sys
import telnetlib
import time

HOST = "192.168.1.25"

tn = telnetlib.Telnet(HOST,23)
tn.set_debuglevel(8)


tn.write(b"Elias\n")
time.sleep(2)
tn.write(b"cisco\n")
time.sleep(2)
tn.write(b"enable\n")
time.sleep(2)
tn.write(b"class\n")

tn.write(b"copy tftp startup-config\n")
tn.write(b"192.168.1.20\n")
tn.write(b"cisco_restore\n")
tn.write(b"\n")

time.sleep(2)
tn.write(b"reload\n")
tn.write(b"\n")



print(tn.read_all().decode('ascii'))

tn.close()