import random
from math import gcd
from Crypto.Util.number import isPrime, inverse

# program ini hanya menerima dan mengeluarkan bilangan bulat
def totient(p, q):
    return (p-1)*(q-1)

def generate_prime_number():
    while True:
        p = random.randint(10**50, 10**100)
        if isPrime(p):
            return p

def generate_key_pair(p, q):
    n = p * q
    m = totient(p, q)

    while True:
        e = random.randint(1, m-1)
        if gcd(e, m) == 1:
            break
    d = inverse(e, m)
    return (e, n), (d, n)

def encrypt(public_key, plaintext):
    key, n = public_key
    cipher = pow(plaintext, key, n)
    return cipher

def decrypt(private_key, ciphertext):
    key, n = private_key
    plain = pow(ciphertext, key, n)
    return plain

def encypttext(public_key, plaintext):
    key, n = public_key
    cipher = pow(plaintext, key, n)
    return cipher


#testing
if __name__ == '__main__':
    print("Prime number for p: ", generate_prime_number()) #untuk nilai p
    print("Prime number for q: ", generate_prime_number()) #untuk nilai q
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))

    public_key, private_key = generate_key_pair(p, q)

    print("Public key: ", public_key)
    print("Private key: ", private_key)
    print("m: ", (p-1) * (q-1))
    print("n: ", public_key[1])
    print("e: ", public_key[0])
    print("d: ", private_key[0])

    message = (input("Enter a number to encrypt: "))
    ciphertext = encrypt(public_key, message)
    print("Encrypted message: ", ciphertext)

    plaintext = decrypt(private_key, ciphertext)
    print("Decrypted message:  ", plaintext)
