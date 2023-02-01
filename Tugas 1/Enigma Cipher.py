import string
import random
import string
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def encrypt():
    #membuat kunci
    key = []
    for i in range(3):
        key.append(random.randint(0,25))
    print(key)
    #membuat 3 rotor
    rotor = []
    for i in range(3):
        rotor.append(list(string.ascii_uppercase))
        random.shuffle(rotor[i])
    print(rotor)
    #membuat reflector
    reflector = list(string.ascii_uppercase)
    random.shuffle(reflector)
    print(reflector)
    #membuat plain text
    plain_text = plain.get()
    #membuat cipher text
    cipher_text = ""
    for i in range(len(plain_text)):
        #mengubah huruf ke angka
        plain_number = ord(plain_text[i]) - 65
        #mengubah angka ke huruf
        cipher_number = ord(rotor[0][(rotor[1][(rotor[2][plain_number] - key[2]) % 26] - key[1]) % 26] - key[0]) % 26
        cipher_text = cipher_text + reflector[cipher_number]
        #menggeser kunci
        key[2] = (key[2] + 1) % 26
        if key[2] == 0:
            key[1] = (key[1] + 1) % 26
            if key[1] == 0:
                key[0] = (key[0] + 1) % 26
    print(cipher_text)
    #menampilkan cipher text
    cipher.set(cipher_text)
    cipherfive.set(fiveletters(cipher_text))

def decrypt():
    #membuat kunci
    key = []
    for i in range(3):
        key.append(random.randint(0,25))
    print(key)
    #membuat 3 rotor
    rotor = []
    for i in range(3):
        rotor.append(list(string.ascii_uppercase))
        random.shuffle(rotor[i])
    print(rotor)
    #membuat reflector
    reflector = list(string.ascii_uppercase)
    random.shuffle(reflector)
    print(reflector)
    #membuat cipher text
    cipher_text = cipher.get()
    #membuat plain text
    plain_text = ""
    for i in range(len(cipher_text)):
        #mengubah huruf ke angka
        cipher_number = ord(cipher_text[i]) - 65
        #mengubah angka ke huruf
        plain_number = rotor[2][(rotor[1][(rotor[0][(reflector[cipher_number] + key[0]) % 26] + key[1]) % 26] + key[2]) % 26]
        plain_text = plain_text + plain_number
        #menggeser kunci
        key[2] = (key[2] + 1) % 26
        if key[2] == 0:
            key[1] = (key[1] + 1) % 26
            if key[1] == 0:
                key[0] = (key[0] + 1) % 26
    print(plain_text)
    #menampilkan plain text
    plain.set(plain_text)
    plainfive.set(fiveletters(plain_text))

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
root.title("Enigma Chiper")
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

button5 = Button(root, text="Save", command=savefile)
button5.grid(row=4, column=2, sticky=W, padx=5, pady=5)

button6 = Button(root, text="Clear", command=clear)
button6.grid(row=5, column=0, sticky=W, padx=5, pady=5)

button7 = Button(root, text="Exit", command=exit)
button7.grid(row=5, column=1, sticky=W, padx=5, pady=5)


root.mainloop()