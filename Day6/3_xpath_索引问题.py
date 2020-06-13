from lxml import etree
import requests

response = open("3.html")
str_response = response.read()

# 转成xpath数据
xpath_response = etree.HTML(str_response)
# 打印除了li标签
result = xpath_response.xpath("//li")
print(result)
# 打印出了li下的文本节点
result = xpath_response.xpath("//li/text()")
print(result)
# 打印出a下的文本节点
result = xpath_response.xpath("//li//a/text()")
print(result)

#说明了不同标签下的相同类型子标签不存在级别关系（即不可以索引）
result = xpath_response.xpath("//li[1]/a/text()")
print(result)
result = xpath_response.xpath("//li/a[3]/text()")
print(result)