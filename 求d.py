from Crypto.PublicKey import RSA
import sys
p = 473398607161
q = 4511491
e = 17
n = (p - 1) * (q - 1)
i = 0
# 17x + ny = 1
while True:
    if ((1 - n * i) % e == 0):
        break
    i -= 1
print('%d' % ((1 - n * i) // e))
