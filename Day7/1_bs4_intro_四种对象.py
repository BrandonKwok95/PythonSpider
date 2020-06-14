#   bs4 是一个从HTML和XML中提取数据的python库
#   可以利用选择器提取出相应的数据（与css选择器类似）
#   优点无需查找相关标签（相比xpath）

from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<c><!--dsadsdsadsadsa--></c>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
#   使用流程
#   1.转类型
#   soup = BeautifulSoup(html_doc)会弹出警告,因此需要假如特定的解析器(主动添加解析库)
soup = BeautifulSoup(html_doc,'lxml')
print(type(soup))
#   2.格式化输出（补全）
#result = soup.prettify
#print(result)

#   3.解析数据
#   BeautifulSoup的四大对象：
#   i.      tag                 文档下的标签的对象为Tag
#   ii.     NavigableString     文档下的标签中的文本为NavigableString
#   iii.    BeautifulSoup       文档（html）是BeautifulSoup
#   iv.     Comment             文档中的注释(使用较少)
#   取出特定的标签（直接利用属性取）
result = soup.a
#   <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
print(result)
print(type(result))

#   内容
#   string可以直接输出标签中的文本
result = soup.a.string
print(result) #   Elsie
print(type(result))
#   属性
result = soup.a['href']
print(result) #   http://example.com/elsie
#   注释
result = soup.c.string
print(result)
print(type(result))
