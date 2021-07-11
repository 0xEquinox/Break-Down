import tkinter
from tkinter.constants import LEFT, END
import tkinter.messagebox
from main import *
from tkinter import *

def delete():        
    taskIndex = listBox.curselection()[0]
    listBox.delete(taskIndex)
    
    

def refresh():
    size = listBox.size()
    listBox.delete(0, size)
    

def delete_input():
    enterTask.delete(0, END)
    enterTask.insert(0, "")
    timeToComplete.delete(0, END)
    timeToComplete.insert(0, "")
    daysUntilDue.delete(0, END)
    daysUntilDue.insert(0, "")


def addTask():
    task = enterTask.get()
    time = timeToComplete.get()
    due = daysUntilDue.get()
    if task != "":
        start(str(task), float(time), float(due))
        delete_input()
        refresh()
    else:
        tkinter.messagebox.showwarning(
            title="Warning!", message="Value not entered in one or more text boxes")

# loads the data from the csv file


def load():
    sort_by_break_down()
    with open("tasks.csv") as myFile:
        reader = csv.DictReader(myFile, delimiter=',')
        for row in reader:
            name = row['Task Name']
            time = row['Estimated Time']
            date = row['Days Left']
            isCompleted = row['Is Completed']
            daily = row['Daily']
            if isCompleted == "False":
                listBox.insert(1, name + "                           " + daily + "  Minutes" + 
                            "                                          " + date)


root = tkinter.Tk()
root.title("Break Down")
root.resizable(False, False)

listBox = tkinter.Listbox(root, height=20, width=40, relief=SOLID)
listBox.grid(column=0, padx=10, columnspan=2)

enterTask = tkinter.Entry(root, width=10, justify=LEFT)

timeToComplete = tkinter.Entry(root, width=10, justify=LEFT)

daysUntilDue = tkinter.Entry(root, width=10, justify=LEFT)


# add task button
add_image = PhotoImage(file = "assets\\Plus-Button.png")
addTaskButton = tkinter.Button(
    root,image=add_image ,text="Add task", command=lambda: [addTask(), load()], borderwidth=0)
addTaskButton.grid(column=1, row=2)

# delete button
minus_image = PhotoImage(file="assets\\minus-sign.png")
deleteTasks = tkinter.Button(
    root,image=minus_image ,text="Delete task", command=delete, borderwidth=0)
deleteTasks.grid(row=2, column=0)

labelEnterTask = tkinter.Label(root, text="Enter task name:")
labelEnterTask.grid(row=5, column=0)

labelTimeToComplete = tkinter.Label(root, text="Enter time to complete task:")
labelTimeToComplete.grid(row=6, column=0)

labelDaysUntilDue = tkinter.Label(root, text="Enter the days until the task is due:")
labelDaysUntilDue.grid(row=7, column=0)

enterTask = tkinter.Entry(root, width=10, relief=SOLID)
enterTask.grid(row=5, pady=8, column=1)

timeToComplete = tkinter.Entry(root, width=10, relief=SOLID)
timeToComplete.grid(row=6, pady=8, column=1)

daysUntilDue = tkinter.Entry(root, width=10, relief=SOLID)
daysUntilDue.grid(row=7, pady=8, column=1)

if os.path.isfile("tasks.csv"):
    load()

root.mainloop()
