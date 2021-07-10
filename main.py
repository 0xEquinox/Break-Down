import csv
from os import stat
from typing import List
import pandas as pd
import os.path
from datetime import date, datetime, timedelta

filename = "tasks.csv"
header = ['Task Name', 'Estimated Time', 'Due Date', 'Daily']

def start(names, estimated_time, due_date):

    today_date = date.today()
    data = {"Task Name": names, "Estimated Time": estimated_time, "Due Date": due_date, "Daily": break_down(estimated_time, due_date)}

    if os.path.isfile("C:\\Users\\Drago\\TaskManager\\tasks.csv"):
        with open("C:\\Users\\Drago\\TaskManager\\tasks.csv", 'a', newline='') as myfile:
            wr = csv.DictWriter(myfile, quoting=csv.QUOTE_ALL, fieldnames=header)
            wr.writerow(data)
    else:
        with open("C:\\Users\\Drago\\TaskManager\\tasks.csv", 'a', newline='') as myfile:
            wr = csv.DictWriter(myfile, quoting=csv.QUOTE_ALL, fieldnames=header)
            wr.writeheader()
            wr.writerow(data)


def break_down(estimated_time, days_till_due):
    return float(estimated_time/days_till_due)

def add():         
    names = str(input("Enter task name: "))
    estimated_time = float(input("Enter estimated time to complete task: "))
    due_date = float(input("Enter days until due: "))
    start(names, estimated_time, due_date)
    more= str(input("Do you have more assignments?"))
    if more == "yes":
        add()
    else:
        user_input()

def user_input():
    user = str(input("Enter Command: "))

    if user == 'add':
        add()
    elif user == 'sort by date':
        sort_by_date()
    elif user == 'sort by time':
        sort_by_time()


def sort_by_date():

    csvFile = pd.read_csv("C:\\Users\\Drago\\TaskManager\\tasks.csv")

    print(csvFile)

    sortedByDate = csvFile.sort_values(by=["Due Date"], ascending=True)
    sortedByDate.to_csv("C:\\Users\\Drago\\TaskManager\\tasks.csv", index=False)

    print(sortedByDate)

    
def sort_by_time():

    csvFile = pd.read_csv("C:\\Users\\Drago\\TaskManager\\tasks.csv")

    print(csvFile)

    sortedByDate = csvFile.sort_values(by=["Estimated Time"], ascending=False)
    sortedByDate.to_csv("C:\\Users\\Drago\\TaskManager\\tasks.csv", index=False)

    print(sortedByDate)



user_input()
