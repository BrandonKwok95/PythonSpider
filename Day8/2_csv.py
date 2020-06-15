# csv表哥包括表头和内容

# json转csv
import csv
import json

# 将json文件转化成csv格式

# 将字符串转成列表形式
str_data = '[{"name":"zhang","gender":"male"},{"name":"wang","gender":"female"}]'
json_data = json.loads(str_data)

# 表头
sheet_title = json_data[0].keys()
sheet_data =[]
# 表内容（遍历循环）
for data in json_data:
    sheet_data.append(data.values())
print(sheet_title)
print(sheet_data)

# 创建csv写入器
writer = csv.writer(open('2.csv','w'))
# 写入表头 writerow
writer.writerow(sheet_title)
# 写入内容writerows
writer.writerows(sheet_data)