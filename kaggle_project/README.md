# ECG DATA PROJECT TO SUPPORT HRV ANALYSIS

This project folder supports learning and experimentation for HRV data using python and pandas. 

## Data 
The Data we are using in this project is from the Kaggle website. The methodology used in some submissions can be found at Here: [Kaggle - Exploring Heart Rate Variability using Python](https://www.kaggle.com/stetelepta/exploring-heart-rate-variability-using-python/notebook?select=ecg.csv)

## Setup
This requires a virtual envionrment to cbe created and activated.

A virtual environment is a an "envionrment" which keeps any packages/dependancies to be installed seperate. *VERY IMPORTANT* for python developmnent. 

The commands: 
* py  - invokes the python language 
* -m  - make 
* venv - short for virtual envionrment
* env is the name of the virtual envionment, you could name it anything else you want alternatively.

``` Bash
py -m venv env
```
After creating the virtual environment, you need to activate it using if you are on a windows computer:

``` Bash
source env/Scripts/activate
```

In this directory you will find a **requirements.txt file**. This contains all the packages installed that are necessary. 

To install the package, first make sure youre virtual envrionment is activate and then use in the Git Bash terminal:
```Bash 
py -m pip freeze > requirements.txt
```



## Code from 04/06/2021
The following code can be found in the main.py file. 
The data from the kaggle data, was not properly comma delimited/seperated, to ensure the miliseconds and heartrate were in seperate columns, we wanted to split this & add it to a new dataframe for exporting/manipulating the data for visualisation. 


1. Iterate/pass over each item in the dataframe by using a For loop. 
2. Split the string data in the rows by the ;
3. Create a new dictionary for each row which seperates the data. 
4. add each new dictionary to a precreated list. 
5. Convert the list of dictionaries into a dataframe. 
6. It is now cleanly seperated.


```Python

ecg_df = pd.read_csv("ecg.csv")

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

```


## Making changes
Before submiting any changes to the code clone the repository and create a seperate branch. 

### .gitignore
Used for where we do not want to track changes against a particular folder/directory or file. In particular we have the env/ directory listed in the git ignore because it is too large a folder to track changes against and is not necessary. 