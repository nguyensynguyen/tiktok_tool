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

from selenium.webdriver.chrome.service import Service

from fake_useragent import UserAgent

class InstagramBot():
    def khoitao(self,filePath):
        chrome_options = webdriver.ChromeOptions()
        ua = UserAgent()
        a = ua.random
        user_agent = ua.random
        print(user_agent)
        chrome_options.add_argument(f'user-agent={user_agent}')
        chrome_options.add_argument(
        "user-data-dir=D:\\tiktok_tool\\tiktok\\"+filePath)
        # prefs = {
        #     "profile.managed_default_content_settings.images": 2
        # }
        # chrome_options.add_experimental_option("prefs", prefs)
        s = Service("./chromedriver")
        self.driver = webdriver.Chrome(
            service =s, chrome_options=chrome_options)

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
        checkStr = ""
        checkCount = 0
        for getItem in read_link_video_convert:
            print(getItem)
            if checkCount == 0:
                checkStr = getItem
                sleep(2)
                self.driver.find_elements_by_css_selector('#paste')[0].click()
                sleep(1)
                self.driver.find_elements_by_css_selector('#paste')[0].click()
                sleep(1)
                self.driver.find_elements_by_css_selector('#input-url')[0].send_keys(getItem)
                sleep(1)
                # self.driver.find_elements_by_css_selector('#input-url')[0].click()
                sleep(5)
                self.driver.find_elements_by_css_selector('.pb-2 a')[0].click()
                sleep(3)
                self.driver.execute_script("window.scrollBy(0,-20000)")
                keyboard.press_and_release('f5')
                sleep(3)
                checkCount += 1
            else:
                if checkStr != getItem:
                    sleep(2)
                    self.driver.find_elements_by_css_selector('#paste')[0].click()
                    sleep(1)
                    self.driver.find_elements_by_css_selector('#paste')[0].click()
                    sleep(1)
                    self.driver.find_elements_by_css_selector('#input-url')[0].send_keys(getItem)
                    sleep(1)
                    # self.driver.find_elements_by_css_selector('#input-url')[0].click()
                    sleep(5)
                    self.driver.find_elements_by_css_selector('.pb-2 a')[0].click()
                    sleep(3)
                    self.driver.execute_script("window.scrollBy(0,-20000)")
                    keyboard.press_and_release('f5')
                    sleep(3)
                    checkStr = getItem


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
                if (item.__contains__('https')):
                    save_list_link.write(item +"\n")
                else:
                    continue

        save_list_link=open('save_link_douyin.txt','r')
        read_link_video_convert = save_list_link.readlines()
        checkStr = ""
        checkCount = 0
        for getItem in read_link_video_convert:
            if checkCount == 0:
                print(getItem)
                self.driver.find_elements_by_css_selector('#url')[0].send_keys(getItem)
                # self.driver.find_elements_by_css_selector('#icondl')[0].click()
                sleep(7)
                self.driver.find_elements_by_css_selector('.mb-0 a')[0].click()
                sleep(3)
                keyboard.press_and_release('f5')
                sleep(3)
                checkCount += 1
            else:
                if checkStr != getItem:
                    print(getItem)
                    self.driver.find_elements_by_css_selector('#url')[0].send_keys(getItem)
                    # self.driver.find_elements_by_css_selector('#icondl')[0].click()
                    sleep(7)
                    self.driver.find_elements_by_css_selector('.mb-0 a')[0].click()
                    sleep(3)
                    keyboard.press_and_release('f5')
                    sleep(3)
                    checkStr = getItem
        list_link.close()
        save_list_link.close()    

    def get_link_video_download_douyins(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://www.douyin.com/user/MS4wLjABAAAABRkC8geqCrjUsDP5oQCtSYLNkT2Xps1UMHYKo7ScViy46BPLvyi5TETzeYifsM7b')
        # input("sd")
        # save_list_link=open('link_douyin.txt','w')
        # list_link=open('link_douyin.txt','r',encoding="utf-8")
        # read = list_link.readlines()
        save_list_link=open('link_douyin.txt','w')
        sleep(2)
        # for x in range(1,4):
        #     self.driver.execute_script("window.scrollBy(0,2000)")
        #     sleep(1)
        input("dv")
        read1 = self.driver.find_elements_by_css_selector('._787337747252a601a979b6885202ecb6-scss')
        # print(len(read1))
        for item in range(0,34):
            # if (read1[item].get_attribute('href').__contains__('video')):
               save_list_link.write(read1[item].get_attribute('href') +"\n")
    

        # list_link.close()

    def get_link_video_download_douyin1(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://www.tiktok.com/@gaixinh446?lang=vi-VN&is_copy_url=1&is_from_webapp=v1')
        read1 = self.driver.find_elements_by_css_selector('.jsx-2261688415 a')
        save_list_link=open('save_link_douyin.txt','w')
        save_list_link1=open('save_link_douyin.txt','r')
        # print(read)


        for item in range(0,len(read1)):
            if (read1[item].get_attribute('href').__contains__('video')):
               save_list_link.write(read1[item].get_attribute('href') +"\n")
               # print(read1[item].get_attribute('href'))
        save_list_linkz = save_list_link1.readlines()
        for getItem in save_list_linkz:
            print(getItem)
            # sleep(2)
            # # self.driver.find_elements_by_css_selector('#paste')[0].click()
            # # sleep(1)
            # # self.driver.find_elements_by_css_selector('#paste')[0].click()
            # sleep(1)
            # self.driver.find_elements_by_css_selector('#input-url')[0].send_keys(getItem)
            # # sleep(2)
            # # self.driver.find_elements_by_css_selector('#input-url')[0].click()
            # sleep(8)
            # self.driver.find_elements_by_css_selector('.pb-2 a')[0].click()
            # sleep(3)
            # # self.driver.execute_script("window.scrollBy(0,-20000)")
            # keyboard.press_and_release('f5')
            # sleep(3)
        save_list_link.close()


    


    def get_link_profile(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://www.douyin.com/user/MS4wLjABAAAAHxBThUlj_rqmfNnniJMZ7Y76K-zmmyr_7moWsE9i991WUD7wspuWDdxefOP2TW3R')
        # input("sd")
        # save_list_link=open('link_douyin.txt','w')
        # list_link=open('link_douyin.txt','r',encoding="utf-8")
        # read = list_link.readlines()
        save_list_link=open('link_douyin.txt','w')
        sleep(2)
        # for x in range(1,4):
        #     self.driver.execute_script("window.scrollBy(0,2000)")
        #     sleep(1)
        input("dv")
        read1 = self.driver.find_elements_by_css_selector('._787337747252a601a979b6885202ecb6-scss')
        print(len(read1))
        for item in range(0,33): #len(read1)
            # if (read1[item].get_attribute('href').__contains__('video')):
               save_list_link.write(read1[item].get_attribute('href') +"\n")
    

        # list_link.close()
    # day_yt = input("nhap ngay : ")
    day_value = 5 + 2

    def upload_youtube(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get("https://studio.youtube.com/channel/UCD2NF_fEA7WWXhTr3v29Nbg")
        sleep(4)
        for i in range(1,6):
            self.driver.find_elements_by_css_selector('#create-icon')[0].click()
            sleep(1)
            self.driver.find_elements_by_css_selector('#text-item-0')[0].click()
            sleep(1)
            self.driver.find_elements_by_css_selector('#content input')[0].send_keys("D:/0_convert/v ({}).mp4".format(i))
            sleep(5)
            self.driver.find_elements_by_css_selector('#textbox')[0].send_keys("D:/0_convert/v.mp4")
            sleep(1)
            self.driver.find_elements_by_css_selector('#offRadio')[1].click()
            sleep(1)

            for i in range(0,3):
                self.driver.find_elements_by_css_selector('#next-button')[0].click()
            sleep(2)

            self.driver.find_elements_by_css_selector('#radioLabel')[3].click()
            sleep(1)
            self.driver.find_elements_by_css_selector('#radioLabel')[4].click() #chọn radio lên lịch
            sleep(1)
            self.driver.find_elements_by_css_selector('.ytcp-dropdown-trigger')[4].click()
            sleep(1)
            self.driver.find_elements_by_css_selector('.calendar-day')[self.day_value].click()
            sleep(1)
            self.driver.find_elements_by_css_selector('.ytcp-dropdown-trigger')[11].click()
            sleep(1)
            self.driver.find_elements_by_css_selector('.tp-yt-paper-item')[50].click()#chọn giờ
            self.driver.find_elements_by_css_selector('#done-button')[0].click()
            sleep(5)
            self.driver.find_elements_by_css_selector('#close-button')[1].click()
            self.day_value += 1

    def init(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://www.tiktok.com/upload/?lang=vi')
        input("ok")
        self.driver.close()
    def get_like(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://www.douyin.com/recommend')
        input("ff")
        for i in range(0,30):
            self.driver.find_elements_by_css_selector('.aa56c3391b648160ab6b643fc006dfa1-scss .png')[5].click()
            sleep(1)
            self.driver.find_elements_by_css_selector('.xgplayer-playswitch-next')[0].click()
            sleep(3)
    def auto(self):
        sleep(2)
        # self.download_list_video('ngb')
        # self.instagram_post_weightloss('meo')
        # self.instagram_post_weightloss('king_man')
        # self.instagram_post_weightloss('clip_nhay_dep')
        # self.instagram_post_weightloss('am_thuc')
        # self.instagram_follow_init("pets")
        # self.get_link_video_download('ngb')
        # self.get_link_video_download_douyin('n')
        # self.get_link_video_download_douyins('n')
        # self.get_link_profile('n')
        list10tk1 = ['s2140','s2137','s2131','s2130','s271','s262','s259','s2123']#,'s273'
        list10tks = ['s2141','s2142','s2143','s2144','s2145','s2146','s2147','s2148','s2149']
        # list10tk = ['jp49','jp50','jp51','jp52','jp53','jp54','jp55','jp56']#,'s273'
        # list10tk = ['jn4','jn5','jn1','jn2','jn3']
        list10tk = ['johnydang31','johnydang10','johnydang22']
        # self.upload_youtube('n')
        # self.init("fbfb")
        # self.initFace("fb10")
        # for item in list10tk:
        #     self.init(item)
        #     input("next")
        # self.download("f")

        # self.get_link_video_download_douyin_snaptik('n')
        # self.get_link_video_download_douyin1('n')
        # self.t1('n1')
        # self.t2('n2')
        # self.t3('n3')
        # self.t4('n4')
        # self.t5('n5')
        self.get_like("n")
    def initFace(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://www.facebook.com/profile.php?id=100027781594097')
        input("ok")
        self.driver.close()

    def yout(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://www.tiktok.com/upload?lang=en')
        sleep(2)
        self.driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/0_convert/v (1).mp4')
        sleep(6)
        self.driver.find_elements_by_css_selector(".btn-post")[0].click()
bot=InstagramBot()
bot.auto()
# bot.yout('bh181')


