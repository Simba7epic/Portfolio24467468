# file: privacy_preserving_aes.py

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Key generation
key = get_random_bytes(16)  # AES-128
cipher = AES.new(key, AES.MODE_EAX)

# Example message
message = "This is a sensitive message."
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))

# Decrypt
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher_dec.decrypt(ciphertext).decode('utf-8')

print("Original:", message)
print("Encrypted:", base64.b64encode(ciphertext).decode('utf-8'))
print("Decrypted:", plaintext)