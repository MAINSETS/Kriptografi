import string
import random as rd
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
#fungsi untuk mengenkripsi pesan
def encrypt():
    if len(plain.get()) == 0:
        messagebox.showerror("Error", "Plain text is empty")
    elif len(keyy.get()) == 0:
        messagebox.showerror("Error", "Key is empty")
    else:
        key = keyy.get()
        #menghapus spasi, karakter non-ascii, dan huruf J pada key, ubah ke huruf besar
        key = removeNonASCII(removeSpacesJ(toUpperCase(key)))
        #menghapus duplikasi huruf
        key = "".join(dict.fromkeys(key))
        #menambahkan key dengan backkey: berupa huruf yang belum ada pada key
        backkey = ""
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for i in alphabet:
            if i not in key:
                backkey = backkey + i
        key = key + backkey
        #membuat matrix key
        matrix = [key[0:5], key[5:10], key[10:15], key[15:20], key[20:25]]
        
        msg1 = plain.get()
        msg1= removeNonASCII(removeSpaces(toUpperCase(msg1)))
        msg1 = msg1.replace("J", "I")
        msg1 = list(msg1)
        i = 0
        while i < len(msg1):
            if msg1[i] == msg1[i + 1]:
                msg1.insert(i + 1, "X")
            i = i + 2
            if len(msg1) % 2 != 0:
                msg1.append("X")
        i = 0
        while i < len(msg1):
            a = 0
            b = 0
            c = 0
            d = 0
            for j in range(5):
                for k in range(5):
                    if msg1[i] == matrix[j][k]:
                        a = j
                        b = k
                    if msg1[i + 1] == matrix[j][k]:
                        c = j
                        d = k
            if a == c:
                if b == 4:
                    b = -1
                if d == 4:
                    d = -1
                msg1[i] = matrix[a][b + 1]
                msg1[i + 1] = matrix[c][d + 1]
            elif b == d:
                if a == 4:
                    a = -1
                if c == 4:
                    c = -1
                msg1[i] = matrix[a + 1][b]
                msg1[i + 1] = matrix[c + 1][d]
            else:
                msg1[i] = matrix[a][d]
                msg1[i + 1] = matrix[c][b]
            i = i + 2
        msg1 = "".join(msg1)
    cipher.set(msg1)
    cipherfive.set(fiveletters(msg1))
    messagebox.showinfo("Success", "Encryption Success")

        
#fungsi untuk mendekripsi pesan
def decrypt():
    if len(cipher.get()) == 0:
        messagebox.showerror("Error", "Plain text is empty")
    elif len(keyy.get()) == 0:
        messagebox.showerror("Error", "Key is empty")
    else:
        key = keyy.get()
        #menghapus spasi, karakter non-ascii, dan huruf J pada key, ubah ke huruf besar
        key = removeNonASCII(removeSpacesJ(toUpperCase(key)))
        #menghapus duplikasi huruf
        key = "".join(dict.fromkeys(key))
        #menambahkan key dengan backkey berupa huruf yang belum ada pada key
        backkey = ""
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for i in alphabet:
            if i not in key:
                backkey = backkey + i
        key = key + backkey
        #membuat matrix key
        matrix = [key[0:5], key[5:10], key[10:15], key[15:20], key[20:25]]
        
        msg1 = cipher.get()
        msg1= removeNonASCII(removeSpaces(toUpperCase(msg1)))
        msg1 = msg1.replace("J", "I")
        msg1 = list(msg1)
        i = 0
        while i < len(msg1):
            if msg1[i] == msg1[i + 1]:
                msg1.insert(i + 1, "X")
            i = i + 2
            if len(msg1) % 2 != 0:
                msg1.append("X")
        i = 0
        while i < len(msg1):
            a = 0
            b = 0
            c = 0
            d = 0
            for j in range(5):
                for k in range(5):
                    if msg1[i] == matrix[j][k]:
                        a = j
                        b = k
                    if msg1[i + 1] == matrix[j][k]:
                        c = j
                        d = k
            if a == c:
                if b == 0:
                    b = 5
                if d == 0:
                    d = 5
                msg1[i] = matrix[a][b - 1]
                msg1[i + 1] = matrix[c][d - 1]
            elif b == d:
                if a == 0:
                    a = 5
                if c == 0:
                    c = 5
                msg1[i] = matrix[a - 1][b]
                msg1[i + 1] = matrix[c - 1][d]
            else:
                msg1[i] = matrix[a][d]
                msg1[i + 1] = matrix[c][b]
            i = i + 2
        msg1 = "".join(msg1)
    plain.set(msg1)
    plainfive.set(fiveletters(msg1))
    messagebox.showinfo("Success", "Decryption success")

