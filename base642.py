import base64


def My_base64_encode(jia_mi):  #转码模块
    jia_mi = jia_mi.encode('utf-8')
    zhuan_ma = base64.b64encode(jia_mi)  #utf-8转换成base64编码
    zhuan_ma.decode()
    return zhuan_ma.decode()


def My_base64_decode(jie_ma):
    jie_xi = base64.b64decode(jie_ma)
    jie_xi.decode()
    return jie_xi.decode()


def Xun_huan_base64(n, nei_rong, hanshu):
    zhuan_ma = hanshu(nei_rong)
    if 0 != n - 1:
        return Xun_huan_base64(n - 1, zhuan_ma, hanshu)
    else:
        return zhuan_ma


def for_xun_huan(n, contento, main):
    for i in range(n):
        contento = main(contento)
        print("运行结果%d:\n%s" % (i + 1, contento))
    return contento


def restart_mod():
    print("   *********************************")
    print("   *   Welcome to the base64 Mod   *")
    print("   *********************************")
    print("   *   (1)编码模块   (2)解析模块   *")
    print("   *********************************")
    print()
    mod = input("请输入要选择的模块:\n->")
    if mod == "1":
        number = input("请输入要编码的次数:\n->")
        if not number.isdigit():
            judge = input("输入的信息无法识别=_=||\n输入q退出\n输入其他任意键重新输入:)\n->")
            if judge == "q":
                exit()
            else:
                restart_mod()
        else:
            content = input("请输入编码内容:\n->")
            for_xun_huan(int(number), content, My_base64_encode)
    elif mod == "2":
        number = input("请输入解析的次数:\n->")
        if not number.isdigit():
            judge = input("输入的信息无法识别=_=||\n输入q退出\n输入其他任意键重新输入:)\n->")
            if judge == "q":
                exit()
            else:
                restart_mod()

        else:
            content = input("请输入要解析的内容:\n->")
            for_xun_huan(int(number), content, My_base64_decode)
    else:
        quit = input('输入的信息无法识别输入q退出=_=||\n输入其他任意键重新输入:)\n->')
        if (quit == "q"):
            exit()
        else:
            return restart_mod()


if __name__ == "__main__":
    restart_mod()
