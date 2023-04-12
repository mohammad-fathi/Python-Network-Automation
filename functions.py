
from colorama import init,Fore
init()
blue= Fore.BLUE
red=Fore.RED
cyan=Fore.CYAN
white=Fore.WHITE
green=Fore.GREEN
reset=Fore.RESET

class Tools:
    def banner(self=None):
        print(f"""
{cyan}
'##::::'##:'########:'##:::::::'##::::::::'#######::'##:::::'##:
###::'###: ##.....:: ##::::::: ##:::::::'##.... ##: ##:'##: ##:
####'####: ##::::::: ##::::::: ##::::::: ##:::: ##: ##: ##: ##:
## ### ##: ######::: ##::::::: ##::::::: ##:::: ##: ##: ##: ##:
##. #: ##: ##...:::: ##::::::: ##::::::: ##:::: ##: ##: ##: ##:
##:.:: ##: ##::::::: ##::::::: ##::::::: ##:::: ##: ##: ##: ##:
##:::: ##: ########: ########: ########:. #######::. ###. ###::
..:::::..::........::........::........:::.......::::...::...:::        
{blue}
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        ~   Code by: Mohammad Fathi                     ~
        ~   Github: https://github.com/mohammad-fathi   ~
        ~   email: m.fathi3742@gmail.com                ~

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        {reset}""")
    

    def options(self=None):
            print(f"""
    Options:{red}
    
      [ 1 ]   -   Hostname
      [ 2 ]   -   VLAN
      [ 3 ]   -   Trunk
      [ 4 ]   -   ARP Inspection
      [ 5 ]   -   DHCP Snooping
      [ 6 ]   -   Port Security
      [ 7 ]   -   Backup
      [ 8 ]   -   IEEE 802.1x
      [ 0 ]   -   Custome Configuration
""")