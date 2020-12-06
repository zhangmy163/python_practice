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
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-cache')
        options.add_argument('--proxy-server={host}:{port}'.format(host="127.0.0.1", port=8080))
        # 无头模式
        options.headless = True
        # window.navigator.webdriver=true 修改
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


# 打开driver
def CheckPV(url):
    driver=initDriver("headless")
    logger.info("Open url====: "+url)
    driver.get(url)
    sleep(3)
    driver.quit()
def CheckEvent(url,x):
    driver=initDriver("headless")
    logger.info("Open url====: "+url)
    driver.get(url)
    logger.info("Click ====: "+url)
    driver.find_element_by_xpath(x).click()
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
        CheckEvent(i[0],i[1])
