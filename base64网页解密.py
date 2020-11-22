import requests
import base64

url = input("请你输入要解析的网页的url:")

r = requests.session()
headers = r.get(url).headers

mid = base64.b64decode(headers['flag'])
mid = mid.decode()

flag = base64.b64decode((mid.split(":")[1]))
data = {"margin": flag}
print(r.post(url, data).text)
