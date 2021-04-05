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
        self.driver.get('https://business.facebook.com/creatorstudio/')
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

    def tiktok_post(self,filePath):

        self.driver = self.khoitao(filePath)
        self.driver.get('https://www.tiktok.com/upload/?lang=vi')
        for index in range(5,10):
            print("D:/tiktok/mo_hinh/n ({}).mp4".format(index))
            a= self.driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/tiktok/king_girl/x ({}).mp4'.format(index))
            self.driver.find_elements_by_css_selector(".DraftEditor-editorContainer")[0].click()
            keyboard.press_and_release('ctrl+v')
            sleep(10)
            self.driver.find_elements_by_css_selector(".btn-post")[0].click()
            sleep(2)
            self.driver.find_elements_by_css_selector(".modal-btn")[0].click()    
    def tiktok_post1(self,filePath):

        self.driver = self.khoitao(filePath)
        self.driver.get('https://www.tiktok.com/upload/?lang=vi')
        for index in range(1,10):
            print("D:/tiktok/mo_hinh/n ({}).mp4".format(index))
            a= self.driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/tiktok/mo_hinh/tt ({}).mp4'.format(index))
            self.driver.find_elements_by_css_selector(".DraftEditor-editorContainer")[0].click()
            keyboard.press_and_release('ctrl+v')
            sleep(15)
            self.driver.find_elements_by_css_selector(".btn-post")[0].click()
            sleep(6)
            self.driver.find_elements_by_css_selector(".modal-btn")[0].click()
    def tiktok_post2(self,filePath):
 
        self.driver = self.khoitao(filePath)
        self.driver.get('https://www.tiktok.com/upload/?lang=vi')
        for index in range(4,100):
            print("D:/tiktok/mo_hinh/n ({}).mp4".format(index))
            a= self.driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/tiktok/hinhnen/len ({}).mp4'.format(index))
            self.driver.find_elements_by_css_selector(".DraftEditor-editorContainer")[0].click()
            # keyboard.press_and_release('ctrl+v')
            sleep(22)
            self.driver.find_elements_by_css_selector(".btn-post")[0].click()
            sleep(8)
            self.driver.find_elements_by_css_selector(".modal-btn")[0].click()    
    def tiktok_post3(self,filePath):

        self.driver = self.khoitao(filePath)
        self.driver.get('https://www.tiktok.com/upload/?lang=vi')
        for index in range(1,10):
            print("D:/tiktok/mo_hinh/n ({}).mp4".format(index))
            a= self.driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/tiktok/king_man/len ({}).mp4'.format(index))
            self.driver.find_elements_by_css_selector(".DraftEditor-editorContainer")[0].click()
            keyboard.press_and_release('ctrl+v')
            sleep(15)
            self.driver.find_elements_by_css_selector(".btn-post")[0].click()
            sleep(6)
            self.driver.find_elements_by_css_selector(".modal-btn")[0].click()    
    def tiktok_post5(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://www.tiktok.com/upload/?lang=vi')
        # input("dv")
        sleep(3)
        for index in range(1,6):
            print("D:/tiktok/mo_hinh/anh ({}).mp4".format(index))
            sleep(3)
            self.driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/0_daopho/anh ({}).mp4'.format(index))
            sleep(1)
            self.driver.find_elements_by_css_selector(".DraftEditor-editorContainer")[0].click()
            keyboard.press_and_release('ctrl+v')
            sleep(15)
            self.driver.find_elements_by_css_selector(".btn-post")[0].click()
            sleep(6)
            self.driver.find_elements_by_css_selector(".modal-btn")[0].click()   
    def tiktok_post6(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://www.tiktok.com/upload/?lang=vi')
        # input("dv")
        sleep(3)
        for index in range(6,11):
            print("D:/tiktok/mo_hinh/anh ({}).mp4".format(index))
            sleep(3)
            self.driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/0_daopho/anh ({}).mp4'.format(index))
            sleep(1)
            self.driver.find_elements_by_css_selector(".DraftEditor-editorContainer")[0].click()
            keyboard.press_and_release('ctrl+v')
            sleep(15)
            self.driver.find_elements_by_css_selector(".btn-post")[0].click()
            sleep(6)
            self.driver.find_elements_by_css_selector(".modal-btn")[0].click()   
    def tiktok_post7(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://www.tiktok.com/upload/?lang=vi')
        # input("dv")
        sleep(3)
        for index in range(11,121):
            print("D:/tiktok/mo_hinh/anh ({}).mp4".format(index))
            sleep(3)
            # self.driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/0_x/anh ({}).mp4'.format(index))
            sleep(1)
            self.driver.find_elements_by_css_selector(".DraftEditor-editorContainer")[0].click()
            # keyboard.press_and_release('ctrl+v')
            sleep(2)
            self.driver.find_elements_by_css_selector(".switch")[0].click()
            sleep(2)
            self.driver.find_elements_by_css_selector(".date-picker-input")[0].click()
            sleep(2)
            self.driver.find_elements_by_css_selector(".day")[9].click()
            sleep(2)
            self.driver.find_elements_by_css_selector(".time-picker-input")[0].click()
            sleep(2)
            self.driver.find_elements_by_css_selector(".option-item")[19].click()
            sleep(15)
            # self.driver.find_elements_by_css_selector(".btn-post")[0].click()
            sleep(6)
            # self.driver.find_elements_by_css_selector(".modal-btn")[0].click()   
    def tiktok_post8(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://www.tiktok.com/upload/?lang=vi')
        # input("dv")
        sleep(3)
        for index in range(1,25):
            print("D:/tiktok/mo_hinh/anh ({}).mp4".format(index))
            sleep(3)
            self.driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/0_x/anh ({}).mp4'.format(index))
            sleep(1)
            self.driver.find_elements_by_css_selector(".DraftEditor-editorContainer")[0].click()
            keyboard.press_and_release('ctrl+v')
            sleep(15)
            self.driver.find_elements_by_css_selector(".btn-post")[0].click()
            sleep(6)
            self.driver.find_elements_by_css_selector(".modal-btn")[0].click()
    def auto(self):
        sleep(2)
        # self.tiktok_post('king_girl')
        # self.tiktok_post1('am_thuc')
        # self.tiktok_post2('may_nghien')
        # self.tiktok_post3('king_man')
        # self.tiktok_post4('nguyen_ns')#gáixinh #gáixinhtiktok #gái_đẹp #xuhuongtiktok #fyp
        # self.tiktok_post5('x')
        # sleep(2)
        # self.tiktok_post6('x1')
        # sleep(2)
        self.tiktok_post7('ggh')
        # sleep(2)
        # self.tiktok_post8('x5')
        # self.instagram_post_spiritual('post_spiritual')
        # self.instagram_post_love('post_love')
        # self.instagram_post_dog('post_dog')

        # self.instagram_follow_init('post_love')

bot=InstagramBot()
bot.auto()


#để lại cmt nhận xét nhé m.n #gáixinh #gáixinhtiktok #gái_đẹp #xuhuongtiktok #fyp
#gáixinh #gáixinhtiktok
 #gái_đẹp #xuhuongtiktok #fyp#gáixinh #gáixinhtiktok #gái_đẹp #xuhuongtiktok k
 #fyp#gáixinh #gáixinhtiktok #gái_đẹp #xuhuongtiktok #fyp#gáixinh #gáixinhtiktok 
 #gái_đẹp #xuhuongtiktok #fyp#gáixinh #gáixinhtiktok #gái_đẹp
 #xuhuongtiktok #fyp#gáixinh #gáixinhtiktok 
 #gái_đẹp #xuhuongtiktok #fyp#gáixinh #gáixinhtiktok #gái_đẹp #xuhuongtiktok #fyp
 #hotboy #traidep #đeptrai #xuhuongtiktok #trend 
 # con gái khi yêu thật lòng là không quan trọng đến ngoại hình
 #quá đỉnh,đã mắt #xuhuongtiktok #xuhuong2021 #fpy #trend
 #Đam mê Dj mà gia đình cấm =)) #xuhuongtiktok #xuhuong2021 #fpy #trend