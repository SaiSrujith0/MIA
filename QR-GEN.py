import pyqrcode
import qrcode
import tkinter as t
from tkinter import *
from tkinter import messagebox
import os

c=os.getcwd()
root=t.Tk()
root.geometry("443x300")
root.title("QR CODE GENERATOR")
root.resizable(False,False)
root.config(background="pink")
d,s="",""

def Widgets():

	head_label = Label(root, text="QR-GEN",
					padx=30,
					pady=10,
					font="League 25",
					bg="pink",
					fg="skyblue")
	head_label.grid(row=1,
					column=0,
					pady=10,
					padx=5,
					columnspan=3)

	link_label = Label(root,
					text="Drop Link :",
					bg="skyblue",
					fg='pink',
					pady=5,
					padx=9,
					font="Milkshake"
					)
	link_label.grid(row=2,
					column=0,
					pady=5,
					padx=5)

	root.linkText = Entry(root,
						width=27,
						textvariable=s,
						font="Arial 14")
	root.linkText.grid(row=2,
					column=1,
					pady=5,
					padx=5,
					columnspan=2)


	destination_label = Label(root,
							text="Drop Text :",
							bg="skyblue",
							fg="pink",
							pady=5,
							font="Milkshake",
							padx=9)
	destination_label.grid(row=3,
						column=0,
						pady=5,
						padx=5)


	root.destinationText = Entry(root,
								width=27,
								textvariable=d,
								font="Arial 14")
	root.destinationText.grid(row=3,
							column=1,
							pady=5,
							padx=5)

	Download_B = Button(root,
						text="From Link",
						command=ytg,
						width=20,
						bg="skyblue",
						fg='pink',
						relief=GROOVE,
						font="Ray-Ban")
	Download_B.grid(row=4,
					column=1,
					pady=5,
					padx=1)
	Download_c = Button(root,
						text="From Text",
						command=ttg,
						width=20,
						bg="skyblue",
						fg='pink',
						relief=GROOVE,
						font="Ray-Ban")
	Download_c.grid(row=5,
					column=1,
					pady=5,
					padx=1)
	

def ytg():
	#"https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"#
	url = pyqrcode.create(s) 
	url.svg("MiaQR-L.png", scale = 8)
	messagebox.showinfo("TRIUMPH","QR of Link is dumped into "+c+"\MiaQR-L.png")
def ttg():
	'''data = input("enter text :")
	img = qrcode.make(data)
	img.save('MiaQR1.svg')'''
	qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)
	qr.add_data(d)
	qr.make(fit = True)
	img = qr.make_image(fill_color = 'white',
                    back_color = 'black')
	img.save('MiaQR-T.png')
	messagebox.showinfo("TRIUMPH","QR of Text is dumped into "+c+"\MiaQR-T.png")
Widgets()
root.mainloop()