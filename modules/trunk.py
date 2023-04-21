from netmiko import ConnectHandler

class trunk_class:
    def trunk_func(device_info,trunk_port):
        try:
            # Connect to Device
            with ConnectHandler(**device_info) as net_connect:
                net_connect.enable()

                # Config Trunk Port
                config_commands = [f'interface range {trunk_port}',
                                   "switchport mode trunk",
                                   "do wr"]
                output = net_connect.send_config_set(config_commands)
                net_connect.disconnect()
                return output
        except Exception as e:
            print(f"Failed to connect to Device {e}")