import re
#import csv
import pandas as pd

with open("PalmerDev_ip.txt", 'r') as file:
    lines = file.readlines()  # 

reg = r"\w([A-Za-z-_0-9\s]+)" # this is regualar express for the school
line_list = []


def Dev_list():
    school_list = []
    for line in range(len(lines)):
        ips = lines[line]
        line_list.append(ips.strip())
        school = re.search(reg, ips)
        
        if school:
            school_list.append(school.group())
        else:
            pass
    school_list = school_list[1::]  # remove the 1st line

    return school_list



#school_list.to_csv("../data/School_list.csv")
    