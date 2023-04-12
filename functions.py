
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
    
      [ 1 ]   -   VLAN
      [ 2 ]   -   Port Security
      [ 3 ]   -   Backup
      [ 4 ]   -   Disable IEEE 802.1x
      [ 5 ]   -   Enable IEEE 802.1x
""")