from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Step 1: Generate RSA key pair (public and private keys)
key = RSA.generate(2048)  # Generate a 2048-bit key

private_key = key.export_key()  # Export private key in PEM format
public_key = key.publickey().export_key()  # Export public key in PEM format

print("Generated RSA Public Key:")
print(public_key.decode())

print("\nGenerated RSA Private Key:")
print(private_key.decode())

# Step 2: Create cipher object using public key for encryption
rsa_public_key = RSA.import_key(public_key)
cipher_rsa_encrypt = PKCS1_OAEP.new(rsa_public_key)

# Step 3: Encrypt a message
message = "Hello RSA Encryption"
ciphertext = cipher_rsa_encrypt.encrypt(message.encode())
print("\nEncrypted Message (hex):", ciphertext.hex())

# Step 4: Create cipher object using private key for decryption
rsa_private_key = RSA.import_key(private_key)
cipher_rsa_decrypt = PKCS1_OAEP.new(rsa_private_key)

# Step 5: Decrypt the message
decrypted_message = cipher_rsa_decrypt.decrypt(ciphertext)
print("\nDecrypted Message:", decrypted_message.decode())
