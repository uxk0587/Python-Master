"""
读写JSON文件
author: Jack Lee
time: 2020/4/13 20:41

"""

import json
# json.dump 序列化：直接将python对象（字典）写入json文件
def write_data_to_json():
    mydict = {
        'name': 'Jack',
        'age': 22,
        'qq': None,
        'friends': ['Pony', 'Mask'],
        'cars': [{'brand': 'Tesla', 'max_speed': 240},
                 {'brand': 'Audi', 'max_speed': 200},
                 {'brand': 'Benz', 'max_speed': 220}
                 ]
    }

    try:
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(mydict, f)
    except IOError as e:
        print(e)
    print('Finish Saving the data')

#  json.load，将文件中数据反序列化为对象(字典）, json.load针对文件句柄
def read_json():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            py_object=  json.load(f) # 注意load和loads的用法区别， 前者直接将文件对象转换为字典，后者要读取json内部的字符串
            print(type(py_object)) # <class 'dict'>
    except IOError as e:
        print(e)
    print("Read JSON Finished")


# 用json.dumps 序列化：将Python对象序列化处理成JSON格式的字符串，再写入JSON文件
def write_pyobject_to_json():
    mydict1 = {'name': 'Jack',
               'age': '22'}
    try:
        with open('data1.json', 'w', encoding='utf-8') as f:
            # 将python对象序列化为JSON格式字符串
            json_string = json.dumps(mydict1) # dumps中的s可看为string
            print(json_string)
            print(type(json_string)) # <class 'str'>
            f.write(json_string) #将字符串写入JSON文件
    except IOError as e:
        print(e)
    print("Write list to JSON string Finished")

# 用json.loads 反序列化：将JSON字符串内容反序列成Python对象; json.load针对内存对象
def read_jsonstr_to_pyobject():
    try:
        with open('data1.json', 'r', encoding='utf-8') as f:
            """
            print(type(f.read())) # JSON字符串
            """
            # 将字符串反序列化伟python对象（字典）
            py_object = json.loads(f.read())  #loads的s可看作string
            print(type(py_object))
            print(py_object)
    except IOError as e:
        print(e)
    print("Read JSON String to Python Object Finished!")


if __name__ == '__main__':
    write_data_to_json()
    read_json()
    write_pyobject_to_json()
    read_jsonstr_to_pyobject()
