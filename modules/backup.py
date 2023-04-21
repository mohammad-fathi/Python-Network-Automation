from netmiko import ConnectHandler
from colorama import Fore
import datetime,os
class backup_class:
    def backup_func(device_info):
        try:
            
            # Establish the SSH connection to the switch and sen Commands
            with ConnectHandler(**device_info) as net_connect:
                # net_connect.enable()
                config = net_connect.send_command('show running-config')
                
                # Create a backup directory if it doesn't exist
                today = datetime.date.today().strftime('%Y-%m-%d')
                backup_dir = f'Backups/{today}'
                os.makedirs(backup_dir, exist_ok=True)

                # Save the configuration to a file
                file_name = f'{backup_dir}/{device_info["ip"]}.txt'
                with open(file_name, 'w') as file:
                    file.write(config)

                net_connect.disconnect()
                print(f'{Fore.GREEN} Backup {device_info["ip"]} Done...{Fore.RESET}')
                while True:
                    if input("Press Enter to Main Menu...")=="":
                        break
        except Exception as e:
            print(f"Failed to connect to Device {e}")
            