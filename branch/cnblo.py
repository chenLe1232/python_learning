from selenium import webdriver
import time


wd = webdriver.Chrome()
# 打开百度
wd.get("https://www.baidu.com")
# 定位输入框并输入关键字
wd.find_element_by_id("kw").send_keys("selenium")
# 点击 百度一下 搜索
wd.find_element_by_id("su").click()
# 等待3s
time.sleep(3)
# 关闭浏览器
wd.quit()