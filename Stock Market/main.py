import os
import pandas as pd
import matplotlib.pyplot as plt
BASE_URL = 'Raw_Data'
files = os.listdir(BASE_URL)
valid_count = 0
for count,i in enumerate(range(2)):
    df = pd.read_csv(BASE_URL+'/'+files[i])
    if df.empty:
        pass
    #Reverse df
    else:
        valid_count+=1
        df = df.reindex(index=df.index[::-1])
        print(df.keys())
        plt.plot(df.Close)
        plt.scatter(df['High'],df['Low'])
        plt.show()

