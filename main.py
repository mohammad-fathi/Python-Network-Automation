
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

while True:
    os.system("clear" or "cls")
    functions.Tools.banner(None)
    functions.Tools.options(None)

    try:
        num=input(f"{green}[ + ]{reset} Enter a Number from list: ")
        if num=="4":
            os.system("clear" or "cls")
            disable_dot1x.device["ip"]=input("Enter Device IP: ")
    except Exception as e:
        print(f"{red} Error: {e}")
        input()
        continue