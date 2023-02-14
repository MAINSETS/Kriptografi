from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

#fungsi untuk mengenkripsi
def encrypt():
    if len(key.get()) == 0 or len(plain.get()) == 0:
        messagebox.showerror("Error", "Key or Plain text is empty")
    else:
        keylist = []
        for i in key.get():
            keylist.append(ord(i))
        s = ksa(keylist)
        keystream = prga(s, len(plain.get()))
        cipherlist = []
        for i in range(len(plain.get())):
            cipherlist.append(ord(plain.get()[i]) ^ keystream[i])
        ciphertext = ""
        for i in cipherlist:
            ciphertext = ciphertext + chr(i)
        cipher.set(ciphertext)
        cipherfive.set(fiveletters(ciphertext))

#fungsi untuk mendekripsi
def decrypt():
    if len(key.get()) == 0 or len(cipher.get()) == 0:
        messagebox.showerror("Error", "Key or Cipher text is empty")
    else:
        keylist = []
        for i in key.get():
            keylist.append(ord(i))
        s = ksa(keylist)
        keystream = prga(s, len(cipher.get()))
        plainlist = []
        for i in range(len(cipher.get())):
            plainlist.append(ord(cipher.get()[i]) ^ keystream[i])
        plaintext = ""
        for i in plainlist:
            plaintext = plaintext + chr(i)
        plain.set(plaintext)
        plainfive.set(fiveletters(plaintext))

#fungsi untuk mengacak key
def ksa(key):
    keylength = len(key)
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % keylength]) % 256
        s[i], s[j] = s[j], s[i]
    return s

#fungsi untuk mengacak plaintext
def prga(s, n):
    i = 0
    j = 0
    keystream = []
    for k in range(n):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        keystream.append(s[(s[i] + s[j]) % 256])
    return keystream


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
entry3 = Entry(root, textvariable=plainfive, state=DISABLED)
entry3.grid(row=1, column=3, sticky=W, padx=5, pady=5)

label4 = Label(root, text="Cipher Text")
label4.grid(row=2, column=0, sticky=W, padx=5, pady=5)
entry4 = Entry(root, textvariable=cipher)
entry4.grid(row=2, column=1, sticky=W, padx=5, pady=5)

label5 = Label(root, text="Cipher Text 5 Letters Group")
label5.grid(row=2, column=2, sticky=W, padx=5, pady=5)
entry5 = Entry(root, textvariable=cipherfive, state=DISABLED)
entry5.grid(row=2, column=3, sticky=W, padx=5, pady=5)

button1 = Button(root, text="Encrypt", command=encrypt)
button1.grid(row=3, column=0, sticky=W, padx=5, pady=5)

button2 = Button(root, text="Decrypt", command=decrypt)
button2.grid(row=3, column=1, sticky=W, padx=5, pady=5)

button3 = Button(root, text="Open Text File", command=openfiletxt)
button3.grid(row=4, column=0, sticky=W, padx=5, pady=5)

button4 = Button(root, text="Open Binary File", command=openfilebiner)
button4.grid(row=4, column=1, sticky=W, padx=5, pady=5)

button5 = Button(root, text="Save Text", command=savefile)
button5.grid(row=4, column=2, sticky=W, padx=5, pady=5)

button6 = Button(root, text="Clear", command=clear)
button6.grid(row=5, column=0, sticky=W, padx=5, pady=5)

button7 = Button(root, text="Exit", command=exit)
button7.grid(row=5, column=1, sticky=W, padx=5, pady=5)

button8 = Button(root, text="Save Binary", command=savefilebiner)
button8.grid(row=4, column=3, sticky=W, padx=5, pady=5)


root.mainloop()