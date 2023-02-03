import tkinter as tk
import string
from tkinter import *

def encrypt():
    plaintext = input_entry.get()
    plaintext = plaintext.upper()
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
    output_label["text"] = ciphertext

def decrypt():
    ciphertext = input_entry.get()
    ciphertext = ciphertext.upper()
    alphabet = string.ascii_uppercase
    enigma = {}
    for i in range(len(alphabet)):
        enigma[alphabet[i]] = alphabet[(i + 3) % 26]
        enigma[alphabet[i]] = alphabet[(alphabet.index(enigma[alphabet[i]]) + 2) % 26]
        enigma[alphabet[i]] = alphabet[(alphabet.index(enigma[alphabet[i]]) + 1) % 26]
    plaintext = ""
    for char in ciphertext:
        if char in alphabet:
            plaintext += alphabet[(alphabet.index(char) - 3) % 26]
            plaintext += alphabet[(alphabet.index(plaintext[-1]) - 2) % 26]
            plaintext += alphabet[(alphabet.index(plaintext[-1]) - 1) % 26]
        else:
            plaintext += char
    input.set(plaintext)

def displayrotors():
    rotors = [3,2,1] 
    alphabet = string.ascii_uppercase
    enigma = {}
    for i in range(len(alphabet)):
        enigma[alphabet[i]] = alphabet[(i + rotors[0]) % 26]
        enigma[alphabet[i]] = alphabet[(alphabet.index(enigma[alphabet[i]]) + rotors[1]) % 26]
        enigma[alphabet[i]] = alphabet[(alphabet.index(enigma[alphabet[i]]) + rotors[2]) % 26]
    output_label2["text"] = enigma

#menghapus semua kotak
def clear():
    input_entry.delete(0, END)
    output_label["text"] = ""

#keluar dari program
def exit():
    root.destroy()

root = tk.Tk()
root.title("Enigma Cipher")
root.geometry("1150x400")
root.resizable(0, 0)

input = StringVar()

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
rotors_button.grid(row=5, column=0, sticky=W, padx=5, pady=5)

input_label2 = tk.Label(root, text="Cipher Text:")
input_label2.grid(row=2, column=0, sticky=W, padx=5, pady=5)

output_label = tk.Label(root)
output_label.grid(row=2, column=1, sticky=W, padx=5, pady=5)

output_label2 = tk.Label(root)
output_label2.grid(row=5, column=1, sticky=W, padx=5, pady=5)

root.mainloop()
