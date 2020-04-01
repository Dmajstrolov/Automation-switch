import getpass
import telnetlib

HOST = "192.168.1.25"
user = input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
	tn.read_until(b"Password: ")
	tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"class\n")
tn.write(b"copy running-config tftp\n")
tn.write(b"192.168.1.20\n")
tn.write(b"sw1_running_config\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
