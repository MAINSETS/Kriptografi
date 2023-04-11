import tkinter as tk
from tkinter import *
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from RSA import *

import GUIKeyGenerator as GUIKey
import GUISigning as GUISign
import GUIVerifying as GUIVerify

class Main(tk.Tk):
    def __init__(root):
        super().__init__()
        
        #canvas
        root.geometry("1000x600")
        root.title("Program Tanda-tangan Digital")
        root.configure(bg = "#FBE6BF")

        canvas = Canvas(
            root,
            bg = "#FBE6BF",
            height = 600,
            width = 900,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        canvas.place(x = 0, y = 0)
        canvas.create_text(
            250,
            30,
            anchor="nw",
            text="Program Tanda-tangan Digital",
            fill="#000000",
            font=("OpenSansRoman Bold", 40 * -1)
        )

        canvas.create_text(
            450,
            100,
            anchor="nw",
            text="Digital Signature",
            fill="#000000",
            font=("OpenSansRoman Regular", 20 * -1)
        )

        #button
        button_image_1 = PhotoImage(
            file = "Tugas 3/img/Key.png")
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=GUIKey.GUIKeyGenerator,
            bg = "#FBE6BF",
            relief="flat"
        )
        button_1.place(
            x=25.0,
            y=150.0,
            width=125,
            height=55
        )
        button_image_2 = PhotoImage(
            file = "Tugas 3/img/Sign.png")
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=GUISign.GUISigning,
            bg = "#FBE6BF",
            relief="flat"
        )
        button_2.place(
            x=25,
            y=250,
            width=125,
            height=55
        )
        button_image_3 = PhotoImage(
            file = "Tugas 3/img/Verify.png")
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=GUIVerify.GUIVerifying,
            bg = "#FBE6BF",
            relief="flat"
        )
        button_3.place(
            x=25,
            y=350,
            width=125,
            height=55
        )
        button_image_4 = PhotoImage(
            file = "Tugas 3/img/Exit.png")
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: root.destroy(),
            bg = "#FBE6BF",
            relief="flat"
        )
        button_4.place(
            x=25,
            y=450,
            width=125,
            height=55
        )
                
        #entry
        entry_ptext = Text(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=1
        )
        
        entry_ptext.place(
            x=200.0,
            y=150.0,
            width=700.0,
            height=350.0
        )
        
        root.resizable(False, False)
        root.mainloop()
        
if __name__ == "__main__":
    app = Main()
    Main.mainloop()