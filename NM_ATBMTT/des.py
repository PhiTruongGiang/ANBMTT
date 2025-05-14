from Crypto.Cipher import DES
import os

def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text

def encrypt_file(file_data, key):
    key = key.ljust(8, '0')[:8].encode()  # Đảm bảo key 8 byte
    des = DES.new(key, DES.MODE_ECB)
    padded_data = pad(file_data)
    return des.encrypt(padded_data)

def decrypt_file(file_data, key):
    key = key.ljust(8, '0')[:8].encode()
    des = DES.new(key, DES.MODE_ECB)
    decrypted = des.decrypt(file_data)
    return decrypted.rstrip(b' ')
