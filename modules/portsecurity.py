from netmiko import ConnectHandler

class poersec_class:
    def port_security_func(device_info,port_number):
        try:
            
            # Connect to Device
            with ConnectHandler(**device_info) as net_connect:
                net_connect.enable()

                # Change Hostname
                config_commands = [f'interface {port_number}',
                                   "switchport port-security",
                                   "switchport port-security mac-address sticky",
                                   "switchport port-security violation restrict",
                                   "spanning-tree portfast",
                                   "spanning-tree bpduguard enable",
                                   "end",
                                   "wr"]
                output = net_connect.send_config_set(config_commands)
                net_connect.disconnect()
                return output
        except Exception as e:
            print(f"Failed to connect to Device {e}")