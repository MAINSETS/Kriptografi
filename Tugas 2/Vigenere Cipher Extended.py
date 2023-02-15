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
        messagebox.showerror("Error", "Key and/or plain text is not in this 256 ASCII characters")


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
        messagebox.showerror("Error", "Key and/or plain text is not in this 256 ASCII characters")


#untuk membuka file teks dan langsung ada di kotak teks
def openfiletxt():
    file = filedialog.askopenfile(mode='r', filetypes=[('Text files', 'txt')])
    if file is not None:
        content = file.read()
        plain.set(content)

# Fungsi untuk membuka file binary
def openfilebiner():
    file = filedialog.askopenfile(mode='rb', filetypes=[('All files', '*')])
    data = file.read()
    data_str = data.decode('latin-1')
    plain.set(data_str)

#fitur untuk menyimpan file teks jika sudah dienkripsi/didekripsi
def savefile():
    if len(plain.get()) == 0:
        messagebox.showerror("Error", "Plain text is empty")
    else:
        file = filedialog.asksaveasfile(mode='w', filetypes=[('Text files', 'txt')])
        if file is not None:
            file.write(plain.get())
            file.close()

# Fungsi untuk menyimpan file binary
def savefilebiner():
    file = filedialog.asksaveasfile(mode='wb', filetypes=[('All files', '*')])
    text = plain.get()
    data = text.encode('latin-1')
    file.write(data)
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
    plainfive.set("")
    cipherfive.set("")

#keluar dari program
def exit():
    root.destroy()

#membuat GUI dari frame, label, dan tombol
root = Tk()
root.title("Vigenere Cipher Extended")
root.geometry("600x400")
root.resizable(0, 0)
root.configure(bg = "#FBE6BF")

key = StringVar()
plain = StringVar()
cipher = StringVar()
cipherfive = StringVar()
plainfive = StringVar()

label1 = Label(root, text="Key", bg = "#FBE6BF")
label1.grid(row=0, column=0, sticky=W, padx=5, pady=5)
entry1 = Entry(root, textvariable=key)
entry1.grid(row=0, column=1, sticky=W, padx=5, pady=5)

label2 = Label(root, text="Plain Text", bg = "#FBE6BF")
label2.grid(row=1, column=0, sticky=W, padx=5, pady=5)
entry2 = Entry(root, textvariable=plain)
entry2.grid(row=1, column=1, sticky=W, padx=5, pady=5)

label3 = Label(root, text="Plain Text 5 Letters Group", bg = "#FBE6BF")
label3.grid(row=1, column=2, sticky=W, padx=5, pady=5)
entry3 = Entry(root, textvariable=plainfive, state=DISABLED)
entry3.grid(row=1, column=3, sticky=W, padx=5, pady=5)

label4 = Label(root, text="Cipher Text", bg = "#FBE6BF")
label4.grid(row=2, column=0, sticky=W, padx=5, pady=5)
entry4 = Entry(root, textvariable=cipher)
entry4.grid(row=2, column=1, sticky=W, padx=5, pady=5)

label5 = Label(root, text="Cipher Text 5 Letters Group", bg = "#FBE6BF")
label5.grid(row=2, column=2, sticky=W, padx=5, pady=5)
entry5 = Entry(root, textvariable=cipherfive, state=DISABLED)
entry5.grid(row=2, column=3, sticky=W, padx=5, pady=5)

button1 = Button(root, text="Encrypt", command=encrypt, bg = "#FBB43C")
button1.grid(row=3, column=0, sticky=W, padx=5, pady=5)

button2 = Button(root, text="Decrypt", command=decrypt, bg = "#FBB43C")
button2.grid(row=3, column=1, sticky=W, padx=5, pady=5)

button3 = Button(root, text="Open Text File", command=openfiletxt, bg = "#FBB43C")
button3.grid(row=4, column=0, sticky=W, padx=5, pady=5)

button4 = Button(root, text="Open Binary File", command=openfilebiner, bg = "#FBB43C")
button4.grid(row=4, column=1, sticky=W, padx=5, pady=5)

button5 = Button(root, text="Save Text", command=savefile, bg = "#FBB43C")
button5.grid(row=4, column=2, sticky=W, padx=5, pady=5)

button6 = Button(root, text="Clear", command=clear, bg = "#FBB43C")
button6.grid(row=5, column=0, sticky=W, padx=5, pady=5)

button7 = Button(root, text="Exit", command=exit, bg = "#FBB43C")
button7.grid(row=5, column=1, sticky=W, padx=5, pady=5)

button8 = Button(root, text="Save Binary", command=savefilebiner, bg = "#FBB43C")
button8.grid(row=4, column=3, sticky=W, padx=5, pady=5)


root.mainloop()

