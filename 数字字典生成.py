txtName = "D://笔记//数字字典.txt"
f = open(txtName, "a+")

for i in range(1, 10001):

    new_context = str(i) + '\n'
    f.write(new_context)
f.close()