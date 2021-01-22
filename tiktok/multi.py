from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from multiprocessing import Pool
from time import sleep

import random
from tkinter import *


def initDriver(filePath):
    chrome_options = webdriver.ChromeOptions()
    #config open chrome theo specific path
    chrome_options.add_argument(
        "user-data-dir="+filePath)
    driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
    return driver
def set_time():
    set_tg = random.randrange(2,4)
    sleep(set_tg)
def tiktok_follow(filePath):
    driver = initDriver(filePath)
    driver.get('https://www.tiktok.com/upload/?lang=vi')
def pool_handler():
    p = Pool(5)
    kq=p.map_async(tiktok_follow, ('hinh_nen_dep','king_man','clip_nhay_dep','am_thuc','meo'))
    input('df')
    p.close()
    p.join()

if __name__ == '__main__':
	pool_handler()

