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




scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill= Y)

window.title("Yet Another YouTube Downloader")
window.geometry('800x500')
listbox = Listbox(window, width=500, height=20, yscrollcommand = scrollbar.set, selectmode = SINGLE)
scrollbar.config(command = listbox.yview)
tfield = Entry(window, width=50)
tfield.place(x=90, y=350)
button = Button(window, text="Go", width=10, command = OnGoButtonClicked)
button.place(x=5, y=350)

button2 = Button(window, text="Download", width=10, command = Download)
button2.place(x=5, y=400)

listbox.pack()
window.mainloop()
