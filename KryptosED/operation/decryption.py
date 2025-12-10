from Crypto.Cipher import AES
from tkinter import filedialog, ttk
import tkinter as tk
import tkinter.messagebox
from pathlib import Path
import os

def decryption(file, key, layoutfilename2, layoutkey, decrypt, button, progressbar=None):
    try:
        #Progressbar
        if progressbar is None:
            progress_window = tk.Toplevel()
            progress_window.title("Decryption Progress")
            progress_window.geometry("600x200")
            
            progress_label = tk.Label(progress_window, text="Decrypting file...")
            progress_label.pack(pady=10)
            
            progressbar = ttk.Progressbar(progress_window, length=250, mode='determinate')
            progressbar.pack(pady=10)
            
            progress_window.update()
        #Read the key
        with open(key, 'rb') as fkey:
            readkey = fkey.read()
        #Read the nonce; First 64KB
        with open(file, 'rb') as fin:
            nonce = fin.read(8)
            cipher = AES.new(readkey, AES.MODE_CTR, nonce=nonce)
            filesize = os.path.getsize(file) - 8
            processed = 0
            chunk_size = 64 * 1024  # 64 KB

            file_path = Path(file)
            if file_path.suffix == '.enc':
                output_file = str(file_path.with_suffix(''))
            else:
                output_file = str(file) + ".decrypted"

            #Decipher per blocks
            with open(output_file, 'wb') as fout:
                while True:
                    chunk = fin.read(chunk_size)
                    if not chunk:
                        break
                    decrypted_chunk = cipher.decrypt(chunk)
                    fout.write(decrypted_chunk)
                    processed += len(chunk)

                    #Update progressbar
                    progress_value = (processed / filesize) * 100
                    progressbar['value'] = progress_value
                    if hasattr(progressbar, 'master'):
                        progressbar.master.update_idletasks()
                    else:
                        progressbar.update_idletasks()

        tkinter.messagebox.showinfo("Info Message", "The file was decrypted successfully")
    except Exception as e:
        tkinter.messagebox.showerror("Error Message", f"An error happened: {e}")

    finally:
        if 'progress_window' in locals():
            progress_window.destroy()
    anw = tkinter.messagebox.askquestion("Info Message", "Do you want to erase the key file?")
    if anw == 'yes':
        os.remove(key)
        tkinter.messagebox.showinfo("Info Message", f"'{key}' was successfully removed")
    else:
        tkinter.messagebox.showinfo("Info Message", f"'{key}' was not removed")
    # Restart the layout
    layoutfilename2.destroy()
    layoutkey.destroy()
    decrypt.destroy()
    button.destroy()