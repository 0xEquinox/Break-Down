import csv
from os import stat
from typing import List
import pandas as pd

filename = "tasks.csv"
header = ['Task Name', 'Estimated Time', 'Due Date']

def start(names, estimated_time, due_date):
        
    data = {"Task Name": names, "Estimated Time": estimated_time, "Due Date": due_date}

    with open("C:\\Users\\Drago\\TaskManager\\tasks.csv", 'a', newline='') as myfile:
        wr = csv.DictWriter(myfile, quoting=csv.QUOTE_ALL, fieldnames=header)
        wr.writeheader()
        wr.writerow(data)


def add():         
    names = str(input("Enter task name: "))
    estimated_time = float(input("Enter estimated time to complete task: "))
    due_date = float(input("Enter days until due: "))
    start(names, estimated_time, due_date)
    more= str(input("Do you have more assignments?"))
    if more == "yes":
        add()

def user_input():
    user = str(input("Enter Command: "))

    if user == 'add':
        add()
    elif user == 'sort by date':
        sort_by_date()
    elif user == 'sort by time':
        sort_by_time()


def sort_by_date():

    dict_from_csv = pd.read_csv('C:\\Users\Drago\\TaskManager\\tasks.csv', header=None, index_col=0, squeeze=True).to_dict()

    print(dict_from_csv)

    df_due_date = pd.DataFrame(dict_from_csv)
    sorted_df_due_date = df_due_date.sort_values(by='Due Date')

    print(sorted_df_due_date)



def sort_by_time():

    dict_from_csv = pd.read_csv('C:\\Users\Drago\\TaskManager\\tasks.csv', header=None, index_col=0, squeeze=True).to_dict()

    print(dict_from_csv)

    df_est_time = pd.DataFrame(dict_from_csv)
    sorted_df_est_time = df_est_time.sort_values(by='Estimated Time')

    print(sorted_df_est_time)



user_input()
sort_by_time()
sort_by_date()