import speedtest
import csv
import time
from datetime import datetime

del_t = 90

# making doc to send data to
nw = datetime.now().strftime('%m%d_%H%M')
file = f'speed_data{nw}.csv'
f = open(file, 'w', newline='')
writer = csv.writer(f)
writer.writerow(['Time', 'Download', 'Upload', 'ID', 'Sponser', 'Name'])
f.close()

# performing speed test
def speedTest():
    st  = speedtest.Speedtest()

    print("\n\nfinding best server...")
    st.get_servers([])
    #print(st.get_servers([]))
    best_server = st.get_best_server()
    best_server
    print('\n...and the best server is :\n')
    print(best_server)

    v_id = best_server['id']  
    v_sponser = best_server['sponsor']  
    v_name = best_server['name']
    

    print('\nDownload speeds...')
    DLspd = st.download()/1_000_000
    #print(DLspd/1000000, 'Mbps')

    print('\nUpload speeds...')
    ULspd = st.upload()/1_000_000
    #print(ULspd/1000000, 'Mbps')

    return DLspd, ULspd, v_id, v_sponser, v_name

## create file that data will be written to


try:
    while True:
        with open(file, mode='a', newline='') as f:
            

        # getting data from speedTest function
            DLspd, ULspd, id, sponser, name = speedTest()
            print('\nappending data...\n')

        # the data want to append to csv file
            time_now = datetime.now().strftime('%H:%M')
            DL = round(DLspd, 2)
            UL = round(ULspd, 2)

            writer = csv.writer(f)
        # appending data to csv file
            writer.writerow([time_now, DL, UL, id, sponser, name])
            f.flush()
            print(f'Logged: {time_now}, {DL}, {UL}, {id}, {sponser}, {name}')
            time.sleep(del_t)
except KeyboardInterrupt:
    print('\n\nUser stopped test...\n')
    
    