from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to perform DES Encryption
def des_encrypt(plaintext, key):
    """
    Encrypts the plaintext using DES algorithm with the given key.
    """
    # Create a DES cipher object in ECB mode
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Convert plaintext to bytes and pad it to match DES block size (8 bytes)
    padded_text = pad(plaintext.encode(), DES.block_size)

    # Encrypt the padded plaintext
    ciphertext = cipher.encrypt(padded_text)

    return ciphertext

# Function to perform DES Decryption
def des_decrypt(ciphertext, key):
    """
    Decrypts the ciphertext using DES algorithm with the given key.
    """
    # Create a DES cipher object in ECB mode
    cipher = DES.new(key, DES.MODE_ECB)

    # Decrypt and then unpad the plaintext
    decrypted_padded_text = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_padded_text, DES.block_size)

    return plaintext.decode()

# Main code execution
if __name__ == "__main__":
    # Plaintext to be encrypted
    plaintext = "HelloWorld"

    # DES key must be exactly 8 bytes long
    key = b'8bytekey'  # Example: b'8bytekey'

    # Encrypt the plaintext
    encrypted = des_encrypt(plaintext, key)
    print("Encrypted (Hex):", encrypted.hex())

    # Decrypt the ciphertext
    decrypted = des_decrypt(encrypted, key)
    print("Decrypted:", decrypted)
