# Importing necessary packages
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog


# Defining CreateWidgets() function
# to create necessary tkinter widgets
def Widgets():

	head_label = Label(root, text="D-tool",
					padx=30,
					pady=10,
					font="League 25",
					bg="black",
					fg="white")
	head_label.grid(row=1,
					column=0,
					pady=10,
					padx=5,
					columnspan=3)

	link_label = Label(root,
					text="YouTube Link :",
					bg="black",
					fg='white',
					font="Milkshake"
					)
	link_label.grid(row=2,
					column=0,
					pady=10,
					padx=5)

	root.linkText = Entry(root,
						width=35,
						textvariable=video_Link,
						font="Arial 14")
	root.linkText.grid(row=2,
					column=1,
					pady=5,
					padx=5,
					columnspan=2)


	destination_label = Label(root,
							text="Destination :",
							bg="black",
							fg="white",
							pady=5,
							font="Milkshake",
							padx=9)
	destination_label.grid(row=3,
						column=0,
						pady=5,
						padx=5)


	root.destinationText = Entry(root,
								width=27,
								textvariable=download_Path,
								font="Arial 14")
	root.destinationText.grid(row=3,
							column=1,
							pady=5,
							padx=5)


	browse_B = Button(root,
					text="Browse",
					command=Browse,
					width=10,
					bg="white",
					fg="black",
					#font="BoldPrice",
					relief=GROOVE)
	browse_B.grid(row=3,
				column=2,
				pady=1,
				padx=1)

	Download_B = Button(root,
						text="Download 1080p",
						command=Download,
						width=20,
						bg="white",
						relief=GROOVE,
						font="Ray-Ban")
	Download_B.grid(row=4,
					column=1,
					pady=5,
					padx=1)
	Download_c = Button(root,
						text="Download 720p",
						command=Download1,
						width=20,
						bg="white",
						relief=GROOVE,
						font="Ray-Ban")
	Download_c.grid(row=5,
					column=1,
					pady=5,
					padx=1)
	Download_D = Button(root,
						text="Download 480p",
						command=Download2,
						width=20,
						bg="white",
						relief=GROOVE,
						font="Ray-Ban")
	Download_D.grid(row=6,
					column=1,
					pady=5,
					padx=1)
	
	Download_E = Button(root,
						text="Download 360p",
						command=Download3,
						width=20,
						bg="white",
						relief=GROOVE,
						font="Ray-Ban")
	Download_E.grid(row=7,
					column=1,
					pady=5,
					padx=1)
	Download_F = Button(root,
						text="Download Mp3",
						command=Download4,
						width=20,
						bg="white",
						relief=GROOVE,
						font="Ray-Ban")
	Download_F.grid(row=10,
					column=1,
					pady=5,
					padx=1)


# Defining Browse() to select a
# destination folder to save the video

def Browse():
	# Presenting user with a pop-up for
	# directory selection. initialdir
	# argument is optional Retrieving the
	# user-input destination directory and
	# storing it in downloadDirectory
	download_Directory = filedialog.askdirectory()

	# Displaying the directory in the directory
	# textbox
	download_Path.set(download_Directory)

# Defining Download() to download the video


def Download():
	Youtube_link = video_Link.get()
	download_Folder = download_Path.get()
	getVideo = YouTube(Youtube_link)
	videoStream = getVideo.streams.filter(res="1080p")
	videoStream.first().download(download_Folder)
	messagebox.showinfo("TRIUMPH",
						"Dumped Video(1080p) In\n"
						+ download_Folder)

def Download1():
	Youtube_link = video_Link.get()
	download_Folder = download_Path.get()
	getVideo = YouTube(Youtube_link)
	videoStream = getVideo.streams.filter(res='720p')
	videoStream.first().download(download_Folder)
	messagebox.showinfo("TRIUMPH",
						"Dumped Video(720p) In\n"
						+ download_Folder)

def Download2():
	Youtube_link = video_Link.get()
	download_Folder = download_Path.get()
	getVideo = YouTube(Youtube_link)
	videoStream = getVideo.streams.filter(res='480p')
	videoStream.first().download(download_Folder)
	messagebox.showinfo("TRIUMPH",
						"Dumped Video(480p) In\n"
						+ download_Folder)
	

def Download3():
	Youtube_link = video_Link.get()
	download_Folder = download_Path.get()
	getVideo = YouTube(Youtube_link)
	videoStream = getVideo.streams.filter(res='360p')
	videoStream.first().download(download_Folder)
	messagebox.showinfo("TRIUMPH",
						"Dumped Video(360p) In\n"
						+ download_Folder)
def Download4():
	Youtube_link = video_Link.get()
	download_Folder = download_Path.get()
	getVideo = YouTube(Youtube_link)
	videoStream = getVideo.streams.filter(only_audio=True)
	videoStream.first().download(download_Folder)
	messagebox.showinfo("TRIUMPH",
						"Dumped Audio(mp3) In\n"
						+ download_Folder)


# Creating object of tk class
root = tk.Tk()

# Setting the title, background color
# and size of the tkinter window and
# disabling the resizing property
root.geometry("560x440")
root.resizable(False, False)
root.title("Youtube Video Downloader")
root.config(background="black")

# Creating the tkinter Variables
video_Link = StringVar()
download_Path = StringVar()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()
