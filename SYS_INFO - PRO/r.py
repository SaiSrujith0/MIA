import psutil
import tkinter
from tkinter import *

def m():
    ram_info = psutil.virtual_memory()
    t=(f"Total RAM: {ram_info.total / (1024 ** 3):.2f} GB")
    f=(f"Available RAM: {ram_info.available / (1024 ** 3):.2f} GB")
    u=(f"Used RAM: {ram_info.used / (1024 ** 3):.2f} GB")
    p=(f"RAM Usage Percentage: {ram_info.percent:.2f}%")
    w=tkinter.Tk()
    w.resizable(False,False)
    w.config(background="brown")
    w.geometry("340x300")
    w.title("RAM_USAGE %")
    def e():
        b=Button(w,text=t,
              padx=3,
              pady=10,
              fg="brown",
              bg="#ffdbac",
              relief="groove")
        b.grid(row=1,column=1,
            padx=70,
            pady=10)
        b1=Button(w,text=u,
                padx=3,
                pady=10,
                fg="brown",
                bg="#ffdbac",
                relief="groove")
        b1.grid(row=2,column=1,
                padx=70,
                pady=10)
        b1=Button(w,text=f,
                padx=3,
                pady=10,
                fg="brown",
                bg="#ffdbac",
                relief="groove")
        b1.grid(row=3,column=1,
                padx=70,
                pady=10)
        b1=Button(w,text=p,
                padx=3,
                pady=10,
                fg="brown",
                bg="#ffdbac",
                relief="groove")
        b1.grid(row=4,column=1,
                padx=80,
                pady=50)
        
    e()
    w.mainloop()

if __name__=="__main__":
    m()
