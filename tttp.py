import speedtest
import csv
import time
from datetime import datetime

del_t = 90

nw = datetime.now().strftime('%m%d_%H%M')
file = f'speed_data{nw}.csv'
f = open(file, 'w')
writer = csv.writer(f)
writer.writerow(['Time', 'Download', 'Upload', 'ID', 'Sponser'])
f.close()
