class QuoPri():
    def __init__(self, string):
        self.string_orig_list = list(string)
        ascii_string1 = ''.join([chr(i) for i in range(33, 61)])
        ascii_string2 = ''.join([chr(i) for i in range(62, 127)])
        self.ascii_string = ascii_string1 + ascii_string2
        print("可打印的ascii码( '=' 和 ' '  除外): {}".format(len(self.ascii_string)))

    def encode(self):
        string_decode_list = []
        for item in self.string_orig_list:
            if item in self.ascii_string:
                string_decode_list.append(item)
            else:
                item_decode = item.decode()
                item_decode_list = list(item_decode)
                for each in item_decode_list:
                    string_decode_list.append('=' + hex(each)[2:].upper())

        return ''.join(string_decode_list)


if __name__ == '__main__':
    test_string = "=E9=82=A3=E4=BD=A0=E4=B9=9F=E5=BE=88=E6=A3=92=E5=93=A6"
    quopri = QuoPri(test_string)
    result = quopri.decode()
    print("original: {}".format(test_string))
    print("encode: {}".format(result))
