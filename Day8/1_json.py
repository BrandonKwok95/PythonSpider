import json
# json数据格式
# i.    不可以写注释
# ii.   名值对形式，利用双引号
# iii.  末尾无逗号

# 四个基本方法

# 1.字符串和字典列表交互
# loads和dumps
data = '[{"name":"zhang","gender":"male"},{"name":"wang","gender":"female"}]'
# loads使字符串转换成列表
list_data = json.loads(data)
print(list_data)
print(type(list_data))
# dumps将列表转为字符串形式
str_data = json.dumps(list_data)
print(str_data)
print(type(str_data))


print('*************')
# 2.文件对象和dict_list转换
# dump将列表直接写入文件
json.dump(str_data,open("1.json","w",encoding="utf-8"))
# load读取文件
file = open('1.json','r')
load_data = json.load(file)
print(load_data)
print(type(load_data))