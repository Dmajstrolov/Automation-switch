import getpass
import sys
import telnetlib
import time

HOST = "192.168.1.25"


user = input("Enter your username: ")
password = getpass.getpass()


tn = telnetlib.Telnet(HOST,23)
tn.set_debuglevel(8)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
	tn.read_until(b"Password: ")
	tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
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