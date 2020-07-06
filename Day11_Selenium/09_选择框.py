from selenium import webdriver
import time


wd = webdriver.Chrome()
wd.get('http://cdn1.python3.vip/files/selenium/test2.html')

# Radio框(单选框)
# 打印出默认选中元素
element = wd.find_element_by_css_selector('#s_radio input[checked=checked]')
print('当前选中的是: ' + element.get_attribute('value'))
time.sleep(2)
# 点击其他元素
wd.find_element_by_css_selector('#s_radio input[value="小雷老师"]').click()

print('当前选中的是: ' + element.get_attribute('value'))
time.sleep(1)
wd.quit()

