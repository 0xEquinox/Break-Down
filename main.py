import csv
from os import stat
from typing import List
import pandas as pd
import os.path
from datetime import date, datetime, timedelta

filename = "tasks.csv"
header = ['Task Name', 'Estimated Time', 'Days Left', 'Daily', 'Recorded Date', 'Assignment Due Date', 'Is Completed']

def start(names, estimated_time, due_date):

    today = datetime.today()
    assignment_due_date = datetime.today() + timedelta(days=due_date)

    data = {"Task Name": names, "Estimated Time": estimated_time, "Days Left": due_date, "Daily": break_down(estimated_time, due_date), 'Recorded Date': today, 'Assignment Due Date': assignment_due_date, 'Is Completed': False}

    if os.path.isfile("tasks.csv"):
        with open("tasks.csv", 'a', newline='') as myfile:
            wr = csv.DictWriter(myfile, quoting=csv.QUOTE_ALL, fieldnames=header)
            wr.writerow(data)
    else:
        with open("tasks.csv", 'a', newline='') as myfile:
            wr = csv.DictWriter(myfile, quoting=csv.QUOTE_ALL, fieldnames=header)
            wr.writeheader()
            wr.writerow(data)


def break_down(estimated_time, days_till_due):
    return int(estimated_time/days_till_due)


def check_tasks():
    csvFile = pd.read_csv('tasks.csv')
    print(csvFile)
    find_task = str(input("Enter completed task name: "))
    ans = str(input("Are you sure you want to remove" + find_task +"? Once removed, changes cannot be undone."))
    if ans == 'yes':
        print(csvFile.drop(csvFile[csvFile['Task Name'] == find_task].index))


def sort_by_break_down():
    csvFile = pd.read_csv("tasks.csv")

    print(csvFile)

    sortedByDaily = csvFile.sort_values(by=['Daily'], ascending=True)
    sortedByDaily.to_csv("tasks.csv", index=False)

    print(sortedByDaily)

def today():
    
    csvFile = pd.read_csv("tasks.csv", usecols=['Task Name', 'Daily'])
    print(csvFile)



