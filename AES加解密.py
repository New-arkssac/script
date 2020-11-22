from binascii import b2a_base64, a2b_base64
from Crypto.Cipher import AES
import random
import string


class AES_CBC():
    def __init__(self):
        key = ''.join(random.sample(string.ascii_letters + string.digits, 16))
        iv = ''.join(random.sample(string.ascii_letters + string.digits, 16))
        self.key = bytes(key, encoding='utf-8')
        self.iv = bytes(iv, encoding='utf-8')
        print(key)
        print(iv)
    
    # 加密。text:需要加密的内容
    def encrypt(self, text):
        cryptor = AES.new(self.key, AES.MODE_CBC, self.iv)
        bs = 16
        length = len(text)
        bytes_length = len(bytes(text, encoding='utf-8'))
        # tips：utf-8编码时，英文占1个byte，而中文占3个byte
        padding_size = length if (bytes_length == length) else bytes_length
        padding = bs - padding_size % bs
        # tips：chr(padding)看与其它语言的约定，有的会使用'\0'
        padding_text = chr(padding) * padding
        text = text + padding_text
        ciphertext = cryptor.encrypt(bytes(text, encoding='utf-8'))
        return b2a_base64(ciphertext)

    # 解密
    def decrypt(self, content):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        encrypt_bytes = a2b_base64(content)
        decrypt_bytes = cipher.decrypt(encrypt_bytes)
        text = str(decrypt_bytes, encoding='utf-8')
        length = len(text)
        unpadding = ord(text[length - 1])
        return text[0:length - unpadding]


a = AES_CBC()
jami = a.encrypt('洁哥天下第一')
print(jami)
jiemi = a.decrypt(jami)
print(jiemi)


