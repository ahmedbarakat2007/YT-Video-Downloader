from tkinter import * 
from pytube import YouTube 
from PIL import ImageTk, Image  
import webbrowser
from tkinter import messagebox
import os
import tkinter as tkk
from tkinter import ttk
import tkinter as tk
import moviepy.editor as mpe
import pytube
import shutil

root = Tk()
root.geometry ('640x600') # Size of the window
root.resizable(0, 0) # makes the window adjustable with its features
root.configure(bg="#1f242b")
root.iconbitmap("Textures\icon.ico")
title = tk.StringVar

def download():
    vname = "clip.mp4"
    aname = "audio.mp3"
    try:
       global title
       title = pytube.YouTube(str(link.get())).title
    except:
        msg = messagebox.showerror( "ERROR!!!!", "Connection Error")

    # Download video and rename
    msg = messagebox.askokcancel( "Alert", "Are you Sure You want to download " + title + " as MP4 File")
    if msg:
        abc= "1"
    else:
        return
    try:
        video = pytube.YouTube(str(link.get())).streams.filter(subtype='mp4', res=n.get()).first().download("Process")
        os.rename(video ,"Process/" + vname)

# Download audio and rename
        audio = pytube.YouTube(str(link.get())).streams.filter(only_audio=True).first().download("Process")
        os.rename(audio,"Process/" + aname)
    except:
        msg = messagebox.showerror( "ERROR!!!!", "Something Wrong happened")

# Setting the audio to the video
    try:
        video = mpe.VideoFileClip("Process/" +vname)
        audio = mpe.AudioFileClip("Process/" +aname)
        final = video.set_audio(audio)

    # Output result
        final.write_videofile("video.mp4")
        shutil.move("video.mp4", "Downloaded Videos/")
        os.rename("Process/video.mp4",title + ".mp4")

# Delete video and audio to keep the result
        os.remove("Process/clip.mp4")
        os.remove("Process/audio.mp3")
    except:
        msg = messagebox.showerror( "ERROR!!!!", "Something Wrong happened")

def download1():
    try: 
        url = YouTube(str(link.get())) #This captures the link(url) and locates it from YouTube.
    except: 
        msg = messagebox.showerror( "ERROR!!!!", "Connection Error")
    global title
    title = url.title
    msg = messagebox.askokcancel( "Alert", "Are you Sure You want to download " + title + " as MP3 File")
    if msg:
       abc= "1"
    else:
        return
    video = url.streams.filter(only_audio=True).first()
    try:
       out_file = video.download("Downloaded Audios")
       base, ext = os.path.splitext(out_file)
       new_file = base + '.mp3'
       os.rename(out_file, new_file) 
       msg = messagebox.showinfo( "Alert", "Downloaded Go Check Download Folder")
    except:
        msg = messagebox.showerror( "ERROR!!!!", "Something Wrong happened")

def openyoutube():
    webbrowser.open ("https://www.youtube.com")

def videos():
    path = "Downloaded Videos"
    path = os.path.realpath(path)
    os.startfile(path)

def audios():
    path = "Downloaded Audios"
    path = os.path.realpath(path)
    os.startfile(path)

def downloadpage():
    def close_loading():
        m3.destroy()
    def donothing():
        pass

    m3 = tk.Tk()
    m3.geometry('200x100')
    m3.resizable(0,0)
    m3.iconbitmap("Textures\icon.ico")
    m3.protocol('WM_DELETE_WINDOW',donothing)
    m3.configure(bg="#1f242b")
    m3.title('Loading...')
    Label(m3,bg="#1f242b").pack()
    Label(m3, text='Downloading....',bg="#1f242b",fg='white', font='san-serif 14 bold').pack()
    Label(m3, text='It Might Take 5 Minutes',bg="#1f242b",fg='white', font='san-serif 10 bold').pack()
    download()
    close_loading()
    m3.mainloop()

def downloadpage1():
    def close_loading():
        m4.destroy()
    def donothing():
        pass

    m4 = tk.Tk()
    m4.geometry('200x100')
    m4.resizable(0,0)
    m4.protocol('WM_DELETE_WINDOW',donothing)
    m4.iconbitmap("Textures\icon.ico")
    m4.configure(bg="#1f242b")
    m4.title('Loading...')
    Label(m4,bg="#1f242b").pack()
    Label(m4, text='Downloading....',bg="#1f242b",fg='white', font='san-serif 14 bold').pack()
    download1()
    close_loading()
    m4.mainloop()
    

