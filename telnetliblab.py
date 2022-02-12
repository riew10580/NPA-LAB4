
import getpass
import telnetlib
import time

def telnetlib_lab(num):
    host = '172.31.111.' + str(num+3)
    user = input("Enter username: ")
    password = getpass.getpass()

    tn = telnetlib.Telnet(host, 23, 5)

    tn.read_until(b"Username:")
    tn.write(user.encode('ascii') + b"\n")
    time.sleep(1)

    tn.read_until(b"Password:")
    tn.write(password.encode('ascii') + b"\n")
    time.sleep(1)

    tn.write(b"conf t\n")
    time.sleep(2)
    tn.write(b"int g0/1\n")
    time.sleep(2)
    tn.write(b"ip add 172.31.111.17 255.255.255.240\n")
    time.sleep(2)
    tn.write(b"end\n")
    time.sleep(2)
    tn.write(b"sh ip int bri\n")
    time.sleep(2)
    tn.write(b"exit\n")
    time.sleep(1)

    output = tn.read_very_eager()
    print(output.decode('ascii'))

    tn.close()

telnetlib_lab(1)
    