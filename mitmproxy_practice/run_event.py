from selenium import webdriver
from time import  sleep
import logging
from pathlib import Path
import csv
base_dir=Path(__file__).resolve().parent
logfile=str(base_dir)+"/log.txt"

# if Path(logfile).is_file():
#     Path(logfile).unlink()

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler(logfile)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def initDriver(t):
    if(t=="headless"):
        options = webdriver.ChromeOptions()
        # 忽略https警告
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-cache')
        options.add_argument("--window-size=1960,1080")
        options.add_argument('--proxy-server={host}:{port}'.format(host="127.0.0.1", port=8080))
        # 无头模式
        # options.headless = True
        # window.navigator.webdriver=true #修改
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        driver = webdriver.Chrome(chrome_options=options)
    elif(t=="normal"):
        options = webdriver.ChromeOptions()
        # 忽略https警告
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-cache')
        options.add_argument('--proxy-server={host}:{port}'.format(host="127.0.0.1", port=8080))        
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        driver = webdriver.Chrome(chrome_options=options)
    return driver

def scroll_to_bottom(driver):
    js = "return action=document.body.scrollHeight"
    # 初始化现在滚动条所在高度为0
    height = 0
    # 当前窗口总高度
    new_height = driver.execute_script(js)

    while height < new_height:
        # 将滚动条调整至页面底部
        for i in range(height,new_height,100):
            driver.execute_script('window.scrollTo(0, {})'.format(i))
            sleep(0.5)
        height = new_height
        sleep(2)
        new_height = driver.execute_script(js)
# 打开driver
def CheckPV(url):
    driver=initDriver("headless")
    logger.info("Open url====: "+url)
    driver.get(url)
    sleep(3)
    driver.quit()
def CheckEvent(url,x):
    driver=initDriver("headless")
    driver.get(url)
    sleep(1)
    # print(x)
    driver.save_screenshot(str(base_dir)+"/tmp.png")
    for clkx in x:
        if clkx == "":
            continue
        if x.index(clkx) == len(x):
            logger.info("Click ====: "+url)
        elif x[x.index(clkx)+1] == "":
            logger.info("Click ====: "+url)
        try:
            driver.find_element_by_xpath(clkx).click()
        except:
            scroll_to_bottom(driver)
            driver.find_element_by_xpath(clkx).click()
    sleep(5)
    driver.quit()
if __name__ == "__main__":
    # checkfile=str(base_dir)+"/file/nissa-ciga-null.csv"
    # with open(checkfile, 'r') as f:
    #     urls = f.readlines()
    #     for url in urls:
    #         print(url)
    #         CheckPV('https://'+url)
    checkfile=str(base_dir)+"/file/dyk-event.csv"
    f = csv.reader(open(checkfile,'r')) 
    for i in f:
        # print(i[1:])
        # print(len(i[1:]))
        CheckEvent(i[0],i[1:])
