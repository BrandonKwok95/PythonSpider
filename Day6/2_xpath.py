from lxml import etree

import requests

url = "http://news.baidu.com/"

response = requests.get(url)
str_response = response.content.decode("utf-8")
with open("2.html","w",encoding="utf-8") as f:
    f.write(str_response)

# 利用xpath解析文件
# 1.转解析类型
xpath_data = etree.HTML(str_response)

# 2.调用xpath的方法
# 基本语法
# "/"   节点顺序（有时候，节点数过多）
# "//"  跨节点选取内容
# 可以利用索引截取出指定内容 a[@属性名值对]（尽量用id）
# 取文本用text()
# 取截取相应标签属性值 /@属性值
#
# xpath返回列表值
# xpath中的索引从1开始
# 注意跨节点时，没有平级这一特点（如在列表中每个<li>都有一个<a>的子节点，这几个子节点并不是平级关系）


result = xpath_data.xpath('//a')
print(len(result))
result = xpath_data.xpath('//a//text()')
print(result)
result = xpath_data.xpath('//a[@mon="ct=1&a=2&c=top&pn=1"]//text()')
print(result)
result = xpath_data.xpath('//a[@mon="ct=1&a=2&c=top&pn=1"]/@href')
print(result)