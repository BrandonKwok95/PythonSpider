import re
# sub可以利用字符串替代指定的字符串
# re.sub(pattern,replace_str,string,count,flags)
# count控制替换次数（默认为全局替换）
#
str = "你好呀兄弟兄弟"
result = re.sub(r'兄弟','弟弟',str,count=1)
print(result)

# split可以分割字符串
# re.split(pattern, string[, maxsplit=0, flags=0])
result = re.split("呀", str)
print(result)


pattern = re.compile('[0-9]')
pattern.fin