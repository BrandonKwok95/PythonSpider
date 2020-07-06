from selenium import webdriver

wd = webdriver.Chrome()
# 存在代码运行速度比服务器返回结果快的情况，因此设定一定的延时来获取完整的返回结果
# wd.implicitly_wait(10)来每隔半秒找寻该元素，最大等待时长为10s
wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')
elements = wd.find_elements_by_tag_name('span')
for element in elements:
    print(element.text)

