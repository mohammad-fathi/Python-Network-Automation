from netmiko import ConnectHandler

# Define the device details
device = {
    'device_type': 'cisco_ios',
    'ip': 'ip',  # Replace with the switch IP address
    'interface': 'interface',
    'username': 'admin',
    'password': 'Skills39~!@',
}

# Define the interface details
device["ip"]=input("Enter Device IP: ")
device["interface"] = input("Enter Interface ID: ")

# Connect to the device
with ConnectHandler(**device) as net_connect:
    # Enter privileged EXEC mode
    net_connect.enable()
    
    # Configure the interface in access mode
    config_commands = [
        f'interface GigabitEthernet{device}',
        'no  authentication port-control auto',
        'no dot1x pae authenticator',
        'do wr',
    ]
    output = net_connect.send_config_set(config_commands)
    
    # Print the output
    print(output)