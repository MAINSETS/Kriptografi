from tkinter.filedialog import askopenfile, asksaveasfile, askopenfilename
from SHA_3 import sha3_256 as hash
from RSA import encrypt, decrypt
from tkinter import messagebox

# nanti pindahin ke GUI
def savefilesign(sign:str):
    '''
    Meminta user untuk menyimpan digital signature
    content: digital signature
    '''
    f = asksaveasfile(mode='w', title="Save sign file", defaultextension=".digsi",
                      initialfile="sign file", filetypes=[('Digital sign file', '.digsi')])
    sign = str(sign)
    if(f is not None):
        f.write(sign)
        f.close()
        messagebox.showinfo('Success', 'Penyimpanan file sukses, nyaa~')
    else:
        messagebox.showerror('Cancelled', 'Penyimpanan file dibatalkan, nyaa~')

def openfilesign():
    '''
    Meminta user membuka file digital signature
    '''
    f = askopenfile(mode='r', title="Open sign file", filetypes=[('Digital sign file', '.digsi')])
    if(f is not None):
        content = f.read()
        f.close()
        return content
    else:
        messagebox.showerror('No File Chosen', 'Tidak ada file yang dipilih, nyaa~')

def openfile():
    '''
    Meminta user membuka file sembarang.
    return content
    '''
    filename = askopenfilename(filetypes=[('All files', '*')])
    if(filename is not None):
    # mastiin file dah dipilih oleh user
        ext = filename.split('.')[1]
        if(ext == 'txt'):
            #file text
            f = open(filename, 'r')
            content = f.read()
            f.close()
        else:
            #file sembarang
            f = open(filename, 'rb')
            content = f.read()
            f.close()
    return content, ext

def stringtokey(stringkey:str):
    '''
    Mengembalikan nilai key dari key yg dalam bentuk string
    '''
    key_temp = (stringkey.replace(')', '')).split('(')[1]
    k = key_temp.split(', ')[0]
    n = key_temp.split(', ')[1].replace("'", '')
    key = int(k), int(n)
    return key


def combineSignTextFile(content:str, sign:int):
    '''
    Gabungin sign dengan text file. hasilnya signed_content
    content: isi file text sebelum
    sign: digital sign
    '''
    # misal user milih satuin sama file
    signed_content = (content+'\n<ds>'+sign+'</ds>')
    return signed_content

# batas GUI

def signtextfile(content:str, private_key:any):
    '''
    sign document, return hasil encrypt intinya ngehasilin tanda tangan (sign)
    '''
    content_bytes = bytes(content, 'utf-8')
    hashed_content = hash(content_bytes)
    integer_hashed = int(hashed_content, base=16)
    return encrypt(private_key, integer_hashed)

def signrandomfile(content:bytes, private_key:any):
    '''
    sign document sembarang. return hasil encrypt
    '''
    hashed_content = hash(content)
    integer_hashed = int(hashed_content, base=16)
    return encrypt(private_key, integer_hashed)

def verifyTextFileSatu(content:str, public_key:any):
    '''
    verify content file text dengan sign satu file. hasil boolean
    '''
    real_content, pre_sign = content.split('\n<ds>')

    # hash dari content yang ada
    real_content_bytes = bytes(real_content, 'utf-8')
    hashed_real_content = hash(real_content_bytes)
    integer_hashed_real = int(hashed_real_content, base=16)

    # hash hasil decrypt
    integer_sign = int(pre_sign.split('</ds>')[0])
    integer_decrypt_sign = decrypt(public_key, integer_sign)
        
    return integer_hashed_real == integer_decrypt_sign

def verifyTextFilePisah(content:str, public_key:any, sign:int):
    '''
    verify content file text dengan sign yang beda file. hasil boolean
    '''
    # hash dari content yang ada
    content_bytes = bytes(content, 'utf-8')
    hashed_content = hash(content_bytes)
    integer_hashed = int(hashed_content, base=16)

    # decrypt ciphertext jadi hash yang akan dikomparasi
    sign_hash = decrypt(public_key, sign)
        
    return integer_hashed == sign_hash




# testing
# stringkey = "b'(220525016522512899534303142402444634969433552519953782316353260664805707605989315073467723341719458240971972670444416460015153041802056018187161130372785305619243274698367607981844763921779553585327, 398784856734535765217641674503699300867202481703020739247738214066550637987314530624634542560596318430743255100500698638884215606885310909068905957843308863996001114056202522143625006787236776812001)'"
# key = stringtokey(stringkey=stringkey)
# print(key[0])
# content, ext = openfile()
# verifyTextFileSatu(content, 212)
# signedtextfile(content, "121",True)

# content = "openfdile()"
# content_bytes = bytes(content, 'utf-8')
# hashed = hash(content_bytes)
# a = 15785641256446652689364289986859690500891573079404851263091127852294370159026709122114659233947630230343414854032110328723580338418790204743753341862491084629369245231050789095470786739396201337106255
# b = 50670280738744436300985965835945568054224791438240039364514038636603155979984254396427968419263920676404558394735712553008293842549136151940172121611510522126564271130523176171482665295063758086363731
# private_key = (a, b)
# encrypted = encrypt(private_key, int(hashed, base=16))
# print(content, hashed, int(hashed, base=16), encrypted)