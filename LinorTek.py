import re
import os
import platform
from reg_test import Dev_list
import pandas as pd

with open('PalmerDev_ip.txt', 'r') as file:
    
    l = file.readlines() # give a block list with \n included in each entry
    
ip_reg = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"  #reg express the get ip address


# Making a list of ips of each school
def Dev_ip():
    ip_list = []
    for i in range(len(l)):
        ip = l[i]
        ip_addr = re.search(ip_reg, ip)
        if ip_addr:
            ip_list.append(ip_addr.group())
            
        else:
            pass
    
    return ip_list

D = Dev_list()
IP = Dev_ip()
Tot = pd.DataFrame({"Device" : D, "IP address" : IP})

item = Tot["Device"]
Dev_i = list(item.index)




def ping_ip(Devices, ip_list):

    suc = []
    unsuc = []
    
    for i in range(len(ip_list)):

            if platform.system().lower() == "windows":
                cmd = f"ping -n 1 {ip_list[i]}"
            else:
                cmd = f"ping -c 1 {ip_list[i]}"

            response = os.system(cmd)

            if response == 0:
                print(f"Ping to {ip_list[i]} sucessful.")
                suc.append(Devices[i])
            else:
                print(f"Ping to {ip_list[i]} for device {Devices[i]} not sucessful")
                unsuc.append(Devices[i])

    return suc, unsuc

A, B = ping_ip(D,IP)

ping_test = list(A + B)
print(ping_test)
