import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
from pathlib import Path
from KryptosED.operation import *
import os
import customtkinter
import sys
from PIL import Image, ImageTk


#Find the relative path for pyinstaller
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def app():
    global root, tk_image
    #Set up the styles:
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    #Font styles
    title_letter = "System"
    font_letter = "System"

    #Main Windows
    root = customtkinter.CTk(fg_color="darkseagreen")

    #Windows size and location
    root.title("KryptosED")
    root.minsize(900,700)
    root.geometry("900x700")
    root.resizable(True, True)

    # Configure grid to make responsive window
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    #Welcome
    welcome_label = customtkinter.CTkLabel(root, text="Welcome To KryptosED", font=(title_letter, 40), text_color="black")
    welcome_label.grid(row=0, column=0, pady=20, sticky="ew")

    #Icon
    icon_path = resource_path('KryptosED/utils/images/icon.png')
    image = Image.open(icon_path)
    resized_image = image.resize((500, 500))
    tk_image = ImageTk.PhotoImage(resized_image)
    icon_label = customtkinter.CTkLabel(root, image=tk_image, text="")
    icon_label.grid(row=1, column=0, sticky="nsew")

    #Layout inferior
    bottom_label = customtkinter.CTkLabel(root, text="Encrypt and Decrypt your files with KryptosED®️\t@v0id0100", font=customtkinter.CTkFont(family=font_letter, size=20), bg_color="cornflower blue")
    bottom_label.grid(row=4, column=0, ipady=5, sticky="ew")

    #Layout frame
    layoutframe = customtkinter.CTkFrame(root, fg_color="lightcyan4")
    layoutframe.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
    #Buttons Grid:
    layoutframe.grid_columnconfigure(0, weight=1)
    layoutframe.grid_columnconfigure(1, weight=1)
    layoutframe.grid_columnconfigure(2, weight=2)
    layoutframe.grid_columnconfigure(3, weight=1)
    layoutframe.grid_columnconfigure(4, weight=1)
    layoutframe.grid_rowconfigure(0, weight=1)
    layoutframe.grid_rowconfigure(1, weight=1)
    layoutframe.grid_rowconfigure(2, weight=1)
    layoutframe.grid_rowconfigure(3, weight=1)
    layoutframe.grid_rowconfigure(4, weight=1)

    #File class
    class File:
        def __init__(self):
            self.filepath = None
        def getFileEncrypt(self):
            self.filepath = Path(filedialog.askopenfilename())
            self.filename = self.filepath.name
            if len(self.filename) > 11:
                self.filename = f'{self.filename[:21]}...'
            else:
                None
            layoutfilename = customtkinter.CTkLabel(layoutframe, text=self.filename)
            layoutfilename.grid(column=2, row=0, sticky="ew", padx=5, pady=5)
            encryptbutton = customtkinter.CTkButton(layoutframe, text="Encrypt File", height=40, fg_color="chartreuse2", hover=False, text_color="black", command=lambda: encryption(self.filepath, layoutfilename, encryptbutton))
            encryptbutton.grid(column=3, row=0, padx=5, pady=5, sticky="ew")
            check_to_destroy(self.filename, layoutfilename, encryptbutton)
        def getFileDecrypt(self):
            global layoutfilename2
            self.filepath = Path(filedialog.askopenfilename())
            self.filename = self.filepath.name
            if len(self.filename) > 11:
                self.filename = f'{self.filename[:21]}...'
            else:
                None
            layoutfilename2 = customtkinter.CTkLabel(layoutframe, text=self.filename)
            layoutfilename2.grid(column=2, row=1, sticky="ew", padx=5, pady=5)
            file2.getKey()
        #Import Key File
        def getKey(self):
            global button
            key = Key()
            button = customtkinter.CTkButton(layoutframe, text="Select local Key", command=key.getKeyFile)
            button.grid(column=3, row=1, padx=5, pady=5, sticky="ew")
            check_to_destroy(file2.filename, layoutfilename2, button)

    #Key class
    class Key:
        def __init__(self):
            self.keypath = None
        def getKeyFile(self):
            def decrypt(file, key):
                decrypt = customtkinter.CTkButton(layoutframe, text="Decrypt file", height=40, hover=False, text_color="black", font=customtkinter.CTkFont(family=font_letter, size=10), fg_color="red", command=lambda: decryption(file, key, layoutfilename2, layoutkey, decrypt, button))
                decrypt.grid(column=4, row=2, sticky="ew", padx=5, pady=5)
                check_to_destroy(keyname, layoutkey, decrypt)
            self.keypath = Path(filedialog.askopenfilename(filetypes=[("Public Key File", "*.bin")]))
            keyname = self.keypath.name
            if len(keyname) > 10:
                keyname = f'{keyname[:11]}.pem'
            else:
                None
            layoutkey = customtkinter.CTkLabel(layoutframe, text=keyname)
            layoutkey.grid(column=4, row=1, sticky="ew", padx=5, pady=5)
            decrypt(file2.filepath, self.keypath)

    #Directory class:
    class Directory():
        def __init__(self):
            global button
            self.files = []
            layout = customtkinter.CTkLabel(layoutframe, text="Do you want to cipher two or more files?\n Compress here and then cipher it!", font=customtkinter.CTkFont(family=font_letter, size=10))
            layout.grid(row=3, column=0, columnspan=2, sticky="ew")
            button = customtkinter.CTkButton(layoutframe, text="Select Files", fg_color="red", text_color="black", hover=False, command=self.select_files)
            button.grid(row=4, column=0, sticky="ew")
        def select_files(self):
           files = filedialog.askopenfilenames()
           for file in files:
              self.files.append(file)
           print(self.files)
           dir_button = customtkinter.CTkButton(layoutframe, text="Compress!!!", hover=False, fg_color="chartreuse2", text_color="black", command=lambda: compress(self.files, dir_button))
           dir_button.grid(row=4, column=1, sticky="ew")
           check_to_destroy(files, dir_button)

    #Layout Encrypt:
    importtext = customtkinter.CTkLabel(layoutframe, text="Select a file to ENCRYPT: ", font=customtkinter.CTkFont(family=font_letter, size=20))
    importtext.grid(column=0, row=0, sticky="ew", padx=15, pady=5)

    file = File()
    button_encrypt = customtkinter.CTkButton(layoutframe, text="Open file", height=40, command=file.getFileEncrypt)
    button_encrypt.grid(column=1, row=0, sticky="ew", padx=5, pady=5)

    #Layout Decrypt:
    importtext2 = customtkinter.CTkLabel(layoutframe, text="Select a file to DECRYPT: ", font=customtkinter.CTkFont(family=font_letter, size=20))
    importtext2.grid(column=0, row=1, sticky="ew", padx=15, pady=5)

    #Layout to compress files
    Directory()

    file2 = File()
    button_decrypt = customtkinter.CTkButton(layoutframe, text="Open file", height=40, command=file2.getFileDecrypt)
    button_decrypt.grid(column=1, row=1, sticky="ew", padx=5, pady=5)

    #Destroy layout in case the are not attributes:
    def check_to_destroy(attribute, element_to_destroy_1, element_to_destroy_2=None):
        if len(attribute) > 0:
            None
        else:
            element_to_destroy_1.destroy()
            element_to_destroy_2.destroy()

#Check running the main file
if __name__ == "__main__":
    #Ask exit
    def exit():
        response=tkinter.messagebox.askyesno('Exit','Are you sure you want to exit?')
        if response:
            root.destroy()
    app()
    root.protocol('WM_DELETE_WINDOW', exit)
    #Mantain the loop:
    root.mainloop()