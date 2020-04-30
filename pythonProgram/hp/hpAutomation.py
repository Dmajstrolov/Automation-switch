import getpass
import telnetlib

HOST = "192.168.1.200"

user = input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST,23)

tn.write(b"y")

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
	tn.read_until(b"Password: ")
	tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"copy running-config tftp 192.168.1.20 hp_switch_config\n")
tn.write(b"exit\n")
tn.write(b"exit\n")
tn.write(b"y")

print(tn.read_all().decode('ascii'))
