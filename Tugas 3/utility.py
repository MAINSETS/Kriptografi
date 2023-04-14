from tkinter.filedialog import askopenfile, asksaveasfile, askopenfilename
from SHA_3 import sha3_256 as hash
from RSA import encrypt, decrypt
from tkinter import messagebox

# nanti pindahin ke GUI
def savePublicKeyFile(pub_sign:str):
    '''
    Meminta user untuk menyimpan public key ke file
    content: digital signature
    '''
    f = asksaveasfile(mode='w', title="Save Public Key File", defaultextension=".pub",
                      initialfile="public_key", filetypes=[('Public Key File (*.pub)', '.pub')])
    if(f != ''):
        f.write(pub_sign)
        f.close()
        messagebox.showinfo('Success', 'Penyimpanan file sukses, nyaa~')
    else:
        messagebox.showerror('Cancelled', 'Penyimpanan file dibatalkan, nyaa~')

def savePrivateKeyFile(pri_sign:str):
    '''
    Meminta user untuk menyimpan private key ke file
    content: digital signature
    '''
    f = asksaveasfile(mode='w', title="Save Private Key File", defaultextension=".pri",
                      initialfile="private_key", filetypes=[('Private Key File (*.pri)', '.pri')])
    if(f != ''):
        f.write(pri_sign)
        f.close()
        messagebox.showinfo('Success', 'Penyimpanan file sukses, nyaa~')
    else:
        messagebox.showerror('Cancelled', 'Penyimpanan file dibatalkan, nyaa~')

def openPublicKeyFile():
    '''
    Meminta user membuka file Public Key
    '''
    f = askopenfile(mode='r', title="Open Public Key File", filetypes=[('Public Key File (*.pub)', '.pub')])
    if(f != ''):
        content = f.read()
        f.close()
        return content
    else:
        messagebox.showerror('No File Chosen', 'Tidak ada file yang dipilih, nyaa~')

def openPrivateKeyFile():
    '''
    Meminta user membuka file Private Key
    '''
    f = askopenfile(mode='r', title="Open Private Key File", filetypes=[('Private Key File (*.pri)', '.pri')])
    if(f != ''):
        content = f.read()
        f.close()
        return content
    else:
        messagebox.showerror('No File Chosen', 'Tidak ada file yang dipilih, nyaa~')

def openRandomFile():
    '''
    Meminta user membuka file sembarang.
    return: content
    '''
    filename = askopenfilename(filetypes=[('All files', '*')])
    if(filename != ''):
    # mastiin file dah dipilih oleh user
        f = open(filename, 'rb')
        content = f.read()
        f.close()
        return content

def openTextFile():
    '''
    Meminta user membuka file teks
    return: content
    '''
    filename = askopenfilename(filetypes=[('Text Document (*.txt)', '.txt')])
    if(filename != ''):
        # mastiin file dah dipilih oleh user
        f = open(filename, 'r')
        content = f.read()
        f.close()
        return content

def saveTextFile(signed_content:str):
    f = asksaveasfile(mode='w', title="Save Signed Text File", defaultextension=".txt",
                      initialfile="sign file", filetypes=[('Text Document (*.txt)', '.txt')])
    if(f != ''):
        f.write(signed_content)
        f.close()
        messagebox.showinfo('Success', 'Penyimpanan file sukses, nyaa~')
    else:
        messagebox.showerror('Cancelled', 'Penyimpanan file dibatalkan, nyaa~')

def saveSeperateSignFile(sign:str):
    '''
    langsung minta user simpan filenya
    '''
    f = asksaveasfile(mode='w', title="Save Sign File", defaultextension=".txt",
                      initialfile="sign_file", filetypes=[('Text Document (*.txt)', '.txt')])
    if(f != ''):
        f.write(str(sign))
        f.close()
        messagebox.showinfo('Success', 'Penyimpanan file sukses, nyaa~')
    else:
        messagebox.showerror('Cancelled', 'Penyimpanan file dibatalkan, nyaa~')

