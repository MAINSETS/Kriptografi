import tkinter as tk
from tkinter import *
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import filedialog
from RSA import *
from SHA_3 import *
from utility import *

class GUITextVerifying(tk.Tk):
    def __init__(roo):
        super().__init__()

        def GUITextVerify():
            def openfile():
                filename = filedialog.askopenfile(mode='rb', filetypes=[('All files', '*')])
                if filename is not None:
                    content = filename.read()
                    entry_file.delete(0, len(entry_file.get()))
                    entry_file.insert(0, content)
                    file.set(content)
            
            def openfilesign():
                filename = filedialog.askopenfile(mode='rb', filetypes=[('All files', '*')])
                if filename is not None:
                    content = filename.read()
                    entry_sign.delete(0, len(entry_sign.get()))
                    entry_sign.insert(0, content)
                    filesign.set(content)

            def selectkey():
                filename = filedialog.askopenfile(mode='rb', filetypes=[('All files', '*')])
                if filename is not None:
                    content = filename.read()
                    entry_key.delete(0, len(entry_key.get()))
                    entry_key.insert(0, content)
                    key.set(content) 

            def verify():
                real_key =  stringtokey(str(key.get()))
                content = file.get().split("'")[1]
                sign = filesign.get().split("'")[1]
                if (verifyTextFilePisah(content, real_key, int(sign, base=16))):
                    messagebox.showinfo("Verifikasi", "Tanda tangan valid")
                else:
                    messagebox.showinfo("Verifikasi", "Tanda tangan tidak valid")


            roo.geometry("600x400")
            roo.title("Verifiying Sign")
            roo.resizable(0, 0)
            roo.configure(bg = "#FBE6BF")

            file = StringVar()
            filesign = StringVar()
            hasil = StringVar()
            key = StringVar()
            
            text = Label(roo, text="Verifikasi tanda-tangan digital\n", font=("Arial", 12, "bold"), bg = "#FBE6BF")
            text.place(x=40, y=10)

            text = Label(roo, text="File Awal", font=("Arial", 12), bg = "#FBE6BF")
            text.place(x=40, y=50)

            entry_file = Entry(roo, textvariable=file, width=40)
            entry_file.place(x=200, y=50)

            button = Button(roo, text="Browse", font=("Arial", 10), command = openfile)
            button.place(x=500, y=50)

            text = Label(roo, text="File Signature", font=("Arial", 12), bg = "#FBE6BF")
            text.place(x=40, y=80)

            entry_sign = Entry(roo, textvariable=filesign, width=40)
            entry_sign.place(x=200, y=80)

            button = Button(roo, text="Browse", font=("Arial", 10), command = openfilesign)
            button.place(x=500, y=80)

            label_key = Label(roo, text="Public Key", font=("Arial", 12), bg = "#FBE6BF")
            label_key.place(x=40, y=110)

            entry_key = Entry(roo, textvariable=key, width=40)
            entry_key.place(x=200, y=110)

            button_key = Button(roo, text="Browse", font=("Arial", 10), command=selectkey)
            button_key.place(x=500, y=110)

            label_hasil = Label(roo, text="Hasil Verifikasi", font=("Arial", 12), bg = "#FBE6BF")
            label_hasil.place(x=40, y=150)

            button = Button(roo, text="Verifikasi", font=("Arial", 10), command = lambda: verify())
            button.place(x=500, y=150)

        GUITextVerify()