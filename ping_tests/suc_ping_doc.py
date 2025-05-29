import csv
import pandas as pd

f_name = "Successful_pings.csv"

doc = []
with open(f_name, 'r', newline='') as file:
    lines = file.readlines()
    for line in lines:
        
        doc.append(line.split(','))


print(doc[2])