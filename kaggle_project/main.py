import pandas as pd
import numpy

ecg_df = pd.read_csv("ecg.csv")
#print(ecg_df.head())


def convert_dataframe(ecg_df):
    ''' function which 
    splits a colon delimited csv into 
    properly split dataframe'''

    data_list = []

    for item, value in ecg_df[0:5].iterrows():
        data = value['ms;heartrate'].split(';')
        data_dict = {
            'milisecond': data[0],
            'heartrate': data[1]
        }
        data_list.append(data_dict)

    print(data_list)

    df = pd.DataFrame(data_list)

    print(df.head())