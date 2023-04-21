# Define colores
from colorama import init,Fore
init()
blue= Fore.BLUE
red=Fore.RED
cyan=Fore.CYAN
white=Fore.WHITE
green=Fore.GREEN
reset=Fore.RESET

from modules import Hostname,vlan,trunk,portsecurity
import functions , os , getpass , time

# Call Functions Main Menu
while True:
    os.system("cls" or "clear")
    functions.Tools.banner(None)
    functions.Tools.options(None)

    try:
        num=input(f"{green}[ + ]{reset} Enter a Number from list: ")
        
        # Change hostname option
        if num=="1":
            os.system("cls" or "clear")
        
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


        #### Config Vlan #### 
        elif num=="2":
            os.system("cls" or "clear")
            
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
                    print(f"""{red}Please Enter Full Interface Name and range\n{reset}Example:\n{green}FastEthernet0/1-24 {reset} or {green}GigabitEthernet0/1-46{reset}\n""")
                    portnum=input(f"Enter Interface Port Range: ")
                    device_info={
                        'device_type': 'cisco_ios',
                        'ip': ip ,
                        'username': user,
                        'password': password,
                    }
            
                    # Call Module VALN 
                    vlan.vlan_class.hostname_func(device_info=device_info,new_vlan=new_vlan,portrange=portnum)

        # Config Trunk
        elif num=="3":
            os.system("cls" or "clear")
            
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
                    print(f"""{red}Please Enter Full Interface Name and range\n{reset}Example:\n{green}FastEthernet0/1-24 {reset} or {green}GigabitEthernet0/1-46{reset}\n""")
                    portnum=input(f"Enter Interface Port Range: ")
                    device_info={
                        'device_type': 'cisco_ios',
                        'ip': ip ,
                        'username': user,
                        'password': password,
                    }
            
                    # Call Module VALN 
                    trunk.trunk_class.trunk_func(device_info=device_info,trunk_port=portnum)

        # Config Port Security
        elif num=="4":
            os.system("cls" or "clear")
            
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
                    print(f"""{red}Please Enter Full Interface Name and range\n{reset}Example:\n{green}FastEthernet0/1-24 {reset} or {green}GigabitEthernet0/1-46{reset}\n""")
                    portnum=input(f"Enter Interface Port Range: ")
                    device_info={
                        'device_type': 'cisco_ios',
                        'ip': ip ,
                        'username': user,
                        'password': password,
                    }
            
                    # Call Module Port Security 
                    portsecurity.poersec_class.port_security_func(device_info=device_info,port_number=portnum)

    except Exception as e:
        print(f"{red} Error: {e}")
        input()
        continue