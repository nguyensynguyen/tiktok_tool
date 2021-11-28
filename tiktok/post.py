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
import pyautogui
from datetime import time
import datetime
from fake_useragent import UserAgent
class InstagramBot():
    a = 11
    counts = 1
    day = 0
    gio = 19
    acounts = ""
    checkIs10Item = 1
    v = 1
    links = ""
    def khoitao(self,filePath):
        chrome_options = webdriver.ChromeOptions()
        ua = UserAgent()
        a = ua.random
        user_agent = ua.random
        # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36
        print(user_agent)
        chrome_options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36')
        chrome_options.add_argument(
        "user-data-dir=D:\\tiktok_tool\\tiktok\\"+filePath)
        # prefs = {
        #     "profile.managed_default_content_settings.images": 2
        # }
        # chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(
            './chromedriver', chrome_options=chrome_options)
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source":
                "const newProto = navigator.__proto__;"
                "delete newProto.webdriver;"
                "navigator.__proto__ = newProto;"
            })
        return self.driver

    def set_time(self):
        self.set_tg = random.randrange(8,15)
        sleep(self.set_tg)
    def init(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://www.tiktok.com/upload')
        input("ok")
        self.driver.close()
    def sholer(self,filePath):
        dem = 1
        try:
            self.driver = self.khoitao(filePath)
            self.driver.get('https://www.tiktok.com/upload/?lang=vi')
            sleep(3)
            pyautogui.click(x = 1038, y = 275 )
            for index in range(1,121):
                if self.day == 0:
                    for i in range(1,4):
                        print("D:/tiktok/mo_hinh/anh ({}).mp4".format(self.counts))
                        sleep(3)
                        self.driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/0_convert/v'+ str(self.v) +' ({}).mp4'.format(self.counts))
                        sleep(1)
                        self.driver.find_elements_by_css_selector(".DraftEditor-editorContainer")[0].click()
                        keyboard.press_and_release('ctrl+v')
                        sleep(10)
                        self.driver.find_elements_by_css_selector(".btn-post")[0].click()
                        sleep(5)
                        self.driver.find_elements_by_css_selector(".modal-btn")[0].click()
                        self.counts += 1

                else:
                    for i in range(1,4):
                        print("D:/tiktok/mo_hinh/anh ({}).mp4".format(self.counts))
                        sleep(1)
                        self.driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/0_convert/v'+str(self.v)+ ' ({}).mp4'.format(self.counts))
                        sleep(3)
                        self.driver.find_elements_by_css_selector(".DraftEditor-editorContainer")[0].click()
                        sleep(1)
                        keyboard.press_and_release('ctrl+v')
                        # sleep(4)
                        sleep(10)
                        self.driver.find_elements_by_css_selector(".switch")[0].click()
                        sleep(2)
                        self.driver.find_elements_by_css_selector(".date-picker-input")[0].click()
                        sleep(2)
                        #sang bên
                        # self.driver.find_elements_by_css_selector(".arrow")[1].click()
                        # sleep(1)
                        self.driver.find_elements_by_css_selector(".valid")[self.day].click()
                        sleep(2)
                        self.driver.find_elements_by_css_selector(".time-picker-input")[0].click()
                        sleep(2)
                        if dem == 1:
                            self.driver.find_elements_by_css_selector(".option-item")[self.gio].click()
                        if dem == 2:
                            self.driver.find_elements_by_css_selector(".option-item")[self.gio].click()
                            sleep(1)
                            self.driver.find_elements_by_css_selector(".option-item")[self.gio - 2].click()
                            # sleep(1)
                            # self.driver.find_elements_by_css_selector(".option-item")[gio - 6].click()
                            # sleep(1)
                            # self.driver.find_elements_by_css_selector(".option-item")[gio - 9].click()

                        if dem == 3:
                            self.driver.find_elements_by_css_selector(".option-item")[self.gio].click()
                            sleep(1)
                            self.driver.find_elements_by_css_selector(".option-item")[self.gio + 2].click()
                            # sleep(1)
                            # self.driver.find_elements_by_css_selector(".option-item")[gio + 6].click()
                            # sleep(1)
                            # self.driver.find_elements_by_css_selector(".option-item")[gio - 8].click()

                        sleep(2)
                        self.driver.find_elements_by_css_selector(".tiktok-btn-pc-primary")[0].click()
                        sleep(6)
                        self.driver.find_elements_by_css_selector(".tiktok-modal__modal-button")[2].click()
                        sleep(2)
                        dem += 1
                        self.counts += 1
                self.day += 1
                dem = 1


                # self.driver.find_elements_by_css_selector(".modal-btn")[0].click()   
        except:
            self.driver.close()
            if self.counts <= 6:
                datetime_object = datetime.datetime.now()
                print(datetime_object.hour)
                if datetime_object.hour - self.gio >= 2:
                    val_gio = input("nhap giờ :")
                    self.gio = int(val_gio)
                self.sholer(filePath)
            else:
                self.counts = 1
                self.day = 0
                print("upload success")

    def sholers2(self,filePath):
        dem = 1
        try:
            self.driver = self.khoitao(filePath)
            self.driver.get('https://www.tiktok.com/upload/?lang=vi')
            sleep(3)
            pyautogui.click(x = 1038, y = 275 )
            for index in range(1,121):
                if self.day == 0:
                    for i in range(1,4):
                        print("D:/tiktok/mo_hinh/anh ({}).mp4".format(self.counts))
                        sleep(3)
                        self.driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/0_convert/v'+str(self.v)+' ({}).mp4'.format(self.counts))
                        sleep(1)
                        self.driver.find_elements_by_css_selector(".DraftEditor-editorContainer")[0].click()
                        keyboard.press_and_release('ctrl+v')
                        sleep(10)
                        self.driver.find_elements_by_css_selector(".btn-post")[0].click()
                        sleep(5)
                        self.driver.find_elements_by_css_selector(".modal-btn")[0].click()
                        self.counts += 1

                else:
                    for i in range(1,4):
                        print("D:/tiktok/mo_hinh/anh ({}).mp4".format(self.counts))
                        sleep(1)
                        self.driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/0_convert/v'+str(self.v)+ ' ({}).mp4'.format(self.counts))
                        sleep(3)
                        self.driver.find_elements_by_css_selector(".DraftEditor-editorContainer")[0].click()
                        sleep(1)
                        keyboard.press_and_release('ctrl+v')
                        # sleep(4)
                        sleep(10)
                        self.driver.find_elements_by_css_selector(".switch")[0].click()
                        sleep(2)
                        self.driver.find_elements_by_css_selector(".date-picker-input")[0].click()
                        sleep(2)
                        #sang bên
                        # self.driver.find_elements_by_css_selector(".arrow")[1].click()
                        # sleep(1)
                        #
                        self.driver.find_elements_by_css_selector(".valid")[self.day].click()
                        sleep(2)
                        self.driver.find_elements_by_css_selector(".time-picker-input")[0].click()
                        sleep(2)
                        if dem == 1:
                            self.driver.find_elements_by_css_selector(".option-item")[self.gio].click()
                        if dem == 2:
                            self.driver.find_elements_by_css_selector(".option-item")[self.gio].click()
                            sleep(1)
                            self.driver.find_elements_by_css_selector(".option-item")[self.gio - 2].click()
                            # sleep(1)
                            # self.driver.find_elements_by_css_selector(".option-item")[gio - 6].click()
                            # sleep(1)
                            # self.driver.find_elements_by_css_selector(".option-item")[gio - 9].click()

                        if dem == 3:
                            self.driver.find_elements_by_css_selector(".option-item")[self.gio].click()
                            sleep(1)
                            self.driver.find_elements_by_css_selector(".option-item")[self.gio + 2].click()
                            # sleep(1)
                            # self.driver.find_elements_by_css_selector(".option-item")[gio + 6].click()
                            # sleep(1)
                            # self.driver.find_elements_by_css_selector(".option-item")[gio - 8].click()

                        sleep(2)
                        self.driver.find_elements_by_css_selector(".tiktok-btn-pc-primary")[2].click()
                        sleep(6)
                        self.driver.find_elements_by_css_selector(".tiktok-modal__modal-button")[2].click()
                        sleep(2)
                        dem += 1
                        self.counts += 1
                self.day += 1
                dem = 1


        except:
            self.driver.close()
            if self.counts <= 6:
                print("ex")
                datetime_object = datetime.datetime.now()
                if datetime_object.hour - self.gio >= 2:
                    val_gio = input("nhap giờ :")
                    self.gio = int(val_gio)
                self.sholer(filePath)
            else:
                print("upload success")
                self.counts = 1
                self.day = 0
        # if self.counts > 6:
        #     self.counts = 1
        #     self.day = 0
        #     print("ok")



    def uploadFakeIp(self,filePath):
        dem = 1
        try:
            self.driver = self.khoitao(filePath)
            self.driver.get('https://www.tiktok.com/upload/?lang=vi')
            input("conti")
            sleep(3)
            # pyautogui.click(x = 1038, y = 275 )
            for index in range(1,121):
                if self.day == 0:
                    for i in range(1,4):
                        print("D:/tiktok/mo_hinh/anh ({}).mp4".format(self.counts))
                        sleep(3)
                        self.driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/0_convert/v'+ str(self.v) +' ({}).mp4'.format(self.counts))
                        sleep(1)
                        self.driver.find_elements_by_css_selector(".DraftEditor-editorContainer")[0].click()
                        keyboard.press_and_release('ctrl+v')
                        sleep(10)
                        self.driver.find_elements_by_css_selector(".btn-post")[0].click()
                        sleep(5)
                        self.driver.find_elements_by_css_selector(".modal-btn")[0].click()
                        self.counts += 1

                else:
                    for i in range(1,4):
                        print("D:/tiktok/mo_hinh/anh ({}).mp4".format(self.counts))
                        sleep(1)
                        self.driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/0_convert/v'+str(self.v)+ ' ({}).mp4'.format(self.counts))
                        sleep(3)
                        self.driver.find_elements_by_css_selector(".DraftEditor-editorContainer")[0].click()
                        sleep(1)
                        keyboard.press_and_release('ctrl+v')
                        # sleep(4)
                        sleep(10)
                        self.driver.find_elements_by_css_selector(".switch")[0].click()
                        sleep(2)
                        self.driver.find_elements_by_css_selector(".date-picker-input")[0].click()
                        sleep(2)
                        #sang bên
                        # self.driver.find_elements_by_css_selector(".arrow")[1].click()
                        # sleep(1)
                        self.driver.find_elements_by_css_selector(".valid")[self.day].click()
                        sleep(2)
                        self.driver.find_elements_by_css_selector(".time-picker-input")[0].click()
                        sleep(2)
                        if dem == 1:
                            self.driver.find_elements_by_css_selector(".option-item")[self.gio].click()
                        if dem == 2:
                            self.driver.find_elements_by_css_selector(".option-item")[self.gio].click()
                            sleep(1)
                            self.driver.find_elements_by_css_selector(".option-item")[self.gio - 2].click()
                            # sleep(1)
                            # self.driver.find_elements_by_css_selector(".option-item")[gio - 6].click()
                            # sleep(1)
                            # self.driver.find_elements_by_css_selector(".option-item")[gio - 9].click()

                        if dem == 3:
                            self.driver.find_elements_by_css_selector(".option-item")[self.gio].click()
                            sleep(1)
                            self.driver.find_elements_by_css_selector(".option-item")[self.gio + 2].click()
                            # sleep(1)
                            # self.driver.find_elements_by_css_selector(".option-item")[gio + 6].click()
                            # sleep(1)
                            # self.driver.find_elements_by_css_selector(".option-item")[gio - 8].click()

                        sleep(2)
                        self.driver.find_elements_by_css_selector(".btn-post")[0].click()
                        sleep(6)
                        self.driver.find_elements_by_css_selector(".tiktok-modal__modal-button")[2].click()
                        sleep(2)
                        dem += 1
                        self.counts += 1
                self.day += 1
                dem = 1


                # self.driver.find_elements_by_css_selector(".modal-btn")[0].click()   
        except:
            self.driver.close()
            if self.counts <= 6:
                datetime_object = datetime.datetime.now()
                print(datetime_object.hour)
                if datetime_object.hour - self.gio >= 2:
                    val_gio = input("nhap giờ :")
                    self.gio = int(val_gio)
                self.sholer(filePath)
            else:
                self.counts = 1
                self.day = 0
                print("upload success")

    def get_link(self,filePath):
        #https://www.douyin.com/user/MS4wLjABAAAAEb3guwHJqmqYN5rwB8vOaDLB2QA8diTQB5bMZDigeGqCKx36guUivB703C-4v1iD?enter_method=video_title&author_id=1833615318062676&group_id=6969464724211764494&log_pb=%7B%22impr_id%22%3A%2220210630170520010212026091380310E0%22%7D&enter_from=main_page
        url = input("nhap link profile: ")
        urls = url.split("?")[0].split("/")[4]
        self.link = urls
        self.get_link_acount(filePath)
        
    def get_link_acount(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://www.douyin.com/user/{}'.format(self.link))
        input("ff")
        save_list_link=open('link_douyin.txt','w')
        sleep(2)

        read1 = self.driver.find_elements_by_css_selector('._787337747252a601a979b6885202ecb6-scss')
        print(len(read1))
        for item in range(0,33): #len(read1)
            # if (read1[item].get_attribute('href').__contains__('video')):
               save_list_link.write(read1[item].get_attribute('href') +"\n")
    

        # list_link.close()
        self.driver.close()
    def get_link_profile(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://www.douyin.com/user/MS4wLjABAAAAX1rLy-8kpfYjUXK8_cXQOr3FV6-GhZvqw_DLkIR0IwlQu7dwdbY084raF8kXyS5M ')
        input("ff")
        save_list_link=open('link_douyin.txt','w')
        sleep(2)

        read1 = self.driver.find_elements_by_css_selector('._787337747252a601a979b6885202ecb6-scss')
        print(len(read1))
        for item in range(0,len(read1)): #len(read1)
            # if (read1[item].get_attribute('href').__contains__('video')):
               rs_str_spl = read1[item].get_attribute('href').split('?')[0].split('/')[4]
               save_list_link.write(rs_str_spl +"\n")

    def yout(self,filePath):
        self.driver = self.khoitao(filePath)
        self.driver.get('https://www.tiktok.com/upload?lang=en')
        sleep(2)
        # self.driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/0_convert/v ({}).mp4'.format(self.counts))
        # self.driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/0_convert/v (1).mp4')

    def get_like(self,filePath):
        self.driver = self.khoitao('n')
        self.driver.get('https://www.douyin.com/recommend')
        sl = input("nhâp số lượng cần like:")

        for i in range(0,int(sl)):
            self.driver.find_elements_by_css_selector('.aa56c3391b648160ab6b643fc006dfa1-scss .png')[5].click()
            sleep(1)
            self.driver.find_elements_by_css_selector('.xgplayer-playswitch-next')[0].click()
            set_time()

    def get_link_profile(self,filePath):

        self.driver = self.khoitao(filePath)
        self.driver.get('https://www.douyin.com/user/MS4wLjABAAAAX1rLy-8kpfYjUXK8_cXQOr3FV6-GhZvqw_DLkIR0IwlQu7dwdbY084raF8kXyS5M ')
        input("ff")
        save_list_link=open('link_douyin.txt','w')
        sleep(2)

        read1 = driver.find_elements_by_css_selector('._787337747252a601a979b6885202ecb6-scss')
        print(len(read1))
        for item in range(0,len(read1)):
            rs_str_spl = read1[item].get_attribute('href').split('?')[0].split('/')[4]
            save_list_link.write(rs_str_spl +"\n")

    def sholer1(self,filePath,sl):
        try:
            self.driver = self.khoitao(filePath)
            self.driver.get('https://www.tiktok.com/upload')
            print("checkIs10Item:" + str(self.checkIs10Item))
            print("count:" + str(self.counts))#gáixinh #gáixinhtiktok #gái_đẹp #xuhuongtiktok #fyp#gáixinh #gáixinhtiktok #gái_đẹp #xuhuongtiktok #fyp
            sleep(3)
            # pyautogui.click(x = 1038, y = 275 )
            for i in range(self.checkIs10Item,int(sl) + 1):
                print("D:/tiktok/mo_hinh/anh ({}).mp4".format(self.counts))
                sleep(3)
                self.driver.find_elements_by_css_selector(".upload-btn-input")[0].send_keys('D:/0_convert/#hotgirl ({}).mp4'.format(self.counts))
                sleep(4)
                self.driver.find_elements_by_css_selector(".DraftEditor-editorContainer")[0].click()
                # keyboard.press_and_release('ctrl+v')
                sleep(9)
                try:
                    self.driver.find_elements_by_css_selector(".tiktok-btn-pc")[2].click()
                except:
                    self.driver.find_elements_by_css_selector(".tiktok-btn-pc")[1].click()
                sleep(5)
                self.driver.find_elements_by_css_selector(".modal-btn")[0].click()
                self.counts += 1
                self.checkIs10Item += 1
        except:
            print("exx")
            self.driver.close()
            if self.checkIs10Item >int(sl):
                self.checkIs10Item = 1
            else:
                print("next")
                self.sholer1(filePath,sl)
        if self.checkIs10Item > int(sl):
            self.checkIs10Item = 1

            # self.driver.find_elements_by_css_selector(".modal-btn")[0].click()   
        # self.driver.close()
    def auto(self):

        s10k = ['bh55','bh60','bh10','jp21','jp6','jp4','jh10']

        dabatkt = ['bh56','bh54','bh103','bh12','bh152','bh57','nguyentrangs2115','nguyentrangs2138','nguyentrangs2105'
        ,'jp20','bh68','bh59','bh23','bh90']

        taikhoanok = ['bh21','bh90','bh58','bh8','','bh17','bh53','bh66','bh11','bh134','','bh2','bh14','bh23'
        ,'bh9','bh153','bh127','bh27','bh174']
        
        xuhuongchinhtri = ['bh158s']
        
        vua_up = ['bh172','bh169','bh170','bh171','bh15','bgh4',
        'bh38','bh39','bh40','bh41','bh42','bh43','bh45','bh46','bh47','bh48','bh24','bh25','bighoa151','bh140','bh127','nguyentsx',
        'smallhoa1s','bh157','bh159','bh125','bh173','bh127','nguyentsx','bh168'
        ,'bighoa151','bh174','bh175','bh143','bh183','bh184','','bh131','bh15','bh22','bh43','bh47','bh48']
       
        hot = ['bh12']
        nick10p = ['bh121','bh127','bh129','bh139']
        nickmoi = []
        list10tks = ['bh160','bh191',
                    'bh49','bh50','bh51','bh52',
            'bh61','bh62','bh64','bh65','bh67',
                    'bh69','bh71','bh72','bh110','bh111','bh120','bh135',
                    'bh137','bh139','bh141','bh144']

        nickloi = ['bh140','bh23','bh58']

        login = ['bh9','bh11','bh66','jp6', 'bh153','bh174','bh27',
        'bh127','bh134','bh137','bh183','bh191','bh186','bh188','bh192','bh140','bh23','bh58','bh182','jp6',
        ]
        #nt2105
        jp = ['jp6' ]
        nt = ['bh153','bh174','bh66','jp6',
        'bh127','bh134','bh137','bh186','bh188','bh192','bh140','bh182','bh191'
        ,'bh17','bh58','bh23','bh53','bh191','bh68','bh59','bh10',
        'bh21','bh183','bh58','bh23',]

        newlogin = ['linhpis1','bh200','bh21','bh183','bh53','bh11','bh10','bh17']

        bts = ['bts10','bts11','bts13','bts16','bts17','bts18','bts19','bts20']

        us =['nus24','test2','nus5','nus8','nus9','nus14','nus10'] #girl
        us1 =['nus11','nus12','nus13','nus15','nus16','nus17','nus18']
        us2 =['nus20','nus21','nus22','nus23']
        #'nbg1','nbg2','nbg3','test2','nus5','nus8','nus9','nus10'
        ok = ['jp3','jp4','jp6','jh12','bh114','jh32'
        ,'bh183','bh66','bh9','bh53','bh2','bh8','bh174']
        oks = ['bh55','bh60','bh191','bh8','bh183']
        ngns = ['ns1','ns2','ns3','bh66','bh21','bh17','bh9','bh53','bh2','bh8','bh183']
        te = ['nus39','nus40','nus48','nus42','nus59','nus60','nus61','nus62']
#'jp3','jp4','jp21','jp6,'jh12','bh191','bh114'
#'nus9','nus5','nus50','nus8','nus40','nus12','nus51','nus52','nbg1','nbg2','nbg3','test2','nus16','nus14',
# 'nus57','nus9','nus50','nus8','nus40','nus12','nus51','nus52','nus5','nbg1','nbg2','nbg3','test2','nus16','nus14'
        list10tk = ['nus40s','nus50s','nus5s','nus8s','nus14s','nus62s']
#nus50,nus5,nus8,
        while True:
            print("\t1.Up video liên tục nhiều acount(1 nick 3-10 video)\n")
            print("\t2.Đăng nhập\n")
            print("\t3.Get like\n")
            print("\t4.Get link profile\n")
            mod = input("chon mode :")

            if mod == "1":
                val_sl = input("nhập số lượng video up trên 1 acount : ")
                for item in list10tk:
                    print(item)
                    self.sholer1(item,val_sl)

            if mod == "2":
                value = input("nhap acount: ")
                self.init(value)

            if mod == "3":
                self.get_like('n')

            if mod == "4":
                self.get_link_profile('n')

                


bot=InstagramBot()
bot.auto()
# list10tk =['bh2','bh8','bh9','bh10','bh11','bh12','bh14','bh15','bh17','bh21','bh22','bh23','bh24','bh25','bh27',
#                     'bgh4','bh38','bh39','bh40','bh41','bh42']
# bot.init('nus62s')
#'bh12','bh152','bh57','bh54','nguyentrangs2115','nguyentrangs2138'

#Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36
#để lại cmt nhận xét nhé m.n #gáixinh #gáixinhtiktok #gái_đẹp #xuhuongtiktok #fyp
#gáixinh #gáixinhtiktok
 #gái_đẹp #xuhuongtiktok #fyp #gáixinh #gáixinhtiktok #gái_đẹp #xuhuongtiktok k
 #fyp#gáixinh #gáixinhtiktok #gái_đẹp #xuhuongtiktok #fyp #gáixinh #gáixinhtiktok
 #gái_đẹp #xuhuongtiktok #fyp#gáixinh #gáixinhtiktok #gái_đẹp
 #xuhuongtiktok #fyp#gáixinh #gáixinhtiktok 
 #gái_đẹp #xuhuongtiktok #fyp#gáixinh #gáixinhtiktok #gái_đẹp #xuhuongtiktok #fyp#trendquá đẹp #xuhuongtiktok #xuhuong2021 #fpy #trend
 #hotboy #traidep #đeptrai #xuhuongtiktok #trend 
 # con gái khi yêu thật lòng là không quan trọng đến ngoại hình
 #quá đỉnh,đã mắt #xuhuongtiktok #xuhuong2021 #fpy #trendquá đẹp #xuhuongtiktok #xuhuong2021 #fpy #trend
 # võ công thiếu lâm tự #xuhuongtiktok #xuhuong2021 #fpy #trendquá đẹp #xuhuongtiktok #xuhuong2021 #fpy #trend
 #hotboy #traidep_gaixinh #traideptrungquoc #traidep 
# hài thực sự #xuhuongtiktok #xuhuong2021 #fpy #trend#gái_đẹp #xuhuongtiktok #fyp #gáixinh #gáixinhtiktok

#thoitrangnu #vaydep #xuhuong #xuhuongthoitrang #YeuVietNam
#gáixinhtiktok #gái_đẹp #xuhuongtiktok #fyp #gáixinh #gáixinhtiktok
#xuhuongtiktok #xuhuong2021 #fpy #gáixinhtiktok
#hotgirl #girls #fyp