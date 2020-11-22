import base64
str = '555.png'
st = bytes(str, 'utf-8')
jm = base64.b64encode(st)
print(jm)
