import pytube
from pytube import YouTube
from tkinter import *
import tkinter
import os
import sys

window = Tk()



def YT():

    YT.url = tfield.get()
    YT.yt = YouTube(YT.url)#, on_progress_callback=download_progress)
    YT.list = YT.yt.streams
#    YT.filesize = YT.yt.streams.first().filesize
def OnGoButtonClicked():
    YT()

    listbox.delete(0, 'end')
    for x in YT.list:
        listbox.insert('end', x)


def Download():
    selected = listbox.curselection()
    for item in selected:
        YT.list[item].download()

#def download_progress(stream=None, chunk=None, file_handle=None, remaining=None):
#    YT()
#    percent =(100*(YT.filesize))/YT.filesize
#    print("{:00.0f}% downloaded".format(percent))

#Need to get file size from list[item]
#AttributeError: 'list' object has no attribute 'filesize'

window.title("Yet Another YouTube Downloader")
window.geometry('800x500')
frame = Frame(window)
listbox = Listbox(frame, width=120, height=20, selectmode = SINGLE)
scrollbar = Scrollbar(frame)

listbox.config(yscrollcommand = scrollbar.set)
tfield = Entry(window, width=50)
tfield.place(x=90, y=350)
button = Button(window, text="Go", width=10, command = OnGoButtonClicked)
button.place(x=5, y=350)

button2 = Button(window, text="Download", width=10, command = Download)
button2.place(x=5, y=400)


scrollbar.pack(side=RIGHT, fill= Y)
scrollbar.config(command = listbox.yview)



frame.pack()
listbox.pack()
window.mainloop()
