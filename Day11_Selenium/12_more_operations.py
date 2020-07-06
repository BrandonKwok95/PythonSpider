# 可以通过Selenium中提供的Actionchains类来实现多种操作
from selenium import webdriver
wb = webdriver.Chrome()
wb.get('https://www.baidu.com/')


# 悬停操作
from selenium.webdriver.common.action_chains import ActionChains
# 将webdriver添加到ActionChains类中
ac = ActionChains(wb)
ac.move_to_element(wb.find_element_by_css_selector('[name = "tj_briicon"]')).perform()