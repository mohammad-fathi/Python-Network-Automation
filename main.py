import paramiko , os , datetime

# Variables
user = input("Enter User Device: ")
password = input("Enter Password Device: ")
port = input("Enter SSH Port Device: ")
tftp = input("Enter TFTP Server IP: ")
win_user = os.getlogin()
infilepath = f"c:\\Users\\{win_user}\\Downloads\\"
outfilepath = f"c:\\Users\\{win_user}\\Downloads\\"
devicelist = "iplist.txt"
date  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')

# Paramiko 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Read IP List Devices From File "ip-list.txt"
input_file = open( infilepath + devicelist, "r")
iplist = input_file.readlines()
input_file.close()

# Connect to Device and Execute Commands and Save to file

for ip in iplist:
    ipaddr = ip.strip()
    ssh.connect(hostname=ipaddr, username=user, password=password, port=port)
    command = f"copy startup-config tftp://{tftp}/" + str(ipaddr)+ "-" + date
    stdin, stdout, stderr = ssh.exec_command(command)
    ssh.close()
    