def saveCombineSignTextFile(content:str, sign:int):
    '''
    Gabungin sign dengan text file. lalu minta user simpan file
    content: isi file text sebelum
    sign: digital sign
    '''
    # misal user milih satuin sama file
    f = asksaveasfile(mode='w', title="Save Signed File", defaultextension=".txt",
                      initialfile="signed_file", filetypes=[('Text Document (*.txt)', '.txt')])
    signed_content = (content+'\n<ds>'+sign+'</ds>')

    if(f != ''):
        f.write(str(signed_content))
        f.close()
        messagebox.showinfo('Success', 'Penyimpanan file sukses, nyaa~')
    else:
        messagebox.showerror('Cancelled', 'Penyimpanan file dibatalkan, nyaa~')
# batas GUI

def stringtokey(stringkey:str):
    '''
    Mengembalikan nilai key dari key yg dalam bentuk string
    '''
    key_temp = (stringkey.replace(')', '')).split('(')[1]
    k = key_temp.split(', ')[0]
    n = key_temp.split(', ')[1].replace("'", '')
    key = int(k), int(n)
    return key

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


# veritfy
def verifyTextFileSatu(content:str, public_key:any):
    '''
    verify content file text dengan sign satu file. hasil boolean
    '''
    real_content, sign = content.split('\n<ds>')

    # hash dari content yang ada
    real_content_bytes = bytes(real_content, 'utf-8')
    hashed_real_content = hash(real_content_bytes)
    integer_hashed_real = int(hashed_real_content, base=16)

    # hash hasil decrypt
    integer_sign = int(sign.split('</ds>')[0], base=16)
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

    # decrypt ciphertext hash basis 10 yang akan dikomparasi
    sign_hash_int = decrypt(public_key, sign)
        
    return integer_hashed == sign_hash_int

def verifyBinFile(content:bytes, public_key:any, sign:int):
    '''
    verify content file binary dengan sign. hasil boolean
    '''
    hashed_content = hash(content)
    integer_hashed = int(hashed_content, base=16)

    # decrypt ciphertext jadi hash basis 10 yang akan dikomparasi
    sign_hash_int = decrypt(public_key, sign)
        
    return integer_hashed == sign_hash_int




# testing
# stringkey = "b'(220525016522512899534303142402444634969433552519953782316353260664805707605989315073467723341719458240971972670444416460015153041802056018187161130372785305619243274698367607981844763921779553585327, 398784856734535765217641674503699300867202481703020739247738214066550637987314530624634542560596318430743255100500698638884215606885310909068905957843308863996001114056202522143625006787236776812001)'"
# key = stringtokey(stringkey=stringkey)
# print(key[0])
# content, ext = openfile()
# verifyTextFileSatu(content, 212)
# signedtextfile(content, "121",True)

# hash_string = "5fc00e5fbc533059e86f4ee35028613bc7fd464e9784fa121d7f9eec1d365cd3f1ecb8777c8e96f5996d93e17d71da905e0ab8079f0de8f1b936376dfbb593f9a44e275898aa7d6b0635df309b0eb34ec6d0b"
# content = "asasasasasas"
# pub = (24411363138917349115253366043256737150808072465601942568450914620309509606880338886099756808108737217757571688014542018318969078720110171969670193969482212499246923592909678998424386324347034568319, 3416732565075892732980794513890730495883304400261426509329556123158445423905862417385425908111992191663721420014761588105310312955704761495209486025869696379362667078169559887000848792628445755706863)

# a = verifyTextFilePisah(content, pub, int(hash_string, base=16))
# print(a)

# content = "openfdile()"
# content_bytes = bytes(content, 'utf-8')
# hashed = hash(content_bytes)
# a = 15785641256446652689364289986859690500891573079404851263091127852294370159026709122114659233947630230343414854032110328723580338418790204743753341862491084629369245231050789095470786739396201337106255
# b = 50670280738744436300985965835945568054224791438240039364514038636603155979984254396427968419263920676404558394735712553008293842549136151940172121611510522126564271130523176171482665295063758086363731
# private_key = (a, b)
# encrypted = encrypt(private_key, int(hashed, base=16))
# print(content, hashed, int(hashed, base=16), encrypted)