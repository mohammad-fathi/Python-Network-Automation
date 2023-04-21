![Main menu](./images/menu.png)
# Configure Cisco Devices
before use script, enable ssh v2 and set user and password for all switche

- Enable SSHv2:
```
Router(config)#crypto key generate rsa 
How many bits in the modulus [512]: 2048
```

- Enable SSH in vty:
```
Router(config)#line vty 0 4
Router(config-line)# login local
Router(config-line)# transport input ssh
Router(config)#line vty 5 15
Router(config-line)# login local
Router(config-line)# transport input ssh
```
- Create User:
```
username admin privilege 15 password 0 YOURPASSWORD
```

> NOTE: in file `iplist.txt` define all ip switches.

## Modules:
- Change Hostname
- Configure VLAN and join Ports to vlan
- Configure Trunk Port
- Configure Port-Security and Spanning-tree Port fast and BPDU Guard
- Backup from Device and store to local directory
- You can run any command with module "Custome Configuration" in all devices
