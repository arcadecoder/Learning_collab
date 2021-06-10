import pandas as pd
import numpy
import matplotlib.pyplot as plt 

ecg_df = pd.read_csv("ecg.csv")

def convert_dataframe(ecg_df):
    ''' function which 
    splits a colon delimited csv into 
    properly split dataframe
    '''

    data_list = []

    for item, value in ecg_df[0:5].iterrows():
        data = value['ms;heartrate'].split(';')
        data_dict = {
            'milisecond': data[0],
            'heartrate': data[1]
        }
        data_list.append(data_dict)
    # local function - only exists within the
    df = pd.DataFrame(data_list)

    print(df.head())
    return df



df = pd.read_csv("ecg.csv", sep=';', index_col="ms")


def plot_ecg_heart_rate(df):
    '''
    Takes data from ecg df and create a graph
    '''
    fig = plt.figure(figsize=(20,7))
    plt.plot(df[0:5000].index, df[0:5000].heartrate, linewidth=1)
    plt.xlabel("Time (ms)", fontsize=20)
    plt.ylabel("Amplitude", fontsize=20)
    plt.show()
    fig.savefig("test.pdf")
    return 

plot_ecg_heart_rate(df)