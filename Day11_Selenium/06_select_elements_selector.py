from selenium import webdriver
wd = webdriver.Chrome()
wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')
# 可以利用css选择器选择元素
elements = wd.find_elements_by_css_selector('.plant,.animal')
for element in elements:
    print(element.get_attribute('innerText'))
