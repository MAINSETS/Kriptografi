import tkinter as tk
import string
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def encrypt():
    plaintext = input_entry.get()
    plaintext = plaintext.upper()
    plaintext = removeNonASCII(removeSpaces(toUpperCase(plaintext)))
    alphabet = string.ascii_uppercase
    enigma = {}
    for i in range(len(alphabet)):
        enigma[alphabet[i]] = alphabet[(i + 3) % 26]
        enigma[alphabet[i]] = alphabet[(alphabet.index(enigma[alphabet[i]]) + 2) % 26]
        enigma[alphabet[i]] = alphabet[(alphabet.index(enigma[alphabet[i]]) + 1) % 26]
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            ciphertext += enigma[char]
        else:
            ciphertext += char
    output.set(ciphertext)
    cipherfive.set(fiveletters(ciphertext))

def decrypt():
    ciphertext = input_entry.get()
    ciphertext = ciphertext.upper()
    ciphertext = removeNonASCII(removeSpaces(toUpperCase(ciphertext)))
    alphabet = string.ascii_uppercase
    enigma = {}
    for i in range(len(alphabet)):
        enigma[alphabet[i]] = alphabet[(i + 3) % 26]
        enigma[alphabet[i]] = alphabet[(alphabet.index(enigma[alphabet[i]]) + 2) % 26]
        enigma[alphabet[i]] = alphabet[(alphabet.index(enigma[alphabet[i]]) + 1) % 26]
    plaintext = ""
    for char in ciphertext:
        if char in alphabet:
            plaintext += alphabet[(alphabet.index(char)) % 26]
        else:
            plaintext += char
    input.set(plaintext)
    plainfive.set(fiveletters(plaintext))

def displayrotors():
    rotors = [3,2,1] 
    alphabet = string.ascii_uppercase
    enigma = {}
    for i in range(len(alphabet)):
        enigma[alphabet[i]] = alphabet[(i + rotors[0]) % 26]
        enigma[alphabet[i]] = alphabet[(alphabet.index(enigma[alphabet[i]]) + rotors[1]) % 26]
        enigma[alphabet[i]] = alphabet[(alphabet.index(enigma[alphabet[i]]) + rotors[2]) % 26]
    messagebox.showinfo("Rotors", enigma)

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

#untuk membuka file teks dan langsung ada di kotak teks
def openfiletxt():
    file = filedialog.askopenfile(mode='r', filetypes=[('Text files', 'txt')])
    if file is not None:
        content = file.read(10000)
        input.set(content)

#fitur untuk menyimpan file teks jika sudah dienkripsi/didekripsi
def savefile():
    if len(input.get()) == 0:
        messagebox.showerror("Error", "Plain text is empty")
    else:
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file is not None:
            file.write(input.get())
            file.close()
            
#menghapus semua kotak
def clear():
    input_entry.delete(0, END)
    output_label["text"] = ""
    input.set("")
    output.set("")
    plainfive.set("")
    cipherfive.set("")

#keluar dari program
def exit():
    root.destroy()

root = tk.Tk()
root.title("Enigma Cipher")
root.geometry("700x400")
root.resizable(0, 0)

input = StringVar()
output = StringVar()
plainfive = StringVar()
cipherfive = StringVar()

input_label = tk.Label(root, text="Plain Text:")
input_label.grid(row=0, column=0, sticky=W, padx=5, pady=5)

input_entry = tk.Entry(root, textvariable=input)
input_entry.grid(row=0, column=1, sticky=W, padx=5, pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.grid(row=1, column=0, sticky=W, padx=5, pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.grid(row=1, column=1, sticky=W, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=6, column=0, sticky=W, padx=5, pady=5)

exit_button = tk.Button(root, text="Exit", command=exit)
exit_button.grid(row=6, column=1, sticky=W, padx=5, pady=5)

rotors_button = tk.Button(root, text="Display Rotors", command=displayrotors)
rotors_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

input_label2 = tk.Label(root, text="Cipher Text:")
input_label2.grid(row=2, column=0, sticky=W, padx=5, pady=5)

output_label = tk.Label(root)
output_label.grid(row=2, column=1, sticky=W, padx=5, pady=5)
output2 = Entry(root, textvariable=output)
output2.grid(row=2, column=1, sticky=W, padx=5, pady=5)

label3 = Label(root, text="Plain Text 5 Letters Group")
label3.grid(row=0, column=2, sticky=W, padx=5, pady=5)
entry3 = Entry(root, textvariable=plainfive, state=DISABLED)
entry3.grid(row=0, column=3, sticky=W, padx=5, pady=5)

label4 = Label(root, text="Cipher Text 5 Letters Group")
label4.grid(row=1, column=2, sticky=W, padx=5, pady=5)
entry4 = Entry(root, textvariable=cipherfive, state=DISABLED)
entry4.grid(row=1, column=3, sticky=W, padx=5, pady=5)

button3 = Button(root, text="Open Text File", command=openfiletxt)
button3.grid(row=4, column=0, sticky=W, padx=5, pady=5)

button5 = Button(root, text="Save Cipher", command=savefile)
button5.grid(row=4, column=2, sticky=W, padx=5, pady=5)

root.mainloop()
