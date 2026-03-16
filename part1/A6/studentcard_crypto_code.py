from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# AES key must be 16, 24, or 32 bytes long
key = b'Sixteen byte key'  # 16 bytes
data = b'StudentID:24467468'

# Create cipher object
cipher = AES.new(key, AES.MODE_CBC)
ct_bytes = cipher.encrypt(pad(data, AES.block_size))

print("Encrypted:", ct_bytes)

# To decrypt
decipher = AES.new(key, AES.MODE_CBC, iv=cipher.iv)
pt = unpad(decipher.decrypt(ct_bytes), AES.block_size)
print("Decrypted:", pt)