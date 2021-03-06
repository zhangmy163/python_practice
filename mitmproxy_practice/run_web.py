from selenium import webdriver
from time import  sleep
import logging
from pathlib import Path
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

def initDriver():
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
    return driver


# 打开driver
def CheckPV(url):
    driver=initDriver()
    logger.info("Open url====: "+url)
    driver.get(url)
    sleep(3)
    driver.quit()

if __name__ == "__main__":
    checkfile=str(base_dir)+"/file/nissa-ciga-null.csv"
    with open(checkfile, 'r') as f:
        urls = f.readlines()
        for url in urls:
            print(url)
            CheckPV('https://'+url)
