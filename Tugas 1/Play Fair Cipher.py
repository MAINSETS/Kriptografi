from pydoc import plain
import numpy as np
import random as rd
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def remove(string):
    return string.replace(" ","")

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']


def genkey(text):
    key=[]
    for i in text:
        if i not in key:
            key.append(i)

    for i in alphabets:
        if i not in key:
            key.append(i)
    return key

def genmatrix(key):
    matrix=[[]]
    # print(key)
    i=0
    while(i<5):
        m=[]
        for j in key[i*5:(i+1)*5]:
            m.append(j)
        matrix.append(m)
        i+=1
    # print(matrix)
    return matrix
    

def createplain(text):
    plaintext=[]
    i=0
    if(len(text)%2!=0):
        text+=rd.choice(alphabets)
    while(i<(len(text))):
        plaintext.append(text[i:i+2])
        i+=2
    return plaintext

def dipslaymatrix(matrix):
    for i in range(1,6):
        print(matrix[i])
        '\n'

def checkmat(start,matrix):
    for i,x in enumerate(matrix):
        if start in x:
            return i,x.index(start)+1

def changeplain(row,col,matrix):
    return matrix[row][col-1]

def encryption():
    msg=entry.get()
    text=keyy.get()
    key=genkey(text)
    matrix=genmatrix(key)
    plain=createplain(msg)
    start=[]
    cipher=[]
    end=[]
    for i in plain:
        start.append(i[0])
        end.append(i[1])
    print("plaintext:")
    dipslaymatrix(matrix)
    print(start,end)
    for i in range(int(len(plain))):
        r1,c1=checkmat(start[i],matrix)
        r2,c2=checkmat(end[i],matrix)
        if r1==r2:
            if c1==5 :
                cipher.append(changeplain(r1,c1-4,matrix))
                cipher.append(changeplain(r2,c2+1,matrix))
            elif c2==5:
                cipher.append(changeplain(r1,c1+1,matrix))
                cipher.append(changeplain(r2,c2-4,matrix))
            else:
                cipher.append(changeplain(r1,c1+1,matrix))
                cipher.append(changeplain(r2,c2+1,matrix))
        elif c1==c2:
            if r1==5 :
                cipher.append(changeplain(r1-4,c1,matrix))
                cipher.append(changeplain(r2+1,c2,matrix))
            elif r2==5:
                cipher.append(changeplain(r1+1,c1,matrix))
                cipher.append(changeplain(r2-4,c2,matrix))
            else:
                cipher.append(changeplain(r1+1,c1,matrix))
                cipher.append(changeplain(r2+1,c2,matrix))
        else:
            cipher.append(changeplain(r1,c2,matrix))
            cipher.append(changeplain(r2,c1,matrix))
    label=Label(frame,text="Encryption:" ,padx=5,pady=5)
    label.grid(row=3,column=0)
    label=Label(frame,text=cipher ,padx=5,pady=5)
    label.grid(row=3,column=1)
    return cipher

def change(row,col,matrix):
    return matrix[row][col-1]

def decryption():
    msg=encryption()
    text=keyy.get()
    key=genkey(text)
    matrix=genmatrix(key)
    plain=createplain(msg)
    start=[]
    cipher=[]
    end=[]
    for i in plain:
        start.append(i[0])
        end.append(i[1])
    print("ciphertext:")
    dipslaymatrix(matrix)
    print(start,end)
    for i in range(int(len(plain))):
        r1,c1=checkmat(start[i],matrix)
        r2,c2=checkmat(end[i],matrix)
        if r1==r2:
            print("same row",r1,c1,r2,c2)
            if c1==1 :
                cipher.append(change(r1,c1+4,matrix))
                cipher.append(change(r2,c2-1,matrix))
            elif c2==1:
                cipher.append(change(r1,c1-1,matrix))
                cipher.append(change(r2,c2+4,matrix))
            else:
                cipher.append(change(r1,c1-1,matrix))
                cipher.append(change(r2,c2-1,matrix))
        elif c1==c2:
            print("same col",r1,c1,r2,c2)
            if r1==1 :
                cipher.append(change(r1+4,c1,matrix))
                cipher.append(change(r2-1,c2,matrix))
            elif r2==1:
                cipher.append(change(r1-1,c1,matrix))
                cipher.append(change(r2+4,c2,matrix))
            else:
                cipher.append(change(r1-1,c1,matrix))
                cipher.append(change(r2-1,c2,matrix))
        else:
            print(r1,c1,r2,c2)
            cipher.append(change(r1,c2,matrix))
            cipher.append(change(r2,c1,matrix))
    label=Label(frame,text="Decryption:" ,padx=5,pady=5)
    label.grid(row=4,column=0)
    label=Label(frame,text=cipher,padx=5,pady=5)
    label.grid(row=4,column=1)

