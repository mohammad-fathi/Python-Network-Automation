from netmiko import ConnectHandler
from colorama import Fore
import time
class custome_class:
    def custome_func(device_info,usercommand):
        try:
            # Connect to Device
            with ConnectHandler(**device_info) as net_connect:
                net_connect.enable()
                outputs = []
                output = net_connect.send_config_set(usercommand)
                outputs.append(output)
                net_connect.disconnect()
                print(f"{Fore.MAGENTA}{output}{Fore.RESET}")
                print(f"{Fore.GREEN} Task Done...{Fore.RESET}")        
                while True:
                    if input("Press Enter to Main Menu...")=="":
                        break
        except Exception as e:
            print(f"Failed to connect to Device {e}")