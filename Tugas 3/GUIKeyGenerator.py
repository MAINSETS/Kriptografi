import tkinter as tk
from tkinter import *
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from RSA import *
#membuat GUI dari frame, label, dan tombol
class GUIKeyGenerator(tk.Tk):
    def __init__(roo):
        super().__init__()

        def GUIKey():
            roo.geometry("600x400")
            roo.title("Key Generator")
            roo.resizable(0, 0)
            roo.configure(bg = "#FBE6BF")
            
            text = Label(roo, text=" Pembangkitan kunci publik dan kunci privat RSA\n", font=("Arial", 12, "bold"), bg = "#FBE6BF")
            text.place(x=40, y=10)
        GUIKey()

        def GUIgetkeypair():   
            public_key = IntVar()
            private_key = IntVar()

            button = Button(roo, text="Buat kunci", font=("Arial", 10, "bold"), bg = "#FBE6BF", command = lambda: [public_key.set(getpublickey()), private_key.set(getprivatekey())])
            button.place(x=200, y=200)

            button = Button(roo, text="Simpan", font=("Arial", 10, "bold"), bg = "#FBE6BF", command = lambda: [write()])
            button.place(x=200, y=250)
            
            text = Label(roo, text="Kunci publik: ", font=("Arial", 10, "bold"), bg = "#FBE6BF")
            text.place(x=40, y=300)

            entry = Entry(roo, textvariable=public_key, font=("Arial", 10, "bold"), bg = "#FBE6BF")
            entry.place(x=150, y=300)

            text = Label(roo, text="Kunci privat: ", font=("Arial", 10, "bold"), bg = "#FBE6BF")
            text.place(x=40, y=350)

            entry = Entry(roo, textvariable=private_key, font=("Arial", 10, "bold"), bg = "#FBE6BF")
            entry.place(x=150, y=350)
        GUIgetkeypair()

