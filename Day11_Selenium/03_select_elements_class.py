from selenium import webdriver

wd = webdriver.Chrome()
wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')
# find_element_by_class_name返回第一个元素
elements = wd.find_elements_by_class_name('animal')
# 返回列表值
print(type(elements))
for element in elements:
    # text属性可以返回元素的文本
    print(element.text)
# 可以像元素选择器一样，层层筛选
elements = wd.find_element_by_id('container')
elements = elements.find_elements_by_tag_name('span')
for element in elements:
    print(element.text)