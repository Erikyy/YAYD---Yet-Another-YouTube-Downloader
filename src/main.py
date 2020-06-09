import pytube
from pytube import YouTube
from tkinter import *
import tkinter
import os
import sys

window = Tk()


global yt
global listbox



def OnGoButtonClicked():
    listbox.delete(0, 'end')
    url = tfield.get()
    yt = YouTube(url)
    global list
    list = yt.streams.all()
    for x in list:
        listbox.insert('end', x)

def Download():
    selected = listbox.curselection()
    print(selected)
    for item in selected:
        list[item].download()






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
