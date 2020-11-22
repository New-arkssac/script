import rsa
import base64
from Crypto.PublicKey import RSA
# RSA加密解密

pubkey = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCcB4zYqi3mjdP3E2f9jyPuF0Xm
N2W9IMymWy7+M/U9c5fYy+/C5s3FIyPoiajg2LPSFccWhPtwRjMmK020r8XRg2BU
dzQEUod0nvrnqfPrrpbgyuCT2Ldw/cAQuVcmkCRmS5ZHpEzPMG4jF/QgOZYrXzCR
TrrOIaoy9uGDe2OsqwIDAQAB
-----END PUBLIC KEY-----'''

privatekey = '''-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQCcB4zYqi3mjdP3E2f9jyPuF0XmN2W9IMymWy7+M/U9c5fYy+/C
5s3FIyPoiajg2LPSFccWhPtwRjMmK020r8XRg2BUdzQEUod0nvrnqfPrrpbgyuCT
2Ldw/cAQuVcmkCRmS5ZHpEzPMG4jF/QgOZYrXzCRTrrOIaoy9uGDe2OsqwIDAQAB
AoGATE8U/1IbqMpshEYlccjz1ZnkQbeONnU4IZQu43wd0LQb65ex5yxiLqwE/9Fz
mqPhLjogaE8ZecubcGt1UY01vYJ1XhSfW5lTfqdNY7ijMSOUdAC/bJWQS/cJFBAI
1aOoPneXnHAHwIBYQdVKosVeckIH2ZoLo87fFlZxC4Js3IECQQDKYmKUPOciVC2r
BMAoHRfcvNqirOTSanWYhrDL1A8z4xNyCKajYXDDmgK+6yryqBzj0lmL6AmCLLlB
Hem6Ohb7AkEAxV1mxMt4nkTI7WluSbcOjNTBheDU6DsD1cTV1tqNPrAqoOSHCFye
3RaPnFBckLA1Q1ihPQv45ucmaL3+fbeSEQJAV7YKCTrX5U3cOPknGnt5YwZKLySF
SxgufPsq1jvClvc77zkGl1pcl7lApWOgSmhHlQkOHA9lR5CAfVMsf7Q7TwJADUTI
QfbD9y/8qilqZr5N1h3/nLaO2cYN7fM7xSQQVuSVGRgEFAXWEFsR8JpefsO58Psm
a+pAI5XquSP81grfYQJBALEX2i0W0en59klTWB4xacNoMexFAJNaWO2ts8iylZtd
jQYMIbFu02rFBsNJnSllWvyoj1zg1MsaTDo7tcrvZPc=
-----END RSA PRIVATE KEY-----'''


# 加密
def to_para(plain):
    rsa_privkey = RSA.importKey(privatekey)
    x = rsa.encrypt(plain.encode(), rsa_privkey)
    return base64.b64encode(x).decode()


# 解密
def to_decrypt(plain):
    rsa_privkey = RSA.importKey(privatekey)
    x = rsa.decrypt(base64.b64decode(plain), rsa_privkey)
    return x.decode()


if __name__ == '__main__':
    jiami = to_para('洁哥天下第一')
    print(jiami)
    jiemi = to_decrypt(jiami)
    print(jiemi)
