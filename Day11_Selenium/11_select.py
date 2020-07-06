from selenium import webdriver
import time


wd = webdriver.Chrome()
wd.get('http://cdn1.python3.vip/files/selenium/test2.html')

# Select框(单选框)
# 打印出默认选中元素
element = wd.find_element_by_css_selector('#s_checkbox input[checked=checked]')
# Select与前两种选择框有所不同：前两种选择框选项为input标签，而select框为option标签
# 因此，处理方式有所不同
# Selenium中提供了三种方法
# i.    value值
# ii.   index次序
# iii.  可见文本
time.sleep(1)
from selenium.webdriver.support.ui import Select
# 利用Select类提取相应的Select框
select = Select(wd.find_element_by_id("ss_single"))
# value值
select.select_by_value('小雷老师')
time.sleep(1)
# index次序
select.select_by_index(0)
time.sleep(1)
# 可见文本
select.select_by_visible_text('小凯老师')
time.sleep(2)



# Select多选框
select = Select(wd.find_element_by_id("ss_multi"))
# 清除已选对象
'''
# 与多选框相同的操作办法
elements = wd.find_elements_by_css_selector('#ss_multi option[selected=selected]')
for element in elements:
    element.click()
'''
# 在Select类中可以利用下列方法快速去除选中对象(此外也可以像勾选一样，特定清除对象deselect_by_index...)
select.deselect_all()
# 相应地选取对象
select.select_by_index(0)
time.sleep(1)
wd.quit()