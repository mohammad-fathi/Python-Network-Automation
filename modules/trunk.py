from netmiko import ConnectHandler
from colorama import Fore
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
                print(f"{Fore.MAGENTA}{output}{Fore.RESET}")
                print(f"{Fore.GREEN} Task Done...{Fore.RESET}")        
        except Exception as e:
            print(f"Failed to connect to Device {e}")