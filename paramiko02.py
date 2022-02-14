from http import client
import time
import paramiko

username = "admin"
password = "cisco"
private = paramiko.RSAKey.from_private_key_file("/home/devasc/.ssh/id_rsa")

devices_ip = ["172.31.111.2", "172.31.111.3", "172.31.111.4", "172.31.111.5", "172.31.111.6"]

for ip in devices_ip:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, username="admin", pkey=private, allow_agent=False, look_for_keys=True)
    print("Connecting to {} ...".format(ip))
    with client.invoke_shell() as ssh:
        print("Connecting to {} ...".format(ip))

        ssh.send("terminal length 0\n")
        time.sleep(1)
        result = ssh.recv(1000).decode('ascii')
        print(result)

        ssh.send("sh ip int br\n")
        time.sleep(1)
        result = ssh.recv(1000).decode('ascii')
        print(result)