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
    ip_list = pd.DataFrame(ip_list)
    ip_list = ip_list.values
    return ip_list

LL = Dev_list()
II = Dev_ip()
All = LL+', '+II
print(All[2][0])

# def ping_ip(ip_list):
    
#     for i in ip_list:

#             if platform.system().lower() == "windows":
#                 cmd = f"ping -n 1 {i}"
#             else:
#                 cmd = f"ping -c 1 {i}"

#             response = os.system(cmd)

#             if response == 0:
#                 print(f"Ping to {i} sucessful.")
                
#             else:
#                 print(f"Ping to {i} not sucessful")

# ping_ip(ip_list)