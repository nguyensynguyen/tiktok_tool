from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import random
import getpass
from time import sleep
from multiprocessing import Pool
from datetime import datetime

class InstagramBot():
    def khoitao(self,filePath):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(
        "user-data-dir="+filePath)
        # prefs = {
        #     "profile.managed_default_content_settings.images": 2
        # }
        # chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(
            './chromedriver', chrome_options=chrome_options)

        return self.driver

    def set_time(self):
        self.set_tg = random.randrange(2,4)
        sleep(self.set_tg)
    def instagram_follow_init(self,filePath):

        self.driver = self.khoitao(filePath)
        # self.driver.get('https://www.fb.com/')
        # input("ok")
        self.driver.get('https://www.instagram.com/')
        sleep(2)
        sleep(2)
        email_ins = self.driver.find_element_by_name('username')
        email_ins.send_keys('weightlosstips.in')

        sleep(2)
        pass_ins = self.driver.find_element_by_name('password')
        pass_ins.send_keys('nguyenbg9811')
        input('oh')
        # sleep(2)
        # buttons = self.driver.find_elements_by_css_selector("button")
        # buttons[1].click()
        # for inx,button in enumerate(buttons, start=0):
        #     if inx == 1:
        #         print(buttons[2])
        #         button.click()

    def instagram_post_weightloss(self,filePath):
        self.driver = self.khoitao(filePath)
            
    def auto(self):
        sleep(3)
        self.instagram_post_weightloss('New_folder')
        # self.instagram_post_love('fb')
        # self.instagram_follow_init('nguyen_xs')
        # self.instagram_follow_spiritual('spiritual')
        # sleep(2)
        # self.instagram_follow_love('love')
        # sleep(2)
        # self.instagram_follow_weightloss('wl')
        # sleep(2)
        # self.instagram_follow_dog('dog')
        # sleep(2)
bot=InstagramBot()
bot.auto()


