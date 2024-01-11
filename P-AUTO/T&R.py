import pyautogui as p
import time
import tkinter
from tkinter import *


r=tkinter.Tk()
r.resizable(False,False)
r.title("Enter TabCount")
r.config(background="black")
r.geometry("350x180")
n=StringVar()

def w():
    l=Entry(r,textvariable=n)
    l.focus()
    l.grid(row=0,column=2,padx=100,pady=40)
    b=Button(r,text="Enter",
             command=c,
             padx=6,
             pady=3,
             fg="black",
             bg="white",
             relief="groove")
    b.grid(row=1,column=2,padx=100)
    r.bind("<Return>",c)



def c(e):
    s=int(n.get())

    p.hotkey(["win","tab"])
    time.sleep(2)
    p.press("end")
    time.sleep(1)

    for i in range(s):
        p.hotkey(["ctrlleft","f4"])
        time.sleep(1)

    p.hotkey(["win","m"])
    time.sleep(1)

    for i in range(3):
        p.press("f5")
        time.sleep(2)

w()
r.mainloop()

