import re

#   re库中正则式表达还有两种方法match和search
#   match是尝试从字符串的开头检测，若匹配成功返回对象;若匹配不成功则返回none
#   两种方法

#   i.可以re.match直接使用
#     re.match(pattern,string,flag)
print(re.match('www', 'www.runoob.com'))        # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))        # 不在起始位置匹配

#   ii.可以先re.compile新建正则式后再，调用方法使用
pattern = re.compile('www')
result = pattern.match("www.runoob.com")
print(result)


#   调用span()可以获取符合正则式的索引
#   调用start()可以获取符合正则式的开始索引
#   调用end()可以获取符合正则式的结束索引
print(result.span())
pattern = re.compile('com')
result = pattern.match("www.runoob.com")
print(result)
#   group(num)可以返回正则式中组的特定字符
#   groups(nums)返回一个元祖
print("group")
matchObj = re.match('www(.*)c(.*)', 'www.runoob.com')
print(matchObj.group())     # www.runoob.com
print(matchObj.group(1))    # .runoob.
print(matchObj.group(2))    # .om
print(matchObj.groups())    # ('.runoob.', 'om')