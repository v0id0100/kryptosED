import zipfile
from tkinter import filedialog
import tkinter.messagebox
import os

def compress(files, dir_button):
    #Check if there is one file and reccomend if it is.
    if len(files) < 2:
        tkinter.messagebox.showwarning("Info Message", "It's recommended to cipher direcly if you have selected only one file.")
    tkinter.messagebox.showwarning("Info Message", "Please select a folder to save the compressed file.")
    #Choose the destination folder.
    dest_folder = filedialog.askdirectory()
    #Compress all the files.
    with zipfile.ZipFile(f"{dest_folder}/compressed.zip", mode='w', compression=zipfile.ZIP_DEFLATED) as f:
        for file in files:
            try:
                filename = os.path.basename(file)
                f.write(file, arcname=filename)
                os.remove(file)
            except Exception as e:
                print(f"Error: {e}")
    tkinter.messagebox.showinfo("Info Message", "Files Compressed successfully")
    #Restart the layout.
    dir_button.destroy()