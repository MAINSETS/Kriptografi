import string
import random

#fungsi mengubah semua text menjadi lower case
def toLowerCase(text):
	return text.lower()

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
    text.lower()
    newtext = ""
    for i in text:
        if i not in string.ascii_lowercase:
            continue
        else:
            newtext = newtext + i
    return newtext

#fungsi menampilkan text dalam kelompok 5 huruf
def fiveletter(text):
    newtext = ""
    count = 0
    for i in text:
        if count%5 == 0:
            newtext = newtext + " "
        newtext = newtext + i
        count = count + 1
    return newtext

#fungsi untuk membuat one-time-key 50000 huruf lowecase ascii secara random
def onetimekey():
    S = 50000
    ran = ''.join(random.choices(string.ascii_lowercase, k = S))
    return ran

#fungsi untuk menyimpan chipertext ke file .txt
def save(text):
    filepath = input("Enter filename: ")
    file = open(filepath, "w")
    file.write(text)
    file.close()


#testing
plaintext = 'Mayo@na1is buKAN insTr3umen'
plaintext = removeNonASCII(removeSpaces(toLowerCase(plaintext)))
#print(plaintext)

chippertext = 'qwertyuiopasdfg'
chippertext = fiveletter(chippertext)
#print(chippertext)

#save(plaintext)
#print(onetimekey())


