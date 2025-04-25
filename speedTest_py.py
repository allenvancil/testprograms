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

def update_plot():
    ax.clear()
    ax.plot(timestamps, DL, label='Downloads (Mbps)', color='blue', marker='o')
    ax.plot(timestamps, UL, label='Uploads (Mbps)', color='red', marker='x')
    ax.set_xlabel('Time')
    ax.set_ylabel('Speed (Mbps)')
    ax.legend()
    ax.grid(True)
    plt.pause(1)

plt.ion()  ## this allows live plotting

fig, ax = plt.subplots()

try:
    while True:
        DLspd, ULspd = speedTest()
        time_now = datetime.now().strftime('%H:%M:%S')

        DL.append(DLspd)
        UL.append(ULspd)
        timestamps.append(time_now)



        

        update_plot()
        time.sleep(60)

except KeyboardInterrupt:
    df = {'time' : timestamps, 'Download' : DL, 'Uploads' : UL}
    df = pd.DataFrame(df)
    df.to_csv('speedtest_doc.csv')
    print("User stopped measurements...")
    plt.ioff()
    plt.show()