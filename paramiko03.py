from http import client
import time
import paramiko

def run_intsuction(intsuction_list, ssh):
    for intsuction in intsuction_list:
        ssh.send(intsuction+"\n")
        time.sleep(1)

def ssh_connect():
    username = "admin"
    password = "cisco"
    private = paramiko.RSAKey.from_private_key_file("/home/devasc/.ssh/id_rsa")

    devices_ip = ["172.31.111.4", "172.31.111.5", "172.31.111.6"]
    instruction = {
        "172.31.111.4":[
        "config t",
        "router ospf 1 vrf control-Data",
        "network 172.31.111.16 0.0.0.15 area 0",
        "network 172.31.111.32 0.0.0.15 area 0",
        "network 1.1.1.1 0.0.0.0 area 0",
        "exit",
        "ip access-list extended 101",
        "permit ospf 172.31.111.0 0.0.0.63 any",
        "permit tcp 172.31.111.0 0.0.0.7 any eq 22",
        "permit tcp 172.31.111.0 0.0.0.7 any eq 23",
        "permit tcp 10.253.190.0 0.0.0.255 any eq 22",
        "permit tcp 10.253.190.0 0.0.0.255 any eq 23",
        "exit",
        "line vty 0 4",
        "access-class 101 in",
        "exit"
        ], 
        "172.31.111.5":[
        "config t",
        "router ospf 1 vrf control-Data",
        "network 172.31.111.32 0.0.0.15 area 0",
        "network 172.31.111.48 0.0.0.15 area 0",
        "network 2.2.2.2 0.0.0.0 area 0",
        "exit",
        "ip access-list extended 101",
        "permit ospf 172.31.111.0 0.0.0.63 any",
        "permit tcp 172.31.111.0 0.0.0.7 any eq 22",
        "permit tcp 172.31.111.0 0.0.0.7 any eq 23",
        "permit tcp 10.253.190.0 0.0.0.255 any eq 22",
        "permit tcp 10.253.190.0 0.0.0.255 any eq 23",
        "exit",
        "line vty 0 4",
        "access-class 101 in",
        "exit"
        ], 
        "172.31.111.6":
        [
        "config t",
        "int g0/2",
        "ip add dhcp",
        "no shut",
        "exit",
        "access-list 1 permit 172.31.111.0 0.0.0.63",
        "ip nat inside source list 1 interface g0/2 vrf control-Data overload",
        "int g0/1",
        "ip nat inside",
        "int g0/2",
        "ip nat outside",
        "ip access-list extended 101",
        "permit ospf 172.31.111.0 0.0.0.63 any",
        "permit tcp 172.31.111.0 0.0.0.7 any eq 22",
        "permit tcp 172.31.111.0 0.0.0.7 any eq 23",
        "permit tcp 10.253.190.0 0.0.0.255 any eq 22",
        "permit tcp 10.253.190.0 0.0.0.255 any eq 23",
        "exit",
        "line vty 0 4",
        "access-class 101 in",
        "exit",
        "ip access-list standard User",
        "permit 172.31.111.0 0.0.0.63",
        "exit",
        "route-map Outside permit 10",
        "match ip address User",
        "set ip default next-hop 192.168.122.1",
        "exit",
        "router ospf 1 vrf control-Data",
        "network 172.31.111.48 0.0.0.15 area 0",
        "network 3.3.3.3 0.0.0.0 area 0",
        "default-information originate always",
        "exit"
        ]
        }

    for ip in instruction:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=ip, username="admin", pkey=private, allow_agent=False, look_for_keys=True)
        print("Connecting to {} ...".format(ip))
        with client.invoke_shell() as ssh:
            print("Connecting to {} ...".format(ip))
            run_intsuction(instruction[ip], ssh)
            result = ssh.recv(1000).decode('ascii')
            print(result)

ssh_connect()