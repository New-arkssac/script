import re
import requests
url='''http://123.206.87.240:8002/qiumingshan/'''
s=requests.Session()
requests=s.get(url)
reg=re.search(r'(\d+[+\-*]+(\d+))',requests.text).group()

result=eval(reg)
text={'value':result}
print(s.post(url,data=text).text)




