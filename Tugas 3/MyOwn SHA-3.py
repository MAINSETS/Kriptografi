# Import libraries
import binascii

# Define SHA-3 constants
R = 1088
c = 512
b = 1600 - R
nr = 24

# Define SHA-3 state
state = [0] * 25

# Define SHA-3 round constants
round_constants = [0x0000000000000001, 0x0000000000008082, 0x800000000000808A, 0x8000000080008000, 0x000000000000808B, 0x0000000080000001, 0x8000000080008081, 0x8000000000008009, 0x000000000000008A, 0x0000000000000088, 0x0000000080008009, 0x000000008000000A, 0x000000008000808B, 0x800000000000008B, 0x8000000000008089, 0x8000000000008003, 0x8000000000008002, 0x8000000000000080, 0x000000000000800A, 0x800000008000000A, 0x8000000080008081, 0x8000000000008080, 0x0000000080000001, 0x8000000080008008]

# Define SHA-3 rotation offsets
rotation_offsets = [0, 36, 3, 41, 18, 1, 44, 10, 45, 2, 6, 43, 15, 61, 28, 55, 25, 21, 56, 27, 20, 39, 8, 14, 62, 18, 39, 61, 1, 6, 25, 8, 28, 55, 24, 27, 14, 10, 3, 43, 9, 45, 2, 41, 29, 56, 44, 62, 52, 30, 40, 51, 46, 12, 15, 35, 47, 34, 33, 16, 22, 38, 19, 32, 37, 50, 48, 13, 7, 54, 63, 26, 17, 31, 23, 58, 42, 60, 57, 49]

# Define SHA-3 bit rotation function
def rotate_left(x, n):
    return ((x << n) | (x >> (64 - n))) & 0xFFFFFFFFFFFFFFFF

# Define SHA-3 theta step function
def theta_step(a, b, c, d, e):
    C = [0] * 5
    D = [0] * 5
    for i in range(5):
        C[i] = state[a + i] ^ state[b + i] ^ state[c + i] ^ state[d + i] ^ state[e + i]
    for i in range(5):
        D[i] = C[(i + 4) % 5] ^ rotate_left(C[(i + 1) % 5], 1)
    for i in range(5):
        for j in range(5):
            state[a + i + 5 * j] ^= D[i]

# Define SHA-3 rho and pi steps function
def rho_and_pi_steps():
    for i in range(25):
        state[i] = rotate_left(state[i], rotation_offsets[i])

# Define SHA-3 chi step function
def chi_step():
    for j in range(5):
        for i in range(5):
            state[i + 5 * j] ^= (~state[(i + 1) % 5 + 5 * j]) & state[(i + 2) % 5 + 5 * j]

# Define SHA-3 iota step function
def iota_step(round):
    state[0] ^= round_constants[round]

# Define SHA-3 initialization function
def initialize_state():
    for i in range(25):
        state[i] = 0

# Define SHA-3 permutation function
def permute():
    for round in range(nr):
        theta_step(0, 1, 2, 3, 4)
        rho_and_pi_steps()
        chi_step()
        iota_step(round)

# Define SHA-3 message padding function
def pad_message(message):
    message_length = len(message)
    message += b'\x06'
    message += b'\x80'
    message += b'\x00' * ((-message_length - 2) % 136)
    message += (message_length * 8).to_bytes(16, byteorder='big')
    return message

# Define SHA-3 message absorption function
def absorb(message):
    for i in range(0, len(message), 136):
        for j in range(17):
            state[j] ^= int.from_bytes(message[i + 8 * j:i + 8 * j + 8], byteorder='little')
        permute()

# Define SHA-3 squeeze function
def squeeze(output_length):
    output = b''
    while len(output) < output_length:
        output += int.to_bytes(state[0], 8, byteorder='little')
        state[0] = rotate_left(state[0], 1)
        permute()
    return output[:output_length]

# Define SHA-3 hash function
def sha3(message, output_length=256):
    initialize_state()
    absorb(pad_message(message))
    return squeeze(output_length // 8)

# Define SHA-3 hash function
def sha3_256(message):
    return sha3(message, 256)

# Define SHA-3 hash function
def sha3_512(message):
    return sha3(message, 512)

# Define main function
def main():
    # Get message from user
    message = input('Enter message: ').encode()
    message1 = input('Enter message: ').encode()
    # Compute SHA-3-256 hash
    hash = sha3_256(message)
    hash1 = sha3_512(message1)
    # Print SHA-3-256 hash
    print('SHA-3-256 hash: ' + binascii.hexlify(hash).decode())
    print('SHA-3-512 hash: ' + binascii.hexlify(hash1).decode())
    
#test
main()





