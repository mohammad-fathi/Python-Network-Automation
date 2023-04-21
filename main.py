# Define colores
from colorama import init,Fore
init()
blue= Fore.BLUE
red=Fore.RED
cyan=Fore.CYAN
white=Fore.WHITE
green=Fore.GREEN
reset=Fore.RESET

from modules import Hostname,vlan,trunk
import functions , os , getpass

# Call Functions Main Menu
while True:
    os.system("clear" or "cls")
    functions.Tools.banner(None)
    functions.Tools.options(None)

    try:
        num=input(f"{green}[ + ]{reset} Enter a Number from list: ")
        
        # Select User an option
        if num=="1":
            os.system("clear" or "cls")
        
            # Get Information Device from User
            ip=input("Enter IP Device: ")
            user=input("Enter Username: ")
            password=getpass.getpass("Enter Password: ")
            new_hostname=input("Enter New Device Hostname: ")
            device_info={
                'device_type': 'cisco_ios',
                'ip': ip ,
                'username': user,
                'password': password,
            }
        
            # Call Module Hostname 
            Hostname.hostname_class.hostname_func(device_info=device_info,new_hostname=new_hostname)

        elif num=="2":
            os.system("clear" or "cls")
            
            # Read all ip switch from iplist.txt 
            with open('iplist.txt', 'r') as f:
                ip_list = f.readlines()

                # Connect to Switches in List
                for ip in ip_list:

                    # Strip any whitespace characters from the IP
                    ip = ip.strip()

                    # Get Information Device from User
                    user=input(f"Enter Username Device {ip}: ")
                    password=getpass.getpass(f"Enter Password Device {ip}: ")
                    new_vlan=input("Enter New VLAN: ")
                    device_info={
                        'device_type': 'cisco_ios',
                        'ip': ip ,
                        'username': user,
                        'password': password,
                    }
            
                    # Call Module VALN 
                    vlan.vlan_class.vlan_func(device_info=device_info,new_vlan=new_vlan)

        elif num=="3":
            os.system("clear" or "cls")
            
            # Read all ip switch from iplist.txt 
            with open('iplist.txt', 'r') as f:
                ip_list = f.readlines()

                # Connect to Switches in List
                for ip in ip_list:

                    # Strip any whitespace characters from the IP
                    ip = ip.strip()

                    # Get Information Device from User
                    user=input(f"Enter Username Device {ip}: ")
                    password=getpass.getpass(f"Enter Password Device {ip}: ")
                    print(f"""
                    {red} Help: Please Enter full name interface
                    {white}Example:
                    {green}FastEthernet0/1 {reset}or {green} GigabitEthernet0/1 {reset}""")
                    
                    trunkport=input("Enter Trunk Ports: ")
                    device_info={
                        'device_type': 'cisco_ios',
                        'ip': ip ,
                        'username': user,
                        'password': password,
                    }
                    # Call Module Trunk 
                    trunk.trunk_class.trunk_func(device_info=device_info,trunk_port=trunkport)   

    
                    


    except Exception as e:
        print(f"{red} Error: {e}")
        input()
        continue