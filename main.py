# Import libs
from colorama import init,Fore
init()
blue= Fore.BLUE
red=Fore.RED
cyan=Fore.CYAN
white=Fore.WHITE
green=Fore.GREEN
reset=Fore.RESET

from modules import Hostname
import functions , os

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
            password=input("Enter Password: ")
            new_hostname=input("Enter New Device Hostname: ")
            device_info={
                'device_type': 'cisco_ios',
                'ip': ip ,
                'username': user,
                'password': password,
            }
        
            # Call Function Hostname 
            Hostname.hostname_class.hostname_func(device_info=device_info,new_hostname=new_hostname)

    except Exception as e:
        print(f"{red} Error: {e}")
        input()
        continue