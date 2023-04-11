import tkinter as tk
from tkinter import *
from tkinter import messagebox
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from RSA import *
#membuat GUI dari frame, label, dan tombol
class GUIKeyGenerator(tk.Tk):
    def __init__(roo):
        super().__init__()     
        def GUIgetkeypair():   
            
            def getpublickey():
                a = generate_key_pair(generate_prime_number(), generate_prime_number())
                pub.set(a[0][0])

            def getprivatekey():
                b = generate_key_pair(generate_prime_number(), generate_prime_number())
                pri.set(b[0][0])
            
            def write():
                with open('public_key.pub', 'w') as f:
                    f.write(pub.get())
                with open('private_key.pri', 'w') as f:
                    f.write(pri.get())
                messagebox.showinfo("Success", "Key has been saved!")

            roo.geometry("600x400")
            roo.title("Key Generator")
            roo.resizable(0, 0)
            roo.configure(bg = "#FBE6BF")
            pub = StringVar()
            pri = StringVar()

            button = Button(roo, text="Keluar", font=("Arial", 10, "bold"), bg = "#FBE6BF", command = lambda: roo.destroy())
            button.place(x=500, y=350)
            
            text = Label(roo, text=" Pembangkitan kunci publik dan kunci privat RSA\n", font=("Arial", 12, "bold"), bg = "#FBE6BF")
            text.place(x=40, y=10)

            button = Button(roo, text="Buat kunci", font=("Arial", 10, "bold"), bg = "#FBE6BF", command = [getpublickey(), getprivatekey()])
            button.place(x=200, y=200)

            button = Button(roo, text="Simpan kunci", font=("Arial", 10, "bold"), bg = "#FBE6BF", command = lambda: write())
            button.place(x=200, y=250)

            text = Label(roo, text="Kunci publik", font=("Arial", 10, "bold"), bg = "#FBE6BF")
            text.place(x=50, y=300)

            entry = Entry(roo, textvariable=pub, font=("Arial", 10, "bold"), bg = "#FBE6BF")
            entry.place(x=150, y=300)

            text = Label(roo, text="Kunci privat", font=("Arial", 10, "bold"), bg = "#FBE6BF")
            text.place(x=50, y=350)

            entry = Entry(roo, textvariable=pri, font=("Arial", 10, "bold"), bg = "#FBE6BF")
            entry.place(x=150, y=350)

        GUIgetkeypair()