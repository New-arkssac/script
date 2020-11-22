import hashlib


def md5(str):
    md5 = hashlib.md5()
    md5.update(str.encode('utf8'))
    return md5.hexdigest()


def filehash():
    filename = '/fllllllllllllag'
    cookie_secret = '656d1319-961f-47a8-835c-1116e367ea88'
    print(md5(cookie_secret + md5(filename)))


if __name__ == '__main__':
    filehash()