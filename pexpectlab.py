import pexpect

def pexpect_lab(num):
    PROMPT = '#'
    IP = '172.31.111.' + str(num+3)
    Loopback_IP = '.'.join([str(num)]*4)
    USERNAME = 'admin'
    PASSWORD = 'cisco'
    
    child = pexpect.spawn('telnet '+ IP)
    child.expect('Username')
    child.sendline(USERNAME)
    child.expect('Password')
    child.sendline(PASSWORD)
    child.expect(PROMPT)
    child.sendline('conf t')
    child.expect(PROMPT)
    child.sendline('int lo 0')
    child.expect(PROMPT)
    child.sendline('ip address %s 255.255.255.255'%Loopback_IP)
    child.expect(PROMPT)
    child.sendline('end')
    child.expect(PROMPT)
    child.sendline('show ip int bri')
    child.expect(PROMPT)
    result = child.before
    print(result.decode('UTF-8'))
    print()
    child.sendline('exit')
pexpect_lab(1)
pexpect_lab(2)
pexpect_lab(3)
