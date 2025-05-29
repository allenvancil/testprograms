import re
import os
import platform
from reg_test import Dev_list
import pandas as pd

with open('linortek_devs.txt', 'r') as file:
    
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

#Dev_list import 
D = Dev_list()
IP = Dev_ip()
Tot = pd.DataFrame({"Device" : D, "IP address" : IP})

item = Tot["Device"]
Dev_i = list(item.index)
print(Tot["Device"][2])




def ping_ip(Tot):

    suc = []
    ip_suc = []
    unsuc = []
    ip_unsuc = []
    
    for i in range(len(Tot)):

            if platform.system().lower() == "windows":
                cmd = f"ping -n 1 {Tot["IP address"][i]}"
            else:
                cmd = f"ping -c 1 {Tot["IP address"][i]}"

            response = os.system(cmd)

            if response == 0:
                print(f"Ping to {Tot['IP address'][i]} for {Tot['Device'][i]} sucessful.")
                suc.append(Tot['Device'][i])
                ip_suc.append(Tot['IP address'][i])
            else:
                print(f"Ping to {Tot["IP address"][i]} for device {Tot["Device"][i]} not sucessful")
                unsuc.append(Tot["Device"][i])
                ip_unsuc.append(Tot["IP address"][i])

    return suc, ip_suc, unsuc, ip_unsuc

A, B , C, D = ping_ip(Tot)



success_ping = pd.DataFrame({"Success" : A, "Ip address" : B})
success_ping.to_csv('Successful_pings.csv')

unsuccess_ping = pd.DataFrame({'Fail' : C, 'IP address' : D})
unsuccess_ping.to_csv('Unsuccessful_pings.csv')

print("\n\nSuccessful Pings = \n", success_ping)
print("\n\nFailed pings = \n", unsuccess_ping)
