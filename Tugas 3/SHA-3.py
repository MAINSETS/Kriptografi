import hashlib

def sha3_256(data):
    hash_object = hashlib.sha3_256()
    hash_object.update(data)
    return hash_object.hexdigest()

def sha3_512(data):
    hash_object = hashlib.sha3_512()
    hash_object.update(data)
    return hash_object.hexdigest()

data = b'Hello, world!'
sha3_256_hash = sha3_256(data)
sha3_512_hash = sha3_512(data)

print(f"SHA3-256 hash: {sha3_256_hash}")
print(f"SHA3-512 hash: {sha3_512_hash}")
