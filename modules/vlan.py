from netmiko import ConnectHandler

class vlan_class:
    def hostname_func(device_info,new_vlan):
        try:
            # Connect to Device
            with ConnectHandler(**device_info) as net_connect:
                net_connect.enable()

                # New VLAN
                config_commands = [f'vlan {new_vlan}',
                                   "do wr"]
                output = net_connect.send_config_set(config_commands)
                net_connect.disconnect()
                return output
        except Exception as e:
            print(f"Failed to connect to Device {e}")