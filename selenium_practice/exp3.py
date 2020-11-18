from selenium import webdriver
from time import  sleep

options = webdriver.ChromeOptions()
# 忽略https警告
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-gpu')
options.add_argument('--disable-cache')
options.add_argument('--proxy-server={host}:{port}'.format(host="127.0.0.1", port=8080))

# 无头模式
options.headless = True
# window.navigator.webdriver=true 修改
options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 打开driver
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.dongfeng-nissan.com.cn/")
sleep(10)
driver.close()