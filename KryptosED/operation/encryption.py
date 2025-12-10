from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from tkinter import filedialog, ttk
import tkinter.messagebox
from pathlib import Path
import os
import tkinter as tk

#AES-256 method
def encryption(file, layoutfilename, encryptbutton, progressbar=None):
    try:
        #Progressbar
        if progressbar is None:
            progress_window = tk.Toplevel()
            progress_window.title("Encryption Progress")
            progress_window.geometry("600x200")

            progress_label = tk.Label(progress_window, text="Encrypting file...")
            progress_label.pack(pady=10)

            progressbar= ttk.Progressbar(progress_window, length=250, mode='determinate')
            progressbar.pack(pady=10)

            progress_window.update()
        #Gen the key
        key = get_random_bytes(32)
        nonce = get_random_bytes(8)
        cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)

        filesize = os.path.getsize(str(file))
        processed = 0
        chunk_size = 64 * 1024  # 64 KB

        #Encrypted output file:
        encrypted_file = str(file) + ".enc"

        with open(str(file), 'rb') as fin, open(encrypted_file, 'wb') as fout:
            fout.write(nonce)  # Save the nonce to first KB
            while True:
                chunk = fin.read(chunk_size)
                if not chunk:
                    break
                encrypted_chunk = cipher.encrypt(chunk)
                fout.write(encrypted_chunk)
                processed += len(chunk)
                
                #Update process bar
                progress_value = (processed / filesize) * 100
                progressbar['value'] = progress_value
                if hasattr(progressbar, 'master'):
                    progressbar.master.update_idletasks()
                else:
                    progressbar.update_idletasks()
                    
        # Save the key
        tkinter.messagebox.showwarning("Info Message", "Please select a folder to save the key.")
        folder = filedialog.askdirectory()
        fileName = Path(str(file)).stem
        key_path = os.path.join(folder, f"{fileName}.key.bin")
        with open(key_path, 'wb') as fkey:
            fkey.write(key)
        tkinter.messagebox.showinfo("Info Message", "File Encrypted Correctly")
        tkinter.messagebox.showinfo("Info message", f"The key has succesfully exported as '{fileName}.key.bin'")
    except Exception as e:
        tkinter.messagebox.showerror("Error Message", f"Sorry, an error happened: {e}")
    finally:
        if 'progress_window' in locals():
            progress_window.destroy()
    layoutfilename.destroy()
    encryptbutton.destroy()