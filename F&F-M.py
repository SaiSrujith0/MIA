from shutil import move
import os
import tkinter as t
from tkinter import *
from tkinter import filedialog


w=t.Tk()
w.resizable(False,False)
w.geometry("380x280")
w.title("F&F Manipulator")
w.config(background="black")

d=""

def m():
    l=Button(w,text="Select Directory",
            command=f,
            padx=4,
            pady=6,
            bg="red",

            fg="black",
            font="Ray-Ban",
            relief="groove"
            )
    l.grid(row=1,column=1,
        padx=70,
        pady=30)
    b=Button(w,text="Sort Files",
             command=s,
             padx=3,
             pady=2,
             fg="black",
            bg="white",
            font="Ray-Ban",
            relief="raised"
             )
    b.grid(row=2,column=1,
           padx=70,
           pady=10)
    b0=Button(w,text="Get Rid of Empty Folders",
             command=r,
             padx=3,
             pady=2,
             fg="black",
            bg="white",
            font="Ray-Ban",
            relief="raised"
             )
    b0.grid(row=3,column=1,
           padx=70,
           pady=20)
    


def f():
    global d
    d=filedialog.askdirectory()
def s():
    for fn in os.listdir(d):
        if os.path.isfile(os.path.join(d, fn)):
            fe = fn.split('.')[-1]
            des = os.path.join(d, fe)
        if not os.path.exists(des):
            os.makedirs(des)
            move(os.path.join(d, fn), os.path.join(des, fn))

def r():
    for root, dirs, files in os.walk(d, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)

m()

w.mainloop()