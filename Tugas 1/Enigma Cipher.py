def encrypt(plaintext, key1, key2, key3):
    ciphertext = ""
    for char in plaintext:
        char = chr((ord(char) + key1) % 126)
        char = chr((ord(char) + key2) % 126)
        char = chr((ord(char) + key3) % 126)
        ciphertext += char
    return ciphertext

def decrypt(ciphertext, key1, key2, key3):
    plaintext = ""
    for char in ciphertext:
        char = chr((ord(char) - key3 + 126) % 126)
        char = chr((ord(char) - key2 + 126) % 126)
        char = chr((ord(char) - key1 + 126) % 126)
        plaintext += char
    return plaintext

# Testing the Enigma cipher with three rotors
plaintext = "uwaki"
key1 = 5
key2 = 11
key3 = 23

ciphertext = encrypt(plaintext, key1, key2, key3)
print("Ciphertext: ", ciphertext)

decrypted_plaintext = decrypt(ciphertext, key1, key2, key3)
print("Decrypted plaintext: ", decrypted_plaintext)
