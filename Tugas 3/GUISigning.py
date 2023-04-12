import tkinter as tk
from tkinter import *
from pathlib import Path
import tkinter.messagebox as messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from RSA import *
from SHA_3 import *

#membuat GUI dari frame, label, dan tombol
class GUISigning(tk.Tk):
    def __init__(roo):
        super().__init__()

        def GUISign():
            def readkey():
                with open('public_key.pub', 'r') as f:
                    pub = f.read()          
                with open('private_key.pri', 'r') as f:
                    pri = f.read()
                messagebox.showinfo("Success", "Key has been read!")
            
            def readfile():
                with open('file.txt', 'r') as f:
                    file = f.read()
                messagebox.showinfo("Success", "File has been opened!")
            
            def readbinary():
                with open('file.*', 'rb') as f:
                    file = f.read()
                    files = file.decode('latin-1')
                messagebox.showinfo("Success", "File has been opened!")
    
                
            roo.geometry("600x400")
            roo.title("Digital Sign")
            roo.resizable(0, 0)
            roo.configure(bg = "#FBE6BF")
            text = Label(roo, text="Pembangkitan tanda-tangan digital\n", font=("Arial", 12, "bold"), bg = "#FBE6BF")
            text.place(x=40, y=10)
        GUISign()
