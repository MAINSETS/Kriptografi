from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

#melakukan enkripsi dengan constraint 256 karakter ASCII
#input dapat berupa spasi, tetapi hasil tidak akan ada spasi
def encrypt():
    if len(key.get()) == 0:
        messagebox.showerror("Error", "Key is empty")
    elif len(plain.get()) == 0:
        messagebox.showerror("Error", "Plain text is empty")
    elif (plain.get() >= chr(0) and plain.get() <= chr(255)) and (key.get() >= chr(0) and key.get() <= chr(255)):
        keyinput = key.get()   
        plaintextinput = plain.get()
        ciphertext = ""
        for i in range(len(plaintextinput)):
            ciphertext += chr(((ord(plaintextinput[i])) + (ord(keyinput[i % len(keyinput)]))) % 256)
        cipher.set(ciphertext)
        cipherfive.set(fiveletters(ciphertext))
        messagebox.showinfo("Success", "Encryption Success")
    else:
        messagebox.showerror("Error", "Key and/or plain text is not ASCII character")


#melakukan enkripsi dengan constraint 256 karakter ASCII
#input dapat berupa spasi, tetapi hasil tidak akan ada spasi
def decrypt():
    if len(key.get()) == 0:
        messagebox.showerror("Error", "Key is empty")
    elif len(cipher.get()) == 0:
        messagebox.showerror("Error", "Cipher text is empty")
    elif (cipher.get() >= chr(0) and cipher.get() <= chr(255)) and (key.get() >= chr(0) and key.get() <= chr(255)):
        keyinput = key.get()
        ciphertext = cipher.get()
        plaintextinput = ""
        for i in range(len(ciphertext)):
            plaintextinput += chr(((ord(ciphertext[i])) - (ord(keyinput[i % len(keyinput)]))) % 256)
        plain.set(plaintextinput)
        plainfive.set(fiveletters(plaintextinput))
        messagebox.showinfo("Success", "Decryption Success")
    else:
        messagebox.showerror("Error", "Key and/or plain text is not ASCII character")

#untuk membuka file teks dan langsung ada di kotak teks
def openfile():
    try:
        file = filedialog.askopenfile(mode='r', filetypes=[('All files', '*')])
        if file is not None:
            content = file.read(10000)
            plain.set(content)
    except:
        file = filedialog.askopenfile(mode='rb', filetypes=[('All files', '*')])
        if file is not None:
            content = file.read(10000)
            plain.set(content)

#fitur untuk menyimpan file teks jika sudah dienkripsi/didekripsi
def savefile():
    if len(plain.get()) == 0:
        messagebox.showerror("Error", "Plain text is empty")
    else:
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
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
    key.set("")
    plain.set("")
    cipher.set("")

#keluar dari program
def exit():
    root.destroy()

#membuat GUI dari frame, label, dan tombol
root = Tk()
root.title("Vigenere Cipher Extended")
root.geometry("600x400")
root.resizable(0, 0)

key = StringVar()
plain = StringVar()
cipher = StringVar()
cipherfive = StringVar()
plainfive = StringVar()

label1 = Label(root, text="Key")
label1.grid(row=0, column=0, sticky=W, padx=5, pady=5)
entry1 = Entry(root, textvariable=key)
entry1.grid(row=0, column=1, sticky=W, padx=5, pady=5)

label2 = Label(root, text="Plain Text")
label2.grid(row=1, column=0, sticky=W, padx=5, pady=5)
entry2 = Entry(root, textvariable=plain)
entry2.grid(row=1, column=1, sticky=W, padx=5, pady=5)

label3 = Label(root, text="Plain Text 5 Letters Group")
label3.grid(row=1, column=2, sticky=W, padx=5, pady=5)
entry3 = Entry(root, textvariable=plainfive)
entry3.grid(row=1, column=3, sticky=W, padx=5, pady=5)

label4 = Label(root, text="Cipher Text")
label4.grid(row=2, column=0, sticky=W, padx=5, pady=5)
entry4 = Entry(root, textvariable=cipher)
entry4.grid(row=2, column=1, sticky=W, padx=5, pady=5)

label5 = Label(root, text="Cipher Text 5 Letters Group")
label5.grid(row=2, column=2, sticky=W, padx=5, pady=5)
entry5 = Entry(root, textvariable=cipherfive)
entry5.grid(row=2, column=3, sticky=W, padx=5, pady=5)

button1 = Button(root, text="Encrypt", command=encrypt)
button1.grid(row=3, column=0, sticky=W, padx=5, pady=5)

button2 = Button(root, text="Decrypt", command=decrypt)
button2.grid(row=3, column=1, sticky=W, padx=5, pady=5)

button3 = Button(root, text="Open", command=openfile)
button3.grid(row=4, column=0, sticky=W, padx=5, pady=5)

button4 = Button(root, text="Save", command=savefile)
button4.grid(row=4, column=1, sticky=W, padx=5, pady=5)

button5 = Button(root, text="Clear", command=clear)
button5.grid(row=5, column=0, sticky=W, padx=5, pady=5)

button6 = Button(root, text="Exit", command=exit)
button6.grid(row=5, column=1, sticky=W, padx=5, pady=5)


root.mainloop()

