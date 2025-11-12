from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to encrypt plaintext using AES
def aes_encrypt(plaintext, key):
    """
    Encrypts the given plaintext using AES encryption with CBC mode.
    """
    # Generate a random 16-byte IV (Initialization Vector)
    iv = get_random_bytes(16)

    # Create AES cipher object using key and IV in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Pad the plaintext to be multiple of AES block size (16 bytes)
    padded_text = pad(plaintext.encode(), AES.block_size)

    # Encrypt the padded plaintext
    ciphertext = cipher.encrypt(padded_text)

    # Return the IV and ciphertext (IV is needed for decryption)
    return iv, ciphertext

# Function to decrypt ciphertext using AES
def aes_decrypt(iv, ciphertext, key):
    """
    Decrypts the given ciphertext using AES decryption with CBC mode.
    """
    # Create AES cipher object again with the same key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the ciphertext
    decrypted_padded_text = cipher.decrypt(ciphertext)

    # Unpad the decrypted plaintext
    plaintext = unpad(decrypted_padded_text, AES.block_size)

    return plaintext.decode()

# Main program
if __name__ == "__main__":
    # Example plaintext message
    plaintext = "Hello World - AES Example"

    # AES key must be 16, 24, or 32 bytes long. Let's use 16 bytes here.
    key = b'ThisIsA16ByteKey'  # 128-bit key

    # Encrypt the message
    iv, encrypted = aes_encrypt(plaintext, key)
    print("Encrypted (hex):", encrypted.hex())
    print("IV (hex):", iv.hex())

    # Decrypt the message
    decrypted = aes_decrypt(iv, encrypted, key)
    print("Decrypted message:", decrypted)
