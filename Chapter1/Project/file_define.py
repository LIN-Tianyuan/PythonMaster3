from data_define import Record

import json

# 文件类
class FileReader:
    def read_data(self):
        pass

class TextFileReader(FileReader):
    def __init__(self, path):
        # 文件的路径
        self.path = path

    def read_data(self):
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            # 去除行末的换行符
            line = line.strip()
            # 把每行文本通过逗号分隔转换成列表，得到date, order_id, money, province
            data_list = line.split(",")
            # 创造record对象
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list

class JsonFileReader(FileReader):
    def __init__(self, path):
        # 文件的路径
        self.path = path

    def read_data(self):
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            # 创造record对象
            record = Record(data_dict["date"], data_dict["order_id"], data_dict["money"], data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list

if __name__ == "__main__":
    text_file_reader = TextFileReader("January2023SalesData.txt")
    json_file_reader = JsonFileReader("February2023SalesData.txt")
    data_list1 = text_file_reader.read_data()
    data_list2 = json_file_reader.read_data()
    for i in data_list1:
        print(i)

    for i in data_list2:
        print(i)