#untuk membuka file teks dan langsung ada di kotak teks
def openfiletxt():
    file = filedialog.askopenfile(mode='r', filetypes=[('Text files', 'txt')])
    if file is not None:
        content = file.read(10000)
        plain.set(content)

#untuk membuka file nonteks
def openfilebiner():
    file = filedialog.askopenfile(mode='rb', filetypes=[('All files', '*')])
    if file is not None:
        content = file.read(10000)
        plain.set(content)

#fitur untuk menyimpan file teks jika sudah dienkripsi/didekripsi
def savefile():
    if len(plain.get()) == 0:
        messagebox.showerror("Error", "Plain text is empty")
    else:
        file = filedialog.asksaveasfile(mode='w', filetypes=[('Text files', 'txt')])
        if file is not None:
            file.write(plain.get())
            file.close()

#fungsi menampilkan text dalam kelompok 5 huruf
def fiveletters(text):
    newtext = ""
    count = 0
    for i in text:
        if count%5 == 0:
            newtext = newtext + " "
        newtext = newtext + i
        count = count + 1
    return newtext

#menghapus semua kotak
def clear():
    keyy.set("")
    plain.set("")
    entry.set("")

#keluar dari program
def exit():
    frame.destroy()

playfair=Tk()

msg = StringVar()
text = StringVar()
plain = StringVar()
cipher = StringVar()
plainfive = StringVar()

label1=Label(playfair,text="Playfair Cipher" ,padx=5,pady=5)
label1.pack(padx=30,pady=30)

frame=LabelFrame(playfair,text="",padx=60,pady=60)
frame.pack(padx=30,pady=30)

label=Label(frame,text="Enter message" ,padx=5,pady=5)
label.grid(row=1,column=0)

entry=Entry(frame)
entry.grid(row=1,column=1)

label=Label(frame,text="Enter key" ,padx=5,pady=5)
label.grid(row=2,column=0)

keyy=Entry(frame)
keyy.grid(row=2,column=1)

label3 = Label(frame, text="Plain Text 5 Letters Group")
label3.grid(row=1, column=2, sticky=W, padx=5, pady=5)
entry3 = Entry(frame, textvariable=plainfive)
entry3.grid(row=1, column=3, sticky=W, padx=5, pady=5)

button1=Button(frame,text="Encrypt",command=encryption)
button1.grid(row=1,column=5)

button2=Button(frame,text="Decrypt",command=decryption)
button2.grid(row=2,column=5)

button3 = Button(frame, text="Open Text File", command=openfiletxt)
button3.grid(row=4, column=0, sticky=W, padx=5, pady=5)

button4 = Button(frame, text="Open Binary File", command=openfilebiner)
button4.grid(row=4, column=1, sticky=W, padx=5, pady=5)

button5 = Button(frame, text="Save", command=savefile)
button5.grid(row=4, column=2, sticky=W, padx=5, pady=5)

button6 = Button(frame, text="Clear", command=clear)
button6.grid(row=5, column=0, sticky=W, padx=5, pady=5)

button7 = Button(frame, text="Exit", command=exit)
button7.grid(row=5, column=1, sticky=W, padx=5, pady=5)

playfair.mainloop()