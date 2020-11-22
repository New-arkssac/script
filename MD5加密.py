#!/usr/bin/python3.8
# encoding:utf-8
import hashlib


def str_md5(jia_mi):
    jia = hashlib.md5()
    jia.update(jia_mi.encode("utf-8"))
    return jia.hexdigest()


def xun_huan(n, content, main):
    zhuan_ma = main(content)
    if 0 != n - 1:
        return xun_huan(n - 1, zhuan_ma, main)
    else:
        return zhuan_ma


def for_xun_huan(i, content, main):
    for n in range(i):
        content = main(content)
        print(("加密结果%d:\n%s" % (n + 1, content)))
    return content


def main():
    print("    ********************************")
    print("    *    Welcome to the md5 Mod    *")
    print("    ********************************")
    number = input("请输入你要加密的次数\n->")
    if not number.lstrip():
        judge = input("输入的信息无法识别=_=||\n输入q退出\n输入其他任意键重新输入:)\n->")
        if judge == "q":
            exit()
        else:
            main()
    else:
        content = input("请输入你要加密的内容\n->")
        for_xun_huan(int(number), content, str_md5)


if __name__ == "__main__":
    main()
