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
            def getkey():
                content_q = entry_q.get()
                content_p = entry_p.get()
                if len(content_q) == 0 or len(content_p) == 0:
                    a = generate_key_pair(generate_prime_number(), generate_prime_number())
                else:
                    a = generate_key_pair(int(content_q), int(content_p))
                    
                entry_pub.delete(0, len(entry_pub.get()))
                entry_pub.insert(0, a[0][0])
                pub.set(a[0])

                entry_pri.delete(0, len(entry_pri.get()))
                entry_pri.insert(0, a[1][0])
                pri.set(a[1])
            
            def write():
                with open('public_key.pub', 'w') as f:
                    f.write(pub.get())
                with open('private_key.pri', 'w') as f:
                    f.write(pri.get())
                messagebox.showinfo("Success", "Key has been saved!")

            def fillentryp_q():
                p = generate_prime_number()
                q = generate_prime_number()
                while q == p:
                    # make sure q != p
                    q = generate_prime_number()

                entry_p.delete(0, len(entry_p.get()))
                entry_p.insert(0, p)
                entry_q.delete(0, len(entry_q.get()))
                entry_q.insert(0, q)  
        
            roo.geometry("600x400")
            roo.title("Key Generator")
            roo.resizable(0, 0)
            roo.configure(bg = "#FBE6BF")
            pub = StringVar()
            pri = StringVar()

            # Bagian p
            text = Label(roo, text="Nilai p", font=("Arial", 10, "bold"), bg = "#FBE6BF")
            text.place(x=50, y=110)

            entry_p = Entry(roo, font=("Arial", 10, "bold"), bg = "#FFFFFF")
            entry_p.place(x=150, y=110)

            # Bagian q
            text = Label(roo, text="Nilai q", font=("Arial", 10, "bold"), bg = "#FBE6BF")
            text.place(x=50, y=160)

            entry_q = Entry(roo, font=("Arial", 10, "bold"), bg = "#FFFFFF")
            entry_q.place(x=150, y=160, height=20)
            
            # Bagian kunci publik
            text = Label(roo, text="Kunci publik", font=("Arial", 10, "bold"), bg = "#FBE6BF")
            text.place(x=50, y=210)

            entry_pub = Entry(roo, textvariable=pub, font=("Arial", 10, "bold"), bg = "#FFFFFF")
            entry_pub.place(x=150, y=210)

            # Bagian kunci privat
            text = Label(roo, text="Kunci privat", font=("Arial", 10, "bold"), bg = "#FBE6BF")
            text.place(x=50, y=260)

            entry_pri = Entry(roo, textvariable=pri, font=("Arial", 10, "bold"), bg = "#FFFFFF")
            entry_pri.place(x=150, y=260, height=20)

            # Buttons
            button = Button(roo, text="Keluar", font=("Arial", 10, "bold"), bg = "#FBE6BF", command = lambda: roo.destroy())
            button.place(x=500, y=350)
            
            text = Label(roo, text=" Pembangkitan kunci publik dan kunci privat RSA\n", font=("Arial", 12, "bold"), bg = "#FBE6BF")
            text.place(x=40, y=10)

            button = Button(roo, text="Generate p dan q", font=("Arial", 10, "bold"), bg = "#FBE6BF", command = lambda :fillentryp_q())
            button.place(x=325, y=110)

            button = Button(roo, text="Generate Key", font=("Arial", 10, "bold"), bg = "#FBE6BF", command = lambda :getkey())
            button.place(x=325, y=210)

            button = Button(roo, text="Simpan kunci", font=("Arial", 10, "bold"), bg = "#FBE6BF", command = lambda: write())
            button.place(x=325, y=350)


        GUIgetkeypair()