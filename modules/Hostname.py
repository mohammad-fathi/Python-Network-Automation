from netmiko import ConnectHandler
from colorama import Fore
class hostname_class:
    def hostname_func(device_info,new_hostname):
        try:
            # Connect to Device
            with ConnectHandler(**device_info) as net_connect:
                net_connect.enable()

                # Change Hostname
                config_commands = [f'hostname {new_hostname}',
                                   "do wr"]
                output = net_connect.send_config_set(config_commands)
                net_connect.disconnect()
                print(f"{Fore.MAGENTA}{output}{Fore.RESET}")
                print(f"{Fore.GREEN} Task Done...{Fore.RESET}")        
        except Exception as e:
            print(f"Failed to connect to Device {e}")
            