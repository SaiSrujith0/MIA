import psutil
import tkinter
from tkinter import *

def m():
    partition_info = psutil.disk_usage('/')
    t=(f"Total Storage : {partition_info.total / (1024 ** 3):.2f} GB")
    u=(f"Used Amount : {partition_info.used / (1024 ** 3):.2f} GB")
    f=(f"Free Amount : {partition_info.free / (1024 ** 3):.2f} GB")
    p=(f"Percentage Of Used Storage : {partition_info.percent:.2f}%")
    w=tkinter.Tk()
    w.resizable(False,False)
    w.config(background="red")
    w.geometry("700x190")
    w.title("STORAGE_USAGE %")
    def e():
        b=Button(w,text=t,
              padx=3,
              pady=5,
              fg="black",
              bg="white",
              relief="groove")
        b.grid(row=1,column=0,
            padx=15,
            pady=40)
        b1=Button(w,text=u,
                padx=3,
                pady=5,
                fg="black",
                bg="white",
                relief="groove")
        b1.grid(row=1,column=2,
                padx=15,
                pady=40)
        b1=Button(w,text=f,
                padx=3,
                pady=5,
                fg="black",
                bg="white",
                relief="groove")
        b1.grid(row=1,column=3,
                padx=15,
                pady=40)
        b1=Button(w,text=p,
                padx=3,
                pady=5,
                fg="black",
                bg="white",
                relief="groove")
        b1.grid(row=2,column=2,
                padx=70,
                pady=10)
        
    e()
    w.mainloop()


if __name__=="__main__":
    m()