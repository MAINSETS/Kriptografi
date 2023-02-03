import tkinter as tk
import string
from tkinter import *

def encrypt_text():
    input_text = input_entry.get()
    rotors = [3,2,1] 
    alphabet = string.ascii_uppercase
    enigma = {}
    for i in range(len(alphabet)):
        enigma[alphabet[i]] = alphabet[(i + rotors[0]) % 26]
        enigma[alphabet[i]] = alphabet[(alphabet.index(enigma[alphabet[i]]) + rotors[1]) % 26]
        enigma[alphabet[i]] = alphabet[(alphabet.index(enigma[alphabet[i]]) + rotors[2]) % 26]

    result = []
    for char in input_text:
        result.append(enigma[char.upper()] if char.upper() in enigma else char)
    output_label["text"] = "".join(result)

def decrypt_text():
    input_text = input_entry.get()
    rotors = [3,2,1] 
    alphabet = string.ascii_uppercase
    enigma = {}
    for i in range(len(alphabet)):
        enigma[alphabet[i]] = alphabet[(i + rotors[0]) % 26]
        enigma[alphabet[i]] = alphabet[(alphabet.index(enigma[alphabet[i]]) + rotors[1]) % 26]
        enigma[alphabet[i]] = alphabet[(alphabet.index(enigma[alphabet[i]]) + rotors[2]) % 26]

    result = []
    for char in input_text:
        result.append(enigma[char.upper()] if char.upper() in enigma else char)
    output_label["text"] = "".join(result)

def displayrotors():
    rotors = [3,2,1] 
    alphabet = string.ascii_uppercase
    enigma = {}
    for i in range(len(alphabet)):
        enigma[alphabet[i]] = alphabet[(i + rotors[0]) % 26]
        enigma[alphabet[i]] = alphabet[(alphabet.index(enigma[alphabet[i]]) + rotors[1]) % 26]
        enigma[alphabet[i]] = alphabet[(alphabet.index(enigma[alphabet[i]]) + rotors[2]) % 26]
    output_label["text"] = enigma

#menghapus semua kotak
def clear():
    input_entry.delete(0, END)
    output_label["text"] = ""

#keluar dari program
def exit():
    root.destroy()

root = tk.Tk()
root.title("Enigma Cipher")
root.geometry("700x400")
root.resizable(0, 0)

input_label = tk.Label(root, text="Plain Text:")
input_label.grid(row=0, column=0, sticky=W, padx=5, pady=5)

input_entry = tk.Entry(root)
input_entry.grid(row=0, column=1, sticky=W, padx=5, pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=1, column=0, sticky=W, padx=5, pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=1, column=1, sticky=W, padx=5, pady=5)

rotors_button = tk.Button(root, text="Display Rotors", command=displayrotors)
rotors_button.grid(row=1, column=2, sticky=W, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=1, column=3, sticky=W, padx=5, pady=5)

exit_button = tk.Button(root, text="Exit", command=exit)
exit_button.grid(row=1, column=4, sticky=W, padx=5, pady=5)

output_label = tk.Label(root, text="Cipher Text:")
output_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)

root.mainloop()
