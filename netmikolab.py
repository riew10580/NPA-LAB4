from netmiko import ConnectHandler

def get_data_from_device(device_params):
    with ConnectHandler(**device_params) as ssh:
        result_shipintbr = ssh.send_command('sh ip int bri')
        result_shintdes = ssh.send_command('sh int des')
        result_iproutevrfmanage = ssh.send_command('sh ip rou vrf management | include ^C')
        result_iproutevrfcon_data = ssh.send_command('sh ip rou vrf control-Data | include ^C')
        result_showipint = ssh.send_command('sh int')
        return [result_shipintbr, result_shintdes, result_iproutevrfmanage
        , result_iproutevrfcon_data, result_showipint]

def send_description_1(device_params):
    command_sequence = ['conf t', 'int g0/0', 'description Connect to G0/2 of S0', 'int g0/1'
                        , 'description Connect to G0/2 of S1', 'int g0/2', 'description Connect to G0/1 of R2'
                        , 'int g0/3', 'description Not Use']
    with ConnectHandler(**device_params) as ssh:
        output = ssh.send_config_set(command_sequence)
        print(output)

def send_description_2(device_params):
    device_params['ip'] = '172.31.111.5' 
    command_sequence = ['conf t', 'int g0/0', 'description Connect to G0/3 of S0', 'int g0/1'
                        , 'description Connect to G0/2 of R1', 'int g0/2', 'description Connect to G0/1 of R3'
                        , 'int g0/3', 'description Not Use']
    with ConnectHandler(**device_params) as ssh:
        output = ssh.send_config_set(command_sequence)
        print(output)

def send_description_3(device_params):
    device_params['ip'] = '172.31.111.6' 
    command_sequence = ['conf t', 'int g0/0', 'description Connect to G1/0 of S0', 'int g0/1'
                        , 'description Connect to G0/2 of R2', 'int g0/2', 'description Connect to WAN'
                        , 'int g0/3', 'description Not Use']
    with ConnectHandler(**device_params) as ssh:
        output = ssh.send_config_set(command_sequence)
        print(output)
        

def get_information(device_params, intf, data):
    information = []
    shipintbr = data[0].strip().split('\n')
    for line in shipintbr[1:]:
        words = line.split()
        if words[0][0] == intf[0] and words[0][-3:] == intf[1:]:
            if words[1] == "unassigned":
                information += [words[1], words[5]]
            information += [words[1], words[4]]
    try:
        subnet = data[4].index(information[0]+"/")
        subnet = data[4][subnet+12: subnet+16]
        subnet = subnet[subnet.index("/") + 1: subnet.index("/") + 3]
    except:
        subnet = "Empty"
    return information + [subnet]

    

if __name__ == '__main__':
    
    device_ip = "172.31.111.4"
    username = 'admin'
    password = 'cisco'

    device_params = {'device_type': 'cisco_ios',
                        'ip': device_ip,
                        'username': username,
                        'password': password, 
                        
                    }
    # send_description_1(device_params)
    # send_description_2(device_params)
    # send_description_3(device_params)

    data = get_data_from_device(device_params)

    device_ips = ["172.31.111.4", "172.31.111.5", "172.31.111.6"]
    for ip in device_ips:
        device_params = {'device_type': 'cisco_ios',
                        'ip': ip,
                        'username': username,
                        'password': password, 
                        }
        print(get_information(device_params, 'G0/0', data))
        print(get_information(device_params, 'G0/1', data))
        print(get_information(device_params, 'G0/2', data))
        print(get_information(device_params, 'G0/3', data))

