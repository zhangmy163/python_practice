# -*- coding:utf-8 -*-
from time import ctime, sleep
from selenium import webdriver
import threading

url=['gv.bo338.com/search',
    'nf.56bet365.vip/',
    'www.dyk.com.cn/404',
    'kx.aac88.com/csr',
    'www.dyk.com.cn/',
    '8kcai.app/',
    'www.dyk.com.cn/vehicles/newsportage/specs',
    'www.dyk.com.cn/brand/policy',
    'gv.bo338.com/dealer',
    'www.dyk.com.cn/shop-made-easy',
    'www.dyk.com.cn/vehicles/allnewk5',
    '101936.cjju.xyz/',
    'www.dyk.com.cn/vehicles/k4cachet',
    'www.dyk.com.cn/vehicles/k5phev',
    'www.dyk.com.cn/vehicles/forte',
    'www.dyk.com.cn/vehicles/pegas',
    'www.dyk.com.cn/vehicles/newkx5',
    'www.dyk.com.cn/vehicles/pegas']

def select_browser():
    print("start %s" % ctime())
    try:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        dr = webdriver.Chrome(chrome_options=option)
        return dr
    except Exception as msg:
        print("启动浏览器出现异常：%s" % str(msg))

def test_open(n):
    driver = select_browser()
    driver.maximize_window()
    driver.get("http://"+str(url[n]))
    cookie = driver.get_cookies()
    print("=======cookie=======")
    print(cookie)
    sleep(10)
    # print(driver.title)
    driver.quit()
    print("end %s" % n, ctime())

def thread_browser(*args):
    if args:
        threads = []                     # 创建线程列表
        for n in args:
            t = threading.Thread(target=test_open, args=(n,))    # 创建线程
            threads.append(t)
        for t in threads:
            t.start()                    # 启动线程
        for t in threads:
            t.join()                     # 守护线程
        print("end all time %s"% ctime())
    else:
        print("Please pass at least one browser name")
        
if __name__ == "__main__":
     thread_browser(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)
    # thread_browser(0,1,2)