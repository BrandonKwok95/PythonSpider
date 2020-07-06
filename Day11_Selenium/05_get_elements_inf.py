from selenium import webdriver
import time
wd = webdriver.Chrome()
wd.get('http://cdn1.python3.vip/files/selenium/test3.html')
element = wd.find_element_by_id('input1')
# 清除文本框内容
element.clear()
# 输入文本框内容
element.send_keys('Kwok')
time.sleep(1)

element = wd.find_element_by_tag_name('h3')
# 获取节点文本内容
print(element.text)
# 获取节点属性值
print(element.get_attribute('style'))
# 获取当前元素节点下的元素节点（不包含当前节点）
print(element.get_attribute('innerHTML'))
# 获取当前元素节点下的元素节点（不包含当前节点）
print(element.get_attribute('outerHTML'))
# 打印当前元素节点下的所有的文本内容（包括子元素的文本内容）
print(element.get_attribute('innerText'))
# 关闭当前页面
wd.close()
# 关闭浏览器
# wd.quit()