import tkinter as tk
from tkinter import *
from pathlib import Path
import tkinter.messagebox as messagebox
from tkinter import filedialog
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from RSA import *
from SHA_3 import *
from utility import *

#membuat GUI dari frame, label, dan tombol
class GUITextSigning(tk.Tk):
    def __init__(roo):
        super().__init__()
        def GUITextSign():
            def selecttextfile():
                filename = filedialog.askopenfile(mode='r', filetypes=[('Text files', 'txt')])
                if filename is not None:
                    content = filename.read()
                    entry_file.delete(0, len(entry_file.get()))
                    entry_file.insert(0, content)
                    file.set(content)

            def selectkey():
                content = openPrivateKeyFile()
                if content is not None:
                    entry_key.delete(0, len(entry_key.get()))
                    entry_key.insert(0, content)
                    key.set(content)
            
            def hash():
                if(file.get() == ""):
                    messagebox.showerror("Error", "File is empty")
                else:
                    a = file.get()
                    e = a.encode('latin-1')
                    b = sha3_256(e)
                    entry_hash.delete(0, len(entry_hash.get()))
                    entry_hash.insert(0, b)
                    hasil.set(b)

            def sign():
                if(key.get() == ""):
                    messagebox.showerror("Error", "Key is empty")
                else:
                    stringkey = str(key.get())
                    real_key = stringtokey(stringkey)
                    b = encrypt(real_key, int(hasil.get(), base=16))
                    c = hex(b)[2:]
                    entry_sign.delete(0, len(entry_sign.get()))
                    entry_sign.insert(0, c)
                    signage.set(c)
            
            
            roo.geometry("600x400")
            roo.title("Digital Sign Text File")
            roo.resizable(0, 0)
            roo.configure(bg = "#FBE6BF")
            text = Label(roo, text="Pembangkitan tanda-tangan digital file text\n", font=("Arial", 12, "bold"), bg = "#FBE6BF")
            text.place(x=40, y=10)

            # variabel
            file = StringVar()
            key = StringVar()
            hasil = StringVar()
            signage = StringVar()

            label_file = Label(roo, text="File", font=("Arial", 12), bg = "#FBE6BF")
            label_file.place(x=40, y=50)

            entry_file = Entry(roo, textvariable=file, width=40)
            entry_file.place(x=200, y=50)

            button_file = Button(roo, text="Browse Text File", command=selecttextfile)
            button_file.place(x=500, y=50)

            label_key = Label(roo, text="Private Key", font=("Arial", 12), bg = "#FBE6BF")
            label_key.place(x=40, y=80)

            entry_key = Entry(roo, textvariable=key, width=40)
            entry_key.place(x=200, y=80)

            button_key = Button(roo, text="Browse", command=selectkey)
            button_key.place(x=500, y=80)

            label_hash = Label(roo, text="Hash", font=("Arial", 12), bg = "#FBE6BF")
            label_hash.place(x=40, y=110)

            entry_hash = Entry(roo, textvariable=hasil, width=40)
            entry_hash.place(x=200, y=110)

            button_hash = Button(roo, text="Hash", command=hash)
            button_hash.place(x=500, y=110)

            label_sign = Label(roo, text="Signature", font=("Arial", 12), bg = "#FBE6BF")
            label_sign.place(x=40, y=140)

            entry_sign = Entry(roo, textvariable=signage, width=40)
            entry_sign.place(x=200, y=140)

            button_sign = Button(roo, text="Sign", command=sign)
            button_sign.place(x=500, y=140)

            button_save_sep = Button(roo, text="Save Sign Seperately", command=lambda: saveSeperateSignFile(signage.get()))
            button_save_sep.place(x=450, y=300)

            button_save_com = Button(roo, text="Save Sign with Content", command=lambda: saveCombineSignTextFile(file.get(), signage.get()))
            button_save_com.place(x=250, y=300)

            button = Button(roo, text="Keluar", font=("Arial", 10, "bold"), command = lambda: roo.destroy())
            button.place(x=500, y=200)

        GUITextSign()
