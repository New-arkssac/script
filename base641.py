# coding:utf-8
import base64


def My_base64_encode(jia_mi): #转码模块
    jia_mi = jia_mi.encode('utf-8')
    zhuan_ma = base64.b64encode(jia_mi) #utf-8转换成base64编码
    print("结果:\n", zhuan_ma.decode())
    return zhuan_ma.decode()


def My_base64_decode(jie_ma):
    jie_xi = base64.b64decode(jie_ma)
    print("转码结果:\n" + jie_xi.decode())
    return jie_xi.decode()


def My_mod():
    print()
    print("     ****************************************")
    print("     *    (1)转码模块        (2)解析模块    *")
    print("     ****************************************")
    print()
    num = input("请你选择你要使用的模块:\n")
    if (num == "1"):

        def restart1():
            print()
            print("    ***********************************")
            print("    *   (1)转码1次       (2)转码2次   *")
            print("    *   (3)转码3次       (4)转码4次   *")
            print("    ***********************************")
            print
            num1 = input("请你选择要转码的次数: \n")
            if (num1 == "1"):
                input_str1 = input("请输入你要转码的内容: \n")
                My_base64_encode(input_str1)
            elif (num1 == "2"):
                input_str2 = input("请输入你要转码的内容: \n")
                one = My_base64_encode(input_str2) #第一次转码
                My_base64_encode(one) #第二次转码
            elif (num1 == "3"):
                input_str3 = input("请输入你要转码的内容: \n")
                one = My_base64_encode(input_str3) #第一次转码
                two = My_base64_encode(one) #第二次转码
                My_base64_encode(two) #第三次转码
            elif (num1 == "4"):
                input_str4 = input("请输入你要转码的内容: \n")
                one = My_base64_encode(input_str4) #第一次转码
                two = My_base64_encode(one) #第二次转码
                three = My_base64_encode(two) #第三次转码
                My_base64_encode(three) #第四次转码
            else:
                quit = input('输入的信息无法识别输入q退出=_=||\n输入其他任意键重新输入:)\n:')
                if (quit == "q"):
                    exit()
                else:
                    restart1()

        restart1()
    elif (num == "2"):

        def restart():
            print()
            print("    *************************************")
            print("    *   (1)解析1次         (2)解析2次   *")
            print("    *   (3)解析3次         (4)解析4次   *")
            print("    *************************************")
            print()
            num2 = input("请输入你要解析的次数: \n")
            if (num2 == "1"):
                input_str1 = input("请输入你要解析的内容: \n")
                My_base64_decode(input_str1)
            elif (num2 == "2"):
                input_str2 = input("请输入你要解析的内容: \n")
                one = My_base64_decode(input_str2)
                My_base64_decode(one)
            elif (num2 == "3"):
                input_str3 = input("请输入你要解析的内容: \n")
                one = My_base64_decode(input_str3)
                two = My_base64_decode(one)
                My_base64_decode(two)
            elif (num2 == "4"):
                input_str4 = input("请输入你要解析的内容: \n")
                one = My_base64_decode(input_str4)
                two = My_base64_decode(one)
                three = My_base64_decode(two)
                My_base64_decode(three)
            else:
                quit = input('输入的信息无法识别输入q退出=_=||\n输入其他任意键重新输入:)\n:')
                if (quit == "q"):
                    exit()
                else:
                    restart()

        restart()

    else:
        quit = input('输入的信息无法识别输入q退出=_=||\n输入其他任意键重新输入:)\n:')
        if (quit == "q"):
            exit()
        else:
            My_mod()


if __name__ == "__main__":

    My_mod()