def about():
    def github():
       webbrowser.open('https://github.com/ahmedbarakat2007')
    def web():
       webbrowser.open('https://ahmed-barakat.netlify.com')
    m5 = Tk()
    m5.geometry("200x200")
    m5.resizable(0, 0)
    m5.title("About")
    m5.configure(bg='#1f242b')
    
    Label(m5, text = "",bg="#1f242b",fg='white').pack()
    Label(m5, text="YT Downloader", font='san-serif 14 bold',bg="#1f242b",fg='white' ).pack()
    Label(m5, text="Version : 2.0", font='san-serif 10 bold',bg="#1f242b",fg='white').pack()
    Label(m5, text="Made By Ahmed Barakat", font='san-serif 10 bold',bg="#1f242b",fg='white').pack()
    m3 = Button(m5, text='Github', font='san-serif 16 bold', bg='purple',fg='white', padx=2,command= github).pack()
    Label(m5,bg="#1f242b",fg='white').pack()
    m3 = Button(m5, text='My Website', font='san-serif 16 bold', bg='Black',fg='lightgreen', padx=2,command= web).pack()
menubar = Menu(root, background="#16191f", foreground="white")
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
    label='Downloaded Videos Folder',
    command=videos
)

file_menu.add_command(
    label='Downloaded Audios Folder',
    command=audios
)

file_menu.add_command(
    label='Open Youtube',
    command=openyoutube
)
file_menu.add_command(
    label='About',
    command=about
)

file_menu.add_command(
    label='Exit',
    command=root.destroy
)

# add the File menu to the menubar
menubar.add_cascade(
    label="Menu",
    menu=file_menu
)

root.title('YT Video Downloader (Made by Ahmed Barakat)')

Label(root, text="" ,bg="#1f242b").pack()
Label(root, text="" ,bg="#1f242b").pack()

img = Image.open('Textures\youtube.png')
img = img.resize((75, 70))    
img = ImageTk.PhotoImage(img)
panel = Label(root, image=img ,bg="#1f242b")
panel.image = img
panel.pack(side = "top", expand = "no")

Label(root, text="" ,bg="#1f242b").pack()

Label(root, text="Download Youtube videos", font='san-serif 14 bold' ,bg="#1f242b", foreground="white").pack()
link = StringVar() # Specifying the variable type

Label(root, text="" ,bg="#1f242b").pack()
Label(root, text="" ,bg="#1f242b").pack()

Label(root, text="Paste your link here", font='san-serif 15 bold' ,bg="#1f242b", foreground="white").pack()

Label(root, text="" ,bg="#1f242b").pack()
Label(root, text="" ,bg="#1f242b").pack()

class EntryEx(Entry):
    """
    Extended entry widget that includes a context menu
    with Copy, Cut and Paste commands.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.menu = tkk.Menu(self, tearoff=False)
        self.menu.add_command(label="Copy", command=self.popup_copy)
        self.menu.add_command(label="Cut", command=self.popup_cut)
        self.menu.add_separator()
        self.menu.add_command(label="Paste", command=self.popup_paste)
        self.bind("<Button-3>", self.display_popup)

    def display_popup(self, event):
        self.menu.post(event.x_root, event.y_root)

    def popup_copy(self):
        self.event_generate("<<Copy>>")

    def popup_cut(self):
        self.event_generate("<<Cut>>")

    def popup_paste(self):
        self.event_generate("<<Paste>>")


link_enter = EntryEx(root, width=70, textvariable=link).pack()

Label(root, text="" ,bg="#1f242b").pack()
Label(root, text="First, Choose Reasolution", font='san-serif 12 bold' ,bg="#1f242b", foreground="white").pack()

reschoosen2 = ["144p","240p","360p","480p","720p","1080p","1440p","2160p"]

n = tk.StringVar()
reschoosen = ttk.Combobox(root, width = 27,values=reschoosen2, textvariable = n).pack()

Label(root, text="" ,bg="#1f242b").pack()
Label(root, text="" ,bg="#1f242b").pack()

Button(root, text='Download as a Video', font='san-serif 16 bold', bg='red', padx=2,command= downloadpage).pack()
Label(root, text="" ,bg="#1f242b").pack()
Button(root, text='Download as a Audio', font='san-serif 16 bold', bg='red', padx=2,command= downloadpage1).pack()


root.mainloop()