import tkinter as tk
from tkinter import PhotoImage
from tkinter import *

def on_closing():
    root.destroy()

root = tk.Tk()
root.title("TO-DO List")
root.geometry("650x650+300+300")
root.resizable(False, False)
root.configure(bg="pale green")

task_list = []
def addTask ():
    task = task_entry.get()
    task_entry.delete (0, END)
    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert( END,task)
def openTaskFile():
    try:
        global task_list
        with open("task_list.txt","r") as taskfile:
            task=taskfile.readlines()
        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END,task)
    except:
        file=open('tasklist.txt','w')
        file.close()
def deleteTask(): 
    global task_list
    task =str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")
        listbox.delete( ANCHOR)

frame_header = tk.Frame(root, bg="#324052")
frame_header.place(x=0, y=10, height=70, width=650)


try:
    icon_path = "/Users/shubham/Desktop/TO_DO_Project/icon.png"
    root.iconbitmap(icon_path)
except tk.TclError as e:
    print("Error setting icon:", e)

image_path = "/Users/shubham/Desktop/TO_DO_Project/icon.png"
image = PhotoImage(file=image_path)
resized_image =image.subsample(10, 10)
image_label = tk.Label(frame_header, image=resized_image)
image_label.place(x=10, y=7)

heading = Label(root, text="WRITE DOWN ALL YOUR TASKS", font=("Times New Roman", 30, "bold"))
heading.place(x=80, y=24)

image_path_bg = "/Users/shubham/Desktop/TO_DO_Project/BG.png"
image_bg = PhotoImage(file=image_path_bg)
image_label_bg = tk.Label(root, image=image_bg)
image_label_bg.place(x=590, y=26)

frame_task = Frame(root, width=650, height=70, bg="pale green") 
frame_task.place(x=0, y=100)

task = StringVar()
task_entry = Entry(frame_task, width=60, font=("Times New Roman", 20))
task_entry.place(x=18, y=16)
task_entry.focus()

button = Button(frame_task, text="Start Adding", font="arial 20 bold", width=10,bg="#5a95ff", fg="#324052", bd=0,command=addTask)
button.place(x=479, y=18)

frame_list=Frame(root,bd=3,width=610,height=350,bg="#32405b")
frame_list.place(x=20,y=180)
listbox = Listbox(frame_list, font=("arial", 20), width=50, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="orange")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
listbox.place(x=2, y=2, width=600, height=340)


scroll = Scrollbar(frame_list)
scroll.pack(side=RIGHT, fill=Y)
listbox = Listbox(frame_list, font=("arial", 20), width=50, height=16, bg="#32405b")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)

openTaskFile()

delete_icon=PhotoImage(file="/Users/shubham/Desktop/TO_DO_Project/del.png")
Button(root,image=delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=8)






root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
