import getpass
import telnetlib
import time

HOST = "192.168.1.25"

tn = telnetlib.Telnet(HOST)

tn.write(b"Elias\n")
time.sleep(2)
tn.write(b"cisco\n")
time.sleep(2)
tn.write(b"enable\n")
time.sleep(2)
tn.write(b"class\n")
tn.write(b"copy running-config tftp\n")
tn.write(b"192.168.1.20\n")
tn.write(b"sw1_running_config\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
