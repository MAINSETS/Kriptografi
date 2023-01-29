from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import string


#membuat GUI dari frame, label, dan tombol
root = Tk()
root.title("Play Fair Cipher")
root.geometry("600x400")
root.resizable(0, 0)

key = StringVar()
plain = StringVar()
cipher = StringVar()
cipherfive = StringVar()
plainfive = StringVar()

keyinput = key.get()
keyinput = keyinput.replace(" ", "")
keyinput = keyinput.upper()

def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]   

result=list()
for c in keyinput: 
    if c not in result:
        if c=='J':
            result.append('I')
        else:
            result.append(c)
flag=0
for i in range(65,91):
    if chr(i) not in result:
        if i==73 and chr(74) not in result:
            result.append("I")
            flag=1
        elif flag==0 and i==73 or i==74:
            pass    
        else:
            result.append(chr(i))
k=0
my_matrix=matrix(5,5,0) 
for i in range(0,5): 
    for j in range(0,5):
        my_matrix[i][j]=result[k]
        k+=1

def locindex(c):
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt(): 
    if len(key.get()) == 0:
        messagebox.showerror("Error", "Key is empty")
    elif len(plain.get()) == 0:
        messagebox.showerror("Error", "Plain text is empty")   
    plaintextinput = plain.get()
    plaintextinput = removeNonASCII(removeSpaces(toUpperCase(plaintextinput)))
    ciphertext = ""             
    i=0
    for s in range(0,len(plaintextinput)+1,2):
        if s<len(plaintextinput)-1:
            if plaintextinput[s]==plaintextinput[s+1]:
                plaintextinput=plaintextinput[:s+1]+'X'+plaintextinput[s+1:]
    if len(plaintextinput)%2!=0:
        plaintextinput=plaintextinput[:]+'X'
    while i<len(plaintextinput):
        loc=list()
        loc=locindex(plaintextinput[i])
        loc1=list()
        loc1=locindex(plaintextinput[i+1])
        if loc[1]==loc1[1]:
            ciphertext.format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]])
        elif loc[0]==loc1[0]:
            ciphertext.format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]) 
        else:
            ciphertext.format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]])   
        i=i+2 
    cipher.set(ciphertext)
    cipherfive.set(fiveletters(ciphertext))       
                 
def decrypt(): 
    if len(key.get()) == 0:
        messagebox.showerror("Error", "Key is empty")
    elif len(cipher.get()) == 0:
        messagebox.showerror("Error", "Cipher text is empty")
    ciphertext = cipher.get()
    ciphertext = removeNonASCII(removeSpaces(toUpperCase(ciphertext)))
    plaintextinput = ""
    i=0
    while i<len(ciphertext):
        loc=list()
        loc=locindex(ciphertext[i])
        loc1=list()
        loc1=locindex(ciphertext[i+1])
        if loc[1]==loc1[1]:
            plaintextinput.format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]])
        elif loc[0]==loc1[0]:
            plaintextinput.format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5])  
        else:
            plaintextinput.format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]])   
        i=i+2   
    plain.set(plaintextinput)
    plainfive.set(fiveletters(plaintextinput))     


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

#menghapus semua kotak
def clear():
    key.set("")
    plain.set("")
    cipher.set("")

#keluar dari program
def exit():
    root.destroy()


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
