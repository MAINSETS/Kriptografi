from pydoc import plain
import numpy as np
import random as rd
from tkinter import *

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
    label=Label(frame,text="Encryption:",font=(20,20) ,padx=10,pady=10)
    label.grid(row=3,column=0)
    label=Label(frame,text=cipher,font=(20,20) ,padx=10,pady=10)
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
    label=Label(frame,text="Decryption:",font=(20,20) ,padx=10,pady=10)
    label.grid(row=4,column=0)
    label=Label(frame,text=cipher,font=(20,20) ,padx=10,pady=10)
    label.grid(row=4,column=1)

playfair=Tk()

label1=Label(playfair,text="Playfair Cipher",font=(30,30) ,padx=10,pady=10)
label1.pack(padx=30,pady=30)

frame=LabelFrame(playfair,text="",padx=60,pady=60)
frame.pack(padx=30,pady=30)

label=Label(frame,text="Enter message",font=(20,20) ,padx=10,pady=10)
label.grid(row=1,column=0)

entry=Entry(frame,font=(20,20))
entry.grid(row=1,column=1)

label=Label(frame,text="Enter key",font=(20,20) ,padx=10,pady=10)
label.grid(row=2,column=0)

keyy=Entry(frame,font=(20,20))
keyy.grid(row=2,column=1)

button=Button(frame,text="Encrypt",command=encryption)
button.grid(row=1,column=2)

button=Button(frame,text="Decrypt",command=decryption)
button.grid(row=1,column=3)

playfair.mainloop()