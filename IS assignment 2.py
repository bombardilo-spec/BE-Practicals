# Transposition Cipher - Columnar Technique

def encrypt(plaintext, key):
    #Encrypts the plaintext using Columnar Transposition based on key length.
    
    # Remove spaces and convert to uppercase (optional based on requirement)
    plaintext = plaintext.replace(" ", "")
    
    # Calculate the number of columns = key
    col = key
    # Calculate the number of rows needed
    row = -(-len(plaintext) // col)  # Ceiling division

    # Padding with 'X' if plaintext doesn't fill the entire matrix
    padding = (col * row) - len(plaintext)
    plaintext += 'X' * padding

    # Create the matrix row-wise
    matrix = [plaintext[i:i+col] for i in range(0, len(plaintext), col)]

    # Read column-wise to generate ciphertext
    ciphertext = ""
    for i in range(col):
        for r in matrix:
            ciphertext += r[i]
    
    return ciphertext

def decrypt(ciphertext, key):
    """
    Decrypts the ciphertext using Columnar Transposition based on key length.
    """
    col = key
    row = -(-len(ciphertext) // col)  # Should be exact if padded during encryption

    # Create an empty matrix for decryption
    matrix = [''] * row

    # Fill the matrix column-wise
    k = 0
    for i in range(col):
        for j in range(row):
            matrix[j] += ciphertext[k]
            k += 1

    # Combine the matrix row-wise to get plaintext
    plaintext = ''.join(matrix)

    # Remove padding if any
    return plaintext.rstrip('X')

# Example usage:
message = "HELLO WORLD"
key = 4

# Encrypt the message
cipher = encrypt(message, key)
print("Encrypted:", cipher)

# Decrypt the message
plain = decrypt(cipher, key)
print("Decrypted:", plain)
