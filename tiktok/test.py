from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import random
import getpass
from time import sleep
from multiprocessing import Pool
from datetime import datetime
import keyboard
import io
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
        self.driver.get('https://www.tiktok.com/upload/?lang=vi')
        # sleep(2)
        # email_ins = self.driver.find_element_by_name('username')
        # email_ins.send_keys('nguyen_xs')

        # sleep(2)
        # pass_ins = self.driver.find_element_by_name('password')
        # pass_ins.send_keys('nguyen98bg')
        input('oh')
        # sleep(2)
        # buttons = self.driver.find_elements_by_css_selector("button")
        # buttons[1].click()
        # for inx,button in enumerate(buttons, start=0):
        #     if inx == 1:
        #         print(buttons[2])
        #         button.click()

    def download_list_video(self,filePath):

        self.driver = self.khoitao(filePath)
        self.driver.get('https://tiktokv.tk/')
        # input("ok")
        
        sleep(2)
        # keyboard.press_and_release('ctrl+a')
        self.driver.find_elements_by_css_selector('.form-group input')[0].click()
        keyboard.press_and_release('ctrl+a')
        sleep(2)

        # @smesleshtjq
        # @danejoness


        self.driver.find_elements_by_css_selector('.form-group input')[0].send_keys("@moto.li")
        self.driver.find_elements_by_css_selector('#search-btn')[0].click()
        sleep(2)
        input("wait")
        # self.driver.execute_script("window.scrollBy(0,1000)")
        # self.driver.find_elements_by_css_selector(".load-more button")[0].click()
        list_item = self.driver.find_elements_by_css_selector(".tiktok-video-item")
        self.driver.find_elements_by_css_selector('.tiktok-video-item a')[0].click()
        sleep(2)
        print(len(list_item))
        for index in range(0,len(list_item)):
            self.driver.find_elements_by_css_selector('.video-download a')[1].click()
            sleep(2)
            self.driver.find_elements_by_css_selector('.popup-next')[0].click()
    def get_link_video_download(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://vt.tiktok.com/ZST23Xhk/')
        input("await")
        list_link=open('list_link_video.txt','w')
        value = self.driver.find_elements_by_css_selector('._ratio_wrapper a')
        print(len(value))
        for item in value:
            list_link.write(item.get_attribute('href')+"\n")
        
        self.driver.get('https://tiktokfull.com/')
        # list_link=open('list_link_video.txt')
        list_link=open('list_link_video.txt','r')

        read = list_link.readlines()
        # print(read)
        for getItem in read:
            print(getItem)
            self.driver.find_elements_by_css_selector('#input-url')[0].send_keys(getItem)
            self.driver.find_elements_by_css_selector('#input-url')[0].click()
            sleep(5)
            self.driver.find_elements_by_css_selector('.pb-2 a')[0].click()
            sleep(3)
            keyboard.press_and_release('f5')
            sleep(3)

        list_link.close()    
    def get_link_video_download_douyin(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://tiktokfull.com/')
        save_list_link=open('save_link_douyin.txt','w')
        list_link=open('link_douyin.txt','r',encoding="utf-8")
        read = list_link.readlines()
        # print(read)
        for getItem in read:
            for item in getItem.split(sep=' '):
                # item.split(sep = ' ')
                if (item.__contains__('http')):
                    save_list_link.write(item +"\n")
                else:
                    continue

        save_list_link=open('save_link_douyin.txt','r')
        read_link_video_convert = save_list_link.readlines()
        for getItem in read_link_video_convert:
            print(getItem)
            sleep(2)
            self.driver.find_elements_by_css_selector('#input-url')[0].send_keys(getItem)
            sleep(2)
            self.driver.find_elements_by_css_selector('#input-url')[0].click()
            sleep(8)
            self.driver.find_elements_by_css_selector('.pb-2 a')[0].click()
            sleep(3)
            keyboard.press_and_release('f5')
            sleep(3)
        list_link.close()
        save_list_link.close()

    def get_link_video_download_douyin_snaptik(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://snaptik.app/vn')
        save_list_link=open('save_link_douyin.txt','w')
        list_link=open('link_douyin.txt','r',encoding="utf8")
        read = list_link.readlines()
        # print(read)
        for getItem in read:
            for item in getItem.split(sep=' '):
                # item.split(sep = ' ')
                if (item.__contains__('http')):
                    save_list_link.write(item +"\n")
                else:
                    continue

        save_list_link=open('save_link_douyin.txt','r')
        read_link_video_convert = save_list_link.readlines()

        for getItem in read_link_video_convert:
            print(getItem)
            self.driver.find_elements_by_css_selector('.input-group .form-control')[0].send_keys(getItem)
            self.driver.find_elements_by_css_selector('#icondl')[0].click()
            sleep(5)
            self.driver.find_elements_by_css_selector('.mb-0 a')[0].click()
            sleep(3)
            keyboard.press_and_release('f5')
            sleep(3)
        list_link.close()
        save_list_link.close()    

    def t1(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://tiktok.com/')
        input("gb")
    def t2(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://tiktok.com/')
        input("gb")
    def t3(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://tiktok.com/')
        input("gb")
    def t4(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://tiktok.com/')
        input("gb")
    def t5(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://tiktok.com/')
        input("gb")




    def auto(self):
        sleep(2)
        # self.download_list_video('ngb')
        # self.instagram_post_weightloss('meo')
        # self.instagram_post_weightloss('king_man')
        # self.instagram_post_weightloss('clip_nhay_dep')
        # self.instagram_post_weightloss('am_thuc')
        # self.instagram_follow_init("pets")
        # self.get_link_video_download('ngb')
        self.get_link_video_download_douyin('n')
    
        # self.get_link_video_download_douyin_snaptik('n')
        # self.t1('n1')
        # self.t2('n2')
        # self.t3('n3')
        # self.t4('n4')
        # self.t5('n5')
bot=InstagramBot()
bot.auto()


