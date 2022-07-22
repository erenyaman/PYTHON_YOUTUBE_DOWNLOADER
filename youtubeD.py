import tkinter as tk
from tkinter import *
from tkinter.tix import COLUMN
from pytube import YouTube
from tkinter import filedialog, messagebox

#UI
def createWidgets():
    
    #youtube link field
    link_label = Label(root, text="Place the URL here >> ", bg="#E8D579")
    link_label.grid(row=1, column=0, pady=5, padx=5)
    
    root.link_text = Entry(root, width=60, textvariable=video_link)
    root.link_text.grid(row=1, column=1, pady=5, padx=5)
    
    dest_label = Label(root, text="Destination >> ", bg="#E8D579")
    dest_label.grid(row=2, column=0, pady=5, padx=5 )
    
    root.dest_text = Entry(root, width=45, textvariable=down_path)
    root.dest_text.grid(row=2, column=1, pady=3, padx=3)
    
    #path button
    browse_button = Button(root, text="Where to?", command=browse, width=10, bg="#E8D579")
    browse_button.grid(row=2, column=2, pady=1, padx=1)
    
    #download button
    down_button = Button(root, text="Get it!", command=download_video, width=25, bg="#E8D579")
    down_button.grid(row=3, column=1, pady=3, padx=3)
    
def browse():
    down_dir = filedialog.askdirectory(initialdir="Your path")
    down_path.set(down_dir)

#download preferences
def download_video():
    url = video_link.get()
    folder = down_path.get()
    
    get_video = YouTube(url)
    get_stream = get_video.streams.get_highest_resolution()
    get_stream.download(folder)
    
    messagebox.showinfo("You got it bossé!", "Check the path...")
    

root =tk.Tk()

root.geometry("600x120")
root.title("YouTube Downloader")
root.config(background="#000000")

video_link = StringVar()
down_path = StringVar()

createWidgets()
root.mainloop()