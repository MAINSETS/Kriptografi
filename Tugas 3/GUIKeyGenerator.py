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
            button = Button(roo, text="Buat kunci", font=("Arial", 10, "bold"), bg = "#FBE6BF")
            button.place(x=200, y=200)
            button.bind("<Button-1>", generate_prime_number())
            
            text = Label(roo, text="Kunci publik: ", font=("Arial", 10, "bold"), bg = "#FBE6BF")
            text.place(x=40, y=300)
            text = Label(roo, text="Kunci privat: ", font=("Arial", 10, "bold"), bg = "#FBE6BF")
            text.place(x=40, y=350)

        GUIgetkeypair()