from selenium import webdriver
import time

wd = webdriver.Chrome()
wd.get('http://cdn1.python3.vip/files/selenium/sample3.html')

element = wd.find_element_by_css_selector('a')
element.click()
elements = wd.find_elements_by_css_selector('#logo')
for element in elements:
    print(element.get_attribute('role'))
print(wd.title)
time.sleep(2)
# 发现存在问题：即使打开了必应的页面，仍然无法将webdriver切换到相应的窗口
# 使用下列切换窗口语句解决该问题
# wd.switch_to.window(handle)根据handle来切换
# 由于handle的值不好确定，只能通过下列循环的方法实现（可以简单地理解handle为页面的id信息）

# 假如还想切换回原先的window，可以事先保存原先window的handle值
mainWindow = wd.current_window_handle
for handle in wd.window_handles:
    print(handle)
    wd.switch_to.window(handle)
    # 再通过wd.title确定是否为该页面，并输出相应的handle值
    if '必应' in wd.title:
        break
print(handle)
element = wd.find_element_by_id('sb_form_q')
element.send_keys('KWOK')
time.sleep(2)
element = wd.find_element_by_css_selector('[class= "search icon tooltip"]')
element.click()
time.sleep(2)
# 切换回原来窗口
wd.switch_to.window(mainWindow)
time.sleep(2)
wd.quit()