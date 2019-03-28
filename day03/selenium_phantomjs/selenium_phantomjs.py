from selenium import webdriver

# 通过 webdriver调用PhantomJS 浏览器
driver = webdriver.PhantomJS()
#driver = webdriver.Chrome()

# 发送浏览器地址栏的 get 请求
driver.get("http://www.baidu.com/")
# 保存当前标签页截图
driver.save_screenshot("baidu1.png")

# 查找指定 id为 wrapper 的元素
element = driver.find_element_by_id("wrapper")

# 获取指定 name为  tj_trnews 的元素
element = driver.find_element_by_name("tj_trnews")

# 获取元素的 文本内容
element.text
# 获取元素的 href属性值
element.get_attribute("href")
# 对当前元素执行点击（通常对a标签处理）
element.click() #模拟鼠标点击事件

driver.save_screenshot("baidu2.png")

# 找到指定 id为 ww 的元素，并输入文本（通常对 input 标签处理）
driver.find_element_by_id("ww").send_keys("劳动节") # 找到指定的输入框输入文本内容
driver.save_screenshot("baidu3.png")

# 查找 指定class为 btn 的元素进行点击
driver.find_elements_by_class_name("btn")[0].click()
driver.save_screenshot("baidu4.png")

# 查找指定 xpath 匹配的 a标签点击
driver.find_element_by_xpath("//div[@id='1']//a").click()
driver.save_screenshot("baidu5.png")

# 查看当前浏览器所有的标签页
driver.window_handles
# 切换到指定标签页
driver.switch_to_window(driver.window_handles[1])
driver.save_screenshot("baidu6.png")

# 获取当前页面的url地址
driver.current_url
# 获取当前标签页的网页源码(执行完js、css等所有数据渲染后的源码）
html = driver.page_source
# 关闭当前所在标签页
driver.close()
# 退出浏览器
driver.quit() # 关闭浏览器（回收内存）


%hist -f selenium_phantomjs.py
