import tkinter as tk
from tkinter import *
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import filedialog
from RSA import *
from SHA_3 import *
from utility import *

import GUITextSigning as GUITextSign
import GUIBinSigning as GUIBinSign

#membuat GUI dari frame, label, dan tombol
class GUISigning(tk.Tk):
    def __init__(roo):
        super().__init__()
        def GUISigning():
            
            def close():
                roo.destroy()
                
            roo.geometry("300x150")
            roo.title("Digital Sign")
            roo.resizable(0, 0)
            roo.configure(bg = "#FBE6BF")
            
            text = Label(roo, text="Pembangkitan tanda-tangan digital\n", font=("Arial", 12, "bold"), bg = "#FBE6BF")
            text.place(x=10, y=10)
            
            text = Label(roo, text="Pilihlah opsi tanda-tangan: \n", font=("Arial", 9), bg = "#FBE6BF")
            text.place(x=10, y=70)
            
            button_1= Button(roo, text="Text File Signing", command=lambda: [GUITextSign.GUITextSigning(), close()], bg= '#FBB43C')
            button_1.place(x=11, y=100)

            button_2 = Button(roo, text="Binary File Signing", command=lambda: [GUIBinSign.GUIBinSigning(), close()], bg= '#FBB43C')
            button_2.place(x=170, y=100)
        
        GUISigning()