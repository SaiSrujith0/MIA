import speedtest as st
import tkinter
from tkinter import *

def m():
    s= st.Speedtest()
    s.get_best_server()
    download_speed = s.download()
    upload_speed = s.upload()
    d=(f"{download_speed / 10**6:.2f} Mbps")
    u=(f"{upload_speed / 10**6:.2f} Mbps")
    w=tkinter.Tk()
    w.title("SpeedTester")
    w.config(background="yellow")
    w.geometry("250x140")
    w.resizable(False,False)
    def e():
        l=Button(w,text="Test Network Speed\n(Mbps)",command=a,padx=4,pady=6,
                 fg="black",bg="white",relief="groove")
        l.grid(row=1,column=2,pady=40,padx=65)
    def a():
        r=tkinter.Tk()
        r.config(background="pink")
        r.geometry("290x330")
        r.title("Speed Test Details")
        r.resizable(False,False)
        def w():
            l=Button(r,text="\nDownload Speed\n"+d+"\n",padx=5,pady=6,fg="black",bg="white",relief="groove")
            l.grid(row=1,column=2,padx=90,pady=50)
            l=Button(r,text="\nUpload Speed\n"+u+"\n",padx=13,pady=6,fg="black",bg="white",relief="groove")
            l.grid(row=2,column=2,padx=90,pady=10)
        w()
        r.mainloop()
    e()
    w.mainloop()

if __name__=="__main__":
    m()
