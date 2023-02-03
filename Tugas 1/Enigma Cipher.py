import tkinter as tk
import string

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

root = tk.Tk()
root.title("Enigma Cipher")
root.geometry("700x400")

input_label = tk.Label(root, text="Plain Text:")
input_label.pack()

input_entry = tk.Entry(root)
input_entry.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.pack()

rotors_button = tk.Button(root, text="Display Rotors", command=displayrotors)
rotors_button.pack()

output_label = tk.Label(root, text="Cipher Text:")
output_label.pack()

root.mainloop()
