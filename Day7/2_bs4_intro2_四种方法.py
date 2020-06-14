from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
    <body>
<p id="oneonly" class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,'lxml')
#   四种通用的解析方法
#   i.find   返回符合查询条件的第一个标签（与直接用属性取类似）
#   以标签名查找
result = soup.find(name="p")
print(result)
#   以属性名查找（字典）(同样只返回一个)
result = soup.find(attrs={"class":"sister"})
print(result)
#   以文本内容查找
result = soup.find(text="Lacie")
print(result)

#   ii.find_all
result = soup.find_all(name="p")
print(len(result))
#   limit值表示选中数目
result = soup.find_all(name="p",limit=5)
print(len(result))

#   iii.select_one 与css选择其相同
#   简单回顾
#   css的4种选择器
#   i. 标签选择器：标签名{}    ii.id选择器：#id值{}   iii.类选择器：.类值    iv.通配选择器：*{}
result = soup.select_one('p')
print(result)
result = soup.select_one('#oneonly')
print(result)
result = soup.select_one('.title')
print(result)

#   iv.select   返回列表值
print('select')
result = soup.select('p')
print(result)
result = soup.select('#oneonly')
print(result)
result = soup.select('.title')
print(result)