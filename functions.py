from colorama import init,Fore
init()
blue= Fore.BLUE
red=Fore.RED
cyan=Fore.CYAN
white=Fore.WHITE
green=Fore.GREEN
reset=Fore.RESET

class Tools:
# Function Banner    
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

# Function Options        
    def options(self=None):
            print(f"""
    Options:{red}
    
      [ 1 ]   -   Hostname
      [ 2 ]   -   VLAN
      [ 3 ]   -   Trunk
      [ 4 ]   -   Port Security and Spaning tree
      [ 5 ]   -   Backup
      [ 6 ]   -   Custome Configuration
      [ 0 ]   -   Exit
""")