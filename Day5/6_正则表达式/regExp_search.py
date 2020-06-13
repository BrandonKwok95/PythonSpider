import re
# 与match类似
# re.search 扫描整个字符串并返回第一个成功的匹配
print(re.search('www', 'www.runoob.com'))        # 在整个字符串中匹配
print(re.search('com', 'www.runoob.com').span())        # 在整个字符串中匹配
# 同样通过span()的调用获取其索引
# group和groups与match相同