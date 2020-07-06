from selenium import webdriver
import time
wd = webdriver.Chrome()
wd.get('http://cdn1.python3.vip/files/selenium/sample2.html')
elements = wd.find_elements_by_css_selector('.plant')
for element in elements:
    print(element.text)
# 上面语句无法成功打印出元素文本内容
# iframe/frame元素中包含一个html文档，导致无法正常找到相应的元素
# 因此，必须切换操作范围到被潜入的文档中
# webdriver中可以切换到相应的frame中，在进行元素查找
# 特殊情况：假如相应的frame和iframe没有id属性，可以利用选择器去寻找相应的frame
#wd.switch_to.frame('frame1')
print("switching...")
wd.switch_to.frame(wd.find_element_by_css_selector('iframe[src="sample1.html"]')) # 也可以达到同样效果
elements = wd.find_elements_by_css_selector('.plant')
for element in elements:
    print(element.get_attribute('outerHTML'))

# 操作完内部元素后，假如想切换到外部的HTML文档可以利用下列语句切换
print("switching...")
wd.switch_to.default_content()
elements = wd.find_elements_by_css_selector('.baiyueheiyu')
for element in elements:
    print(element.text)
wd.find_element_by_id('outerbutton').click()

time.sleep(1)
wd.quit()