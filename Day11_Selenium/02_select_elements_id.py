from selenium import webdriver
wd = webdriver.Chrome()         #相当于一个遥控器(创建一个实例)
wd.get('https://www.baidu.com')

# 根据id来选取(找到baidu中的输入框)
element = wd.find_element_by_id('kw')
# 往元素中输入文本
element.send_keys('郭昊\n')

element = wd.find_element_by_id('kw')
element.send_keys('Real Madrid')
element = wd.find_element_by_id('su')
# click是点击
element.click()