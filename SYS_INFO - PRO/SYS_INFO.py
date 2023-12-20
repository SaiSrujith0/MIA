import time
import psutil
import tkinter
from tkinter import *
import c
import s
import r

w=tkinter.Tk()
w.resizable(False,False)
w.geometry("730x100")
w.title("SYS_INFO")
w.config(background="#b2beb5")

def e():
    b=Button(w,text="CPU_USAGE %",
              command=cpu,
              padx=3,
              pady=5,
              fg="#b2beb5",
              bg="black",
              relief="groove")
    b.grid(row=1,column=0,
            padx=70,
            pady=30)
    b1=Button(w,text="STORAGE_USAGE %",
              command=su,
              padx=3,
              pady=5,
              fg="#b2beb5",
              bg="black",
              relief="groove")
    b1.grid(row=1,column=4,
            padx=70,
            pady=30)
    b1=Button(w,text="RAM_USAGE %",
              command=ru,
              padx=3,
              pady=5,
              fg="#b2beb5",
              bg="black",
              relief="groove")
    b1.grid(row=1,column=8,
            padx=70,
            pady=30)




def cpu():
    c.m()

def su():
    s.m()

def ru():
    r.m()

e()
w.mainloop()