cipher = input("请输入你要解密的内容:\n")
index = 0
for num in range(5, len(cipher) + 5):
    temp = ""
    for i in cipher:
        temp += chr(ord(i) + num)

    print(temp[index], end="")
    index += 1
