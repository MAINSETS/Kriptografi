import tkinter as tk
from tkinter import *
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from RSA import *

import GUIKeyGenerator as GUIKey
import GUIVerifying as GUIVerify
import GUISigning as GUISign

class Main(tk.Tk):
    def __init__(root):
        super().__init__()
        
        #canvas
        root.geometry("790x400")
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
            120,
            30,
            anchor="nw",
            text="Program Tanda-tangan Digital",
            fill="#000000",
            font=("OpenSansRoman Bold", 40 * -1)
        )

        canvas.create_text(
            320,
            100,
            anchor="nw",
            text="Digital Signature",
            fill="#000000",
            font=("OpenSansRoman Regular", 20 * -1)
        )
        
        canvas.create_text(
            120,
            370,
            anchor="nw",
            text="dibuat oleh 18220031 Muhammad Raihan Aulia, 18220052 Christopher Jie, 18220066 Michel Vito Adinugroho",
            fill="#000000",
            font=("OpenSansRoman Regular", 12 * -1)
        )

        #button
        button_image_1 = PhotoImage(
            file = "img/Key.png")
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
            y=250.0,
            width=125,
            height=55
        )
        button_image_2 = PhotoImage(
            file = "img/Sign.png")
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=GUISign.GUISigning,
            bg = "#FBE6BF",
            relief="flat"
        )
        button_2.place(
            x=225,
            y=250,
            width=125,
            height=55
        )
        button_image_3 = PhotoImage(
            file = "img/Verify.png")
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=GUIVerify.GUIVerifying,
            bg = "#FBE6BF",
            relief="flat"
        )
        button_3.place(
            x=425,
            y=250,
            width=125,
            height=55
        )
        button_image_4 = PhotoImage(
            file = "img/Exit.png")
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: root.destroy(),
            bg = "#FBE6BF",
            relief="flat"
        )
        button_4.place(
            x=625,
            y=250,
            width=125,
            height=55
        )
                
        
        
        root.resizable(False, False)
        root.mainloop()
        
if __name__ == "__main__":
    Main()
    