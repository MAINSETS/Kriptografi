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
                content = openTextFile()
                if content is not None:
                    entry_file.delete(0, len(entry_file.get()))
                    entry_file.insert(0, content)
                    file.set(content)
            
            def openfilesign():
                content = openTextFile()
                if content is not None:
                    entry_sign.delete(0, len(entry_sign.get()))
                    entry_sign.insert(0, content)
                    filesign.set(content)

            def selectkey():
                content = openPublicKeyFile()
                if content is not None:
                    entry_key.delete(0, len(entry_key.get()))
                    entry_key.insert(0, content)
                    key.set(content) 

            def verifyPisah():
                real_key =  stringtokey(str(key.get()))
                content = file.get()
                sign = filesign.get()
                if (verifyTextFilePisah(content, real_key, int(sign, base=16))):
                    messagebox.showinfo("Verifikasi", "Tanda tangan valid")
                else:
                    messagebox.showinfo("Verifikasi", "Tanda tangan tidak valid")

            def verifySatu():
                real_key =  stringtokey(str(key.get()))
                content = file.get()
                if('<ds' in content):
                    if (verifyTextFileSatu(content, real_key)):
                        messagebox.showinfo("Verifikasi", "Tanda tangan valid")
                    else:
                        messagebox.showinfo("Verifikasi", "Tanda tangan tidak valid")
                else:
                    messagebox.showerror("Unsigned File", "File belum ditandatangani \n(file yang ditandatangani memiliki '<ds>' di dalam dokumen)")


            roo.geometry("600x400")
            roo.title("Verifiying Text Sign")
            roo.resizable(0, 0)
            roo.configure(bg = "#FBE6BF")

            file = StringVar()
            filesign = StringVar()
            hasil = StringVar()
            key = StringVar()
            
            text = Label(roo, text="Verifikasi tanda-tangan digital file text\n", font=("Arial", 12, "bold"), bg = "#FBE6BF")
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

            button = Button(roo, text="Verifikasi Sign Terpisah", font=("Arial", 10), command = lambda: verifyPisah())
            button.place(x=200, y=150)

            button = Button(roo, text="Verifikasi Sign Tak Terpisah", font=("Arial", 10), command = lambda: verifySatu())
            button.place(x=400, y=150)

            label_key = Label(roo, text="*taruh file yang sudah ditandatangani pada entry paling atas jika ingin verifikasi sign tak terpisah", font=("Arial", 9), bg = "#FBE6BF")
            label_key.place(x=10, y=350)

            label_key = Label(roo, text="tidak perlu mengisi entry ke-dua", font=("Arial", 9), bg = "#FBE6BF")
            label_key.place(x=10, y=370)

            button = Button(roo, text="Keluar", font=("Arial", 10, "bold"), command = lambda: roo.destroy())
            button.place(x=500, y=200)

        GUITextVerify()