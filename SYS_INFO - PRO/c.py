import psutil
import time
import tkinter
from tkinter import *

def m():
    l=[0,0,0,0,0,0,0,0]

    w=tkinter.Tk()
    w.geometry("260x380")
    w.title("CPU_USAGE %")
    w.resizable(False,False)
    w.config(background="pink")

    def e():
        m=Button(w,text="Core 1\n"+str(l[0]),
                padx=4,
                pady=6,
                fg="skyblue",
                bg="white",
                relief="groove")
        m.grid(row=1,column=1,
            padx=40,
            pady=20)
        m=Button(w,text="Core 2\n"+str(l[1]),
                padx=4,
                pady=6,
                fg="skyblue",
                bg="white",
                relief="groove")
        m.grid(row=1,column=4,
            padx=40,
            pady=20)
        m=Button(w,text="Core 3\n"+str(l[2]),
                padx=4,
                pady=6,
                fg="skyblue",
                bg="white",
                relief="groove")
        m.grid(row=2,column=1,
            padx=40,
            pady=20)
        m=Button(w,text="Core 4\n"+str(l[3]),
                padx=4,
                pady=6,
                fg="skyblue",
                bg="white",
                relief="groove")
        m.grid(row=2,column=4,
            padx=40,
            pady=20)
        m=Button(w,text="Core 5\n"+str(l[4]),
                padx=4,
                pady=6,
                fg="skyblue",
                bg="white",
                relief="groove")
        m.grid(row=3,column=1,
            padx=40,
            pady=20)
        m=Button(w,text="Core 6\n"+str(l[5]),
                padx=4,
                pady=6,
                fg="skyblue",
                bg="white",
                relief="groove")
        m.grid(row=3,column=4,
            padx=40,
            pady=20)
        m=Button(w,text="Core 7\n"+str(l[6]),
                padx=4,
                pady=6,
                fg="skyblue",
                bg="white",
                relief="groove")
        m.grid(row=4,column=1,
            padx=40,
            pady=20)
        m=Button(w,text="Core 8\n"+str(l[7]),
                padx=4,
                pady=6,
                fg="skyblue",
                bg="white",
                relief="groove")
        m.grid(row=4,column=4,
            padx=40,
            pady=20)
    def c():
        cpu_percent_per_core = psutil.cpu_percent(percpu=True, interval=1)
        for core, percent in enumerate(cpu_percent_per_core):
            l[core]=percent
    c()
    e()
    w.mainloop()

if __name__=="__main__":
    m()