#menampilkan matriks 5x5
def matrix():
    if len(keyy.get()) == 0:
        messagebox.showerror("Error", "Key is empty")
    else:
        key = keyy.get()
        #menghapus spasi, karakter non-ascii, dan huruf J pada key, ubah ke huruf besar
        key = removeNonASCII(removeSpacesJ(toUpperCase(key)))
        #menghapus duplikasi huruf
        key = "".join(dict.fromkeys(key))
        #menambahkan key dengan backkey berupa huruf yang belum ada pada key
        backkey = ""
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for i in alphabet:
            if i not in key:
                backkey = backkey + i
        key = key + backkey
        key = list(key)
        #membuat matrix key
        matrix = [key[0:5], key[5:10], key[10:15], key[15:20], key[20:25]]
        return matrix

def displaymatrix(table): 
    res1 = '[{}]\n'.format(' '.join(table[0]))
    res2 = ''
    for i in range(1,len(table)-1,1):
        res2 = res2 + '|{}|\n'.format(' '.join(table[i]))
    res3 = '[{}]\n'.format(' '.join(table[len(table)-1]))
    res = res1 + res2 + res3
    messagebox.showinfo("Matrix", res)

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

#fungsi mengubah semua text menjadi upper case
def toUpperCase(text):
	return text.upper()

#fungsi menghapus spasi
def removeSpaces(text):
	newtext = ""
	for i in text:
		if i == " ":
			continue
		else:
			newtext = newtext + i
	return newtext

#fungsi menghapus spasi dan J
def removeSpacesJ(text):
	newtext = ""
	for i in text:
		if i == " " or i == "J":
			continue
		else:
			newtext = newtext + i
	return newtext

#fungsi menghapus karakter non-alfabet 
def removeNonASCII(text):
    text.upper()
    newtext = ""
    for i in text:
        if i not in string.ascii_uppercase:
            continue
        else:
            newtext = newtext + i
    return newtext

#menghapus semua kotak
def clear():
    keyy.set("")
    plain.set("")
    plainfive.set("")
    cipher.set("")
    cipherfive.set("")

#keluar dari program
def exit():
    root.destroy()

root=Tk()
root.title("Play Fair Cipher")
root.geometry("600x400")
root.resizable(0, 0)

plain = StringVar()
keyy = StringVar()
cipher = StringVar()
plainfive = StringVar()
cipher = StringVar()
cipherfive = StringVar()

label1 = Label(root, text="Key")
label1.grid(row=0, column=0, sticky=W, padx=5, pady=5)
entry1 = Entry(root, textvariable=keyy)
entry1.grid(row=0, column=1, sticky=W, padx=5, pady=5)

label2 = Label(root, text="Plain Text")
label2.grid(row=1, column=0, sticky=W, padx=5, pady=5)
entry2 = Entry(root, textvariable=plain)
entry2.grid(row=1, column=1, sticky=W, padx=5, pady=5)

label3 = Label(root, text="Plain Text 5 Letters Group")
label3.grid(row=1, column=2, sticky=W, padx=5, pady=5)
entry3 = Entry(root, textvariable=plainfive, state=DISABLED)
entry3.grid(row=1, column=3, sticky=W, padx=5, pady=5)

label4 = Label(root, text="Cipher Text")
label4.grid(row=2, column=0, sticky=W, padx=5, pady=5)
entry4 = Entry(root, textvariable=cipher)
entry4.grid(row=2, column=1, sticky=W, padx=5, pady=5)

label5 = Label(root, text="Cipher Text 5 Letters Group")
label5.grid(row=2, column=2, sticky=W, padx=5, pady=5)
entry5 = Entry(root, textvariable=cipherfive,state=DISABLED)
entry5.grid(row=2, column=3, sticky=W, padx=5, pady=5)

button1=Button(root,text="Encrypt",command=encrypt)
button1.grid(row=3,column=0, sticky=W, padx=5, pady=5)

button2=Button(root,text="Decrypt",command=decrypt)
button2.grid(row=3,column=1, sticky=W, padx=5, pady=5)

button3 = Button(root, text="Open Text File", command=openfiletxt)
button3.grid(row=4, column=0, sticky=W, padx=5, pady=5)

button4 = Button(root, text="Open Binary File", command=openfilebiner)
button4.grid(row=4, column=1, sticky=W, padx=5, pady=5)

button5 = Button(root, text="Save", command=savefile)
button5.grid(row=4, column=2, sticky=W, padx=5, pady=5)

button6 = Button(root, text="Clear", command=clear)
button6.grid(row=5, column=0, sticky=W, padx=5, pady=5)

button7 = Button(root, text="Exit", command=exit)
button7.grid(row=5, column=1, sticky=W, padx=5, pady=5)

button8 = Button(root, text="Display Matrix", command=lambda:displaymatrix(matrix()))
button8.grid(row=5, column=2, sticky=W, padx=5, pady=5)

root.mainloop()