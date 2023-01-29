from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

#melakukan enkripsi 26 huruf alphabet dengan konversi ke huruf kapital
#cipher text yang berupa nonalphabet yang pembacaannya diskip pada saat dekripsi, tidak bisa dikembalikan menjadi cipher text semula dengan karakter nonalphabet
#key harus berupa alphabet
def encrypt():
    if len(key.get()) == 0:
        messagebox.showerror("Error", "Key is empty")
    elif len(plain.get()) == 0:
        messagebox.showerror("Error", "Plain text is empty")
    #pengecekan kunci harus alphabet
    if (key.get() >= chr(65) and key.get() <= chr(90) or key.get() >= chr(97) and key.get() <= chr(122)):
        keyinput = key.get()   
        keyinput = keyinput.replace(" ", "")  
        keyinput = keyinput.upper()
        plaintextinput = plain.get()
        plaintextinput = plaintextinput.upper()
        plaintextinput = plaintextinput.replace(" ", "")
        ciphertext = ""
        for i in range(len(plaintextinput)):
            if(plaintextinput[i] >= chr(65) and plaintextinput[i] <= chr(90)):
                ciphertext += chr(((ord(plaintextinput[i]) - 65) + (ord(keyinput[i % len(keyinput)]) - 65)) % 26 + 65)
            else:
                continue
        cipher.set(ciphertext)
        cipherfive.set(fiveletters(ciphertext))
        messagebox.showinfo("Success", "Encryption Success")
    else:
        messagebox.showerror("Error", "Key is not alphabet")


#melakukan dekripsi 26 huruf alphabet dengan konversi ke huruf kapital
#plain text yang berupa nonalphabet yang pembacaannya diskip pada saat enkripsi, tidak bisa dikembalikan menjadi plain text semula dengan karakter nonalphabet
#key harus berupa alphabet
def decrypt():
    if len(key.get()) == 0:
        messagebox.showerror("Error", "Key is empty")
    elif len(cipher.get()) == 0:
        messagebox.showerror("Error", "Cipher text is empty")
    elif (key.get() >= chr(65) and key.get() <= chr(90) or key.get() >= chr(97) and key.get() <= chr(122)):
        keyinput = key.get()
        keyinput = keyinput.replace(" ", "")
        keyinput = keyinput.upper()
        ciphertext = cipher.get()
        ciphertext = ciphertext.upper()
        ciphertext = ciphertext.replace(" ", "")
        plaintextinput = ""
        for i in range(len(ciphertext)):
            if(ciphertext[i] >= chr(65) and ciphertext[i] <= chr(90)):
                plaintextinput += chr(((ord(ciphertext[i]) - 65) - (ord(keyinput[i % len(keyinput)]) - 65)) % 26 + 65)
            else:
                continue
        plain.set(plaintextinput)
        plainfive.set(fiveletters(plaintextinput))
        messagebox.showinfo("Success", "Decryption success")
    else:
        messagebox.showerror("Error", "Key and chiper text is not match!")

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
root.title("Vigenere Cipher Standard")
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


root.mainloop()
