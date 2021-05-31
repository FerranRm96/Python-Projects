# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 23:38:57 2021

@author: Ferran
"""
import os
from google_images_download import google_images_download
from tkinter import *
import tkinter.messagebox
import shutil
import ctypes

response = google_images_download.googleimagesdownload()

SPI_SETDESKTOPWALLPAPER=20

root = Tk(className="frm - Desktop Wallpaper Changer")
root.geometry("375x100")
entry = Entry(root)
entry.pack(fill=BOTH, expand=1)

def on_close():
     close = tkinter.messagebox.askokcancel("Close", "Would you like to close the program?")
     if close:
         root.destroy()
         script_dir = os.path.dirname(__file__) 
         rel_path = "downloads"
         folder_delete = os.path.join(script_dir, rel_path)
         if(os.path.exists(folder_delete)):
            shutil.rmtree(folder_delete)



def select_Picture():    
    value = entry.get()
    if(value != ""):
        absolute_image_paths = response.download({"keywords":value,"limit":1})
        for filename in os.listdir("downloads/"+str(value)):
            picture = filename
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "downloads/"+str(value)+"/"+str(picture)
        abs_file_path = os.path.join(script_dir, rel_path)
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKTOPWALLPAPER, 0,abs_file_path, 3)
    else:
        print("Type Something")

        
root.protocol("WM_DELETE_WINDOW",  on_close)
button_app = Button(root, text="Change Background", command=select_Picture)
button_app.pack(side=BOTTOM, expand=1, fill=BOTH)


root.mainloop()
