import urllib.parse


def My_url_qute(bian_ma):
    coding = urllib.parse.quote(bian_ma)
    print("编码结果:\n->", coding)


def My_url_unqute(jie_xi):
    parsing = urllib.parse.unquote(jie_xi)
    print("解析结果:\n->", parsing)


def Xun_huan_url(n, content, function):
    m = function(content)
    if 0 != n - 1:
        return Xun_huan_url(n - 1, content, function)
    else:
        return m


def restart_mod():
    print()
    print("      ************************************")
    print("      *     (1)编码模块    (2)解析模块   *")
    print("      ************************************")
    print()
    mod = input("请输入要选择的模块:\n->")
    if mod == "1":
        number = input("请输入要编码的次数:\n->")
        if not number.isdigit():
            judge = input("输入的信息无法识别=_=||\n输入q退出\n    输入其他任意键重新输入:)\n===>")
            if judge == "q":
                exit()
            else:
                restart_mod()
        else:
            content = input("请输入编码内容:\n->")
            Xun_huan_url(int(number), content, My_url_qute)
    elif mod == "2":
        number = input("请输入解析的次数:\n->")
        if not number.isdigit():
            judge = input("输入的信息无法识别=_=||\n输入q退出\n    输入其他任意键重新输入:)\n===>")
            if judge == "q":
                exit()
            else:
                restart_mod()
        else:
            content = input("请输入要解析的内容:\n->")
            Xun_huan_url(int(number), content, My_url_unqute)
    else:
        quit = input('输入的信息无法识别输入q退出=_=||\n输入其他任意键重新输入:)\n===>')
        if quit == "q":
            exit()
        else:
            return restart_mod()


restart_mod()
