from netmikolab import *

def test_ip_1(ip, username, password, device_params):
    assert get_information(device_params, "G0/0", data) == ["172.31.111.4", "up", "28"]
    assert get_information(device_params, "G0/1", data) == ["172.31.111.17", "up", "28"]
    assert get_information(device_params, "G0/2", data) == ["172.31.111.33", "up", "28"]
    assert get_information(device_params, "G0/3", data) == ['unassigned', 'down', 'unassigned', 'administratively', 'Empty']
    print('test_ip passed')

def test_ip_2(ip, username, password, device_params):
    assert get_information(device_params, "G0/0", data) == ["172.31.111.5", "up", "28"]
    assert get_information(device_params, "G0/1", data) == ["172.31.111.34", "up", "28"]
    assert get_information(device_params, "G0/2", data) == ["172.31.111.49", "up", "28"]
    assert get_information(device_params, "G0/3", data) == ['unassigned', 'down', 'unassigned', 'administratively', 'Empty']
    print('test_ip passed')

def test_ip_3(ip, username, password, device_params):
    assert get_information(device_params, "G0/0", data) == ["172.31.111.6", "up", "28"]
    assert get_information(device_params, "G0/1", data) == ["172.31.111.50", "up", "28"]
    assert get_information(device_params, "G0/3", data) == ['unassigned', 'down', 'unassigned', 'administratively', 'Empty']
    print('test_ip passed')

device_ip = '172.31.111.4'
username = 'admin'
password = 'cisco'

device_params = {'device_type': 'cisco_ios',
               'ip': device_ip,
               'username': username,
               'password': password, }

data = get_data_from_device(device_params) 

test_ip_1('172.31.111.4', username, password, device_params)
device_params['ip'] = '172.31.111.5' 
data = get_data_from_device(device_params)
test_ip_2('172.31.111.5', username, password, device_params)
device_params['ip'] = '172.31.111.6'
data = get_data_from_device(device_params)
test_ip_3('172.31.111.6', username, password, device_params)