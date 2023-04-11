import tkinter as tk
from tkinter import *
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

#membuat GUI dari frame, label, dan tombol
class GUIVerifying(tk.Tk):
    def __init__(roo):
        super().__init__()

        def GUIVerify():
            roo.geometry("600x400")
            roo.title("Verifiying Sign")
            roo.resizable(0, 0)
            roo.configure(bg = "#FBE6BF")
            
            text = Label(roo, text="Verifikasi tanda-tangan digital\n", font=("Arial", 12, "bold"), bg = "#FBE6BF")
            text.place(x=40, y=10)
        GUIVerify()
