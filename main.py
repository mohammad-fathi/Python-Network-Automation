# Import libs
from colorama import init,Fore
init()
blue= Fore.BLUE
red=Fore.RED
cyan=Fore.CYAN
white=Fore.WHITE
green=Fore.GREEN
reset=Fore.RESET

from modules import disable_dot1x,enable_dot1x,backup
import functions
import os

# Call Functions 
while True:
    os.system("clear" or "cls")
    functions.Tools.banner(None)
    functions.Tools.options(None)

# Select User an option
    try:
        num=input(f"{green}[ + ]{reset} Enter a Number from list: ")
        
    except Exception as e:
        print(f"{red} Error: {e}")
        input()
        continue