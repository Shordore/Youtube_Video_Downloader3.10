from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("YouTube Video Downloader")

Label(root, text = "YouTube Video Downloader", font = "arial 20 bold").pack()

link = StringVar()

Label(root, text = "paste Link Here: ", font = "arial 15 bold").place(x = 160, y = 60)
link_enter = Entry(root, width = 70, textvariable = link).place(x = 30, y = 90)

def Downloadermp4():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text = "DOWNLOADED", font = "arial 15").place(x = 180, y = 210)

def Downloadermp3():
    url = YouTube(str(link.get()))
    video = url.streams.get_audio_only(subtype= "mp3")
    video.download()
    Label(root, text = "DOWNLOADED", font = "arial 15").place(x = 180, y = 210)

Button(root, text = "DOWNLOAD MP4", font = "arial 15 bold", bg = "purple", padx = 2, command = Downloadermp4).place(x = 80, y = 150)
Button(root, text = "DOWNLOAD MP3", font = "arial 15 bold", bg = "purple", padx = 2, command = Downloadermp3).place(x = 260, y = 150)





root.mainloop()
