import speedtest
import matplotlib.pyplot as plt
import time
from datetime import datetime
import pandas as pd

DL = []
UL = []
timestamps = []


def speedTest():
    st  = speedtest.Speedtest()

    # print("finding best server...")
    # st.get_best_server()

    print('\nDownload speeds...')
    DLspd = st.download()/1_000_000
    #print(DLspd/1000000, 'Mbps')

    print('\nUpload speeds...')
    ULspd = st.upload()/1_000_000
    #print(ULspd/1000000, 'Mbps')
    return DLspd, ULspd


try:
    while True:
        DLspd, ULspd = speedTest()
        print('\nappending data...\n')
        time_now = datetime.now().strftime('%H:%M:%S')

        DL.append(DLspd)
        UL.append(ULspd)
        timestamps.append(time_now)
        time.sleep(120)

except KeyboardInterrupt:
    df = {'time' : timestamps, 'Download' : DL, 'Uploads' : UL}
    df = pd.DataFrame(df)
    df.to_csv('speedtest_doc.csv')
    print("User stopped measurements...")
