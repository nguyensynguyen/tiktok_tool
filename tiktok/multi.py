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
def tiktok_post(filePath):
    driver = initDriver(filePath)
    driver.get('https://www.tiktok.com/upload/?lang=vi')
    flagCount = 55
    sleep(3)
    if filePath == str(flagCount+0):
        # input("dv")
        sleep(3)
        for index in range(1,6):
            print("t1_ ({}).mp4".format(index))
            sleep(3)
            driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/0_daopho/anh ({}).mp4'.format(index))
            sleep(1)
            driver.find_elements_by_css_selector(".DraftEditor-editorContainer")[0].click()
            # keyboard.press_and_release('ctrl+v')
            sleep(15)
            driver.find_elements_by_css_selector(".btn-post")[0].click()
            sleep(6)
            driver.find_elements_by_css_selector(".modal-btn")[0].click()   
    if filePath == str(flagCount+1):
        # input("dv")
        for index in range(6,11):
            print("t2__ ({}).mp4".format(index))
            sleep(3)
            driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/0_daopho/anh ({}).mp4'.format(index))
            sleep(1)
            driver.find_elements_by_css_selector(".DraftEditor-editorContainer")[0].click()
            # keyboard.press_and_release('ctrl+v')
            sleep(15)
            driver.find_elements_by_css_selector(".btn-post")[0].click()
            sleep(6)
            driver.find_elements_by_css_selector(".modal-btn")[0].click()   
    if filePath == str(flagCount+2):
        # input("dv")
        sleep(3)
        for index in range(11,16):
            print("t3____ ({}).mp4".format(index))
            sleep(3)
            driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/0_daopho/anh ({}).mp4'.format(index))
            sleep(1)
            driver.find_elements_by_css_selector(".DraftEditor-editorContainer")[0].click()
            # keyboard.press_and_release('ctrl+v')
            sleep(15)
            driver.find_elements_by_css_selector(".btn-post")[0].click()
            sleep(6)
            driver.find_elements_by_css_selector(".modal-btn")[0].click()   
    if filePath == str(flagCount+3):
        # input("dv")
        sleep(3)
        for index in range(16,21):
            print("t4_____ ({}).mp4".format(index))
            sleep(3)
            driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/0_daopho/anh ({}).mp4'.format(index))
            sleep(1)
            driver.find_elements_by_css_selector(".DraftEditor-editorContainer")[0].click()
            # keyboard.press_and_release('ctrl+v')
            sleep(15)
            driver.find_elements_by_css_selector(".btn-post")[0].click()
            sleep(6)
            driver.find_elements_by_css_selector(".modal-btn")[0].click()           
    if filePath == str(flagCount+4):
        # input("dv")
        sleep(3)
        for index in range(21,26):
            print("t5______ ({}).mp4".format(index))
            sleep(3)
            driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/0_daopho/anh ({}).mp4'.format(index))
            sleep(1)
            driver.find_elements_by_css_selector(".DraftEditor-editorContainer")[0].click()
            # keyboard.press_and_release('ctrl+v')
            sleep(15)
            driver.find_elements_by_css_selector(".btn-post")[0].click()
            sleep(6)
            driver.find_elements_by_css_selector(".modal-btn")[0].click()   
    # print(filePath)
    # input("d")
def open_acount_tiktok(filePath):
    driver = initDriver(filePath)
    driver.get('https://www.tiktok.com/upload/?lang=vi')

def init_acount_tiktok(filePath):
    driver = initDriver(filePath)
    driver.get('https://www.tiktok.com/upload/?lang=vi')

def pool_handler():
    p = Pool(5)
    # kq=p.map_async(tiktok_post, ('55','56','57','58','59'))
    # kq=p.map_async(open_acount_tiktok, ('t1','t2','t3','t4','t5'))
    kq=p.map_async(init_acount_tiktok, ('55','56','57','58','59'))
    input("dv")
    p.close()
    p.join()

if __name__ == '__main__':
	pool_handler()

