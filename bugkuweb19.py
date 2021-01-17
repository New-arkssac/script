import requests
import base64

url = input('请输入url：')
push = requests.Session()
headers = push.get(url).headers

str1 = base64.b64decode(headers['flag'])
print(str1)
flag = base64.b64decode(repr(str1).split(':')[1])
print(flag)

data1 = {'margin': flag}
r = push.post(url=url, data=data1)
print(r.text)
