import hashlib
import base64


def md5_m(data):
    md5 = hashlib.md5()
    md5.update(data.encode("utf-8"))
    return md5.hexdigest()


def flag(data, content):
    m = data
    m_len = len(m)
    m_str = content
    m_str = base64.b64decode(m_str).decode()
    m_str_len = len(m_str)
    x = 0
    char = ""
    m_str_data = []
    f = ""
    for i in range(m_str_len):
        if x == m_len:
            x = 0
        chr1 = m[x]
        char += chr1
        x += 1
    for a in range(m_str_len):
        s = ord(m_str[a])
        m_str_data.append(chr(s))
    for s in range(m_str_len):
        a = (ord(m_str[s]) - ord(char[s])) % 128
        if a < 0:
            f += chr(a + 128)
        else:
            f += chr(a)
    print(m)
    print(char)
    print(f)


v = input("请输入要加密的md5:")
z = input("请输入密文:")
flag(md5_m(v), z)
