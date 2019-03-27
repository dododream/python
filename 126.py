# 导入webdriver
from selenium import webdriver

##################################################################################################
## 修改PhantomJS的User-Agent流程

# 可以修改webdriver请求报头
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# iPhone的手机浏览器User-Agent
agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A365 Safari/600.1.4"
# 构建PhantomJS的浏览器报头，修改为字典类型
dcap = dict(DesiredCapabilities.PHANTOMJS)
# 修改User-Agent的值
dcap["phantomjs.page.settings.userAgent"] = agent

# 创建webdriver对象，并指定使用修改后的请求报头对象，并禁用图片加载（提高网页加载速度）
driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--load-images=false'])
#################################################k#################################################

# 发送网页请求
driver.get("http://email.126.com/")
# 获取页面截图（是个广告，需要点击一个连接才能访问网页版的126邮箱）
driver.save_screenshot("126_1.png")
print driver.page_source


# 点击页面连接（访问网页版邮箱的页面）
driver.find_element_by_class_name("entry").click()
driver.save_screenshot("126_2.png")

# 获取手机版126邮箱的页面数据
print driver.page_source
