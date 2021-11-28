import pyautogui
from time import sleep
import keyboard
import random
import threading
# keyboard.press_and_release('WIN + v')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pynput
import time
import requests
import pyperclip
import clipboard
from decimal import Decimal
count = 0
break_program = False
pause_key = False
pasuse_keys = 0
pasuse_key = pynput.keyboard.KeyCode(char = 'p')
flag = 30
def set_time():
  set_tg = random.randrange(2,5)
  sleep(set_tg)
def set_times():
  set_tg = random.randrange(1,2)
  sleep(set_tg)
listMusic = [
  {"x" : 210, "y" : 115},
  {"x" : 209, "y" : 134},
  {"x" : 209, "y" : 156},
  {"x" : 212, "y" : 175},
  {"x" : 212, "y" : 198},
  {"x" : 212, "y" : 223},
  {"x" : 218, "y" : 241},
  {"x" : 213, "y" : 262},
  {"x" : 211, "y" : 279},
  {"x" : 212, "y" : 301},
  {"x" : 211, "y" : 321},
  {"x" : 214, "y" : 343},
  {"x" : 221, "y" : 368},
  {"x" : 211, "y" : 390},
  {"x" : 214, "y" : 410},
  {"x" : 214, "y" : 427},
  {"x" : 209, "y" : 451},
  {"x" : 210, "y" : 470},
  {"x" : 212, "y" : 492},
  {"x" : 212, "y" : 511},
  {"x" : 214, "y" : 533},
  {"x" : 214, "y" : 553},
  {"x" : 212, "y" : 576},
  {"x" : 208, "y" : 597},
  {"x" : 216, "y" : 619},
  {"x" : 282, "y" : 114},
  {"x" : 287, "y" : 135},
  {"x" : 280, "y" : 156},
  {"x" : 280, "y" : 174},
  {"x" : 282, "y" : 200},
  {"x" : 278, "y" : 217},
  {"x" : 275, "y" : 239},
  {"x" : 276, "y" : 259},
  {"x" : 280, "y" : 281},
  {"x" : 283, "y" : 299},
  {"x" : 287, "y" : 323},
  {"x" : 282, "y" : 346},
  {"x" : 285, "y" : 366},
  {"x" : 274, "y" : 388},
  {"x" : 277, "y" : 407},
  {"x" : 277, "y" : 427},
  {"x" : 280, "y" : 448},
  {"x" : 279, "y" : 470},
  {"x" : 286, "y" : 493},
  {"x" : 285, "y" : 510},
  {"x" : 279, "y" : 533},
  {"x" : 283, "y" : 553},
  {"x" : 283, "y" : 578},
  {"x" : 287, "y" : 596},
  {"x" : 278, "y" : 617},
  {"x" : 356, "y" : 112},
  {"x" : 356, "y" : 134},
  {"x" : 350, "y" : 156},
  {"x" : 351, "y" : 174},
  {"x" : 351, "y" : 197},
  {"x" : 350, "y" : 215},
  {"x" : 349, "y" : 237},
  {"x" : 350, "y" : 261},
  {"x" : 349, "y" : 281},
  {"x" : 346, "y" : 301},
  {"x" : 341, "y" : 325},
  {"x" : 341, "y" : 344},
  {"x" : 338, "y" : 366},
  {"x" : 343, "y" : 386},
  {"x" : 342, "y" : 408},
  {"x" : 345, "y" : 429},
  {"x" : 346, "y" : 450},
  {"x" : 347, "y" : 470},
  {"x" : 349, "y" : 492},
  {"x" : 347, "y" : 514},
  {"x" : 347, "y" : 534},
  {"x" : 348, "y" : 554},
  {"x" : 348, "y" : 576},
  {"x" : 346, "y" : 599},
  {"x" : 350, "y" : 617},
  {"x" : 420, "y" : 113},
  {"x" : 425, "y" : 133},
  {"x" : 424, "y" : 154},
  {"x" : 424, "y" : 175},
  {"x" : 424, "y" : 197},
  {"x" : 424, "y" : 217},
  {"x" : 424, "y" : 237},
  {"x" : 424, "y" : 259},
  {"x" : 421, "y" : 280},
  {"x" : 420, "y" : 303},
  {"x" : 419, "y" : 318},
  {"x" : 421, "y" : 342},
  {"x" : 421, "y" : 365},
  {"x" : 424, "y" : 383},
  {"x" : 422, "y" : 406},
  {"x" : 421, "y" : 428},
  {"x" : 419, "y" : 448},
  {"x" : 419, "y" : 467},
  {"x" : 420, "y" : 491},
  {"x" : 420, "y" : 513},
  {"x" : 420, "y" : 532},
  {"x" : 426, "y" : 556},
  {"x" : 419, "y" : 576},
  {"x" : 417, "y" : 595},
  {"x" : 414, "y" : 616},
  {"x" : 485, "y" : 114},
  {"x" : 485, "y" : 133},
  {"x" : 486, "y" : 154},
  {"x" : 490, "y" : 175},
  {"x" : 489, "y" : 197},
  {"x" : 488, "y" : 217},
  {"x" : 489, "y" : 239},
  {"x" : 489, "y" : 258},
  {"x" : 492, "y" : 278},
  {"x" : 488, "y" : 301},
  {"x" : 482, "y" : 321},
  {"x" : 479, "y" : 344},
  {"x" : 479, "y" : 363},
  {"x" : 479, "y" : 388},
  {"x" : 482, "y" : 406},
  {"x" : 481, "y" : 425},
  {"x" : 476, "y" : 451},
  {"x" : 479, "y" : 469},
  {"x" : 477, "y" : 494},
  {"x" : 483, "y" : 512},
  {"x" : 489, "y" : 532},
  {"x" : 484, "y" : 553},
  {"x" : 480, "y" : 575},
  {"x" : 479, "y" : 598},
  {"x" : 479, "y" : 613},
  {"x" : 570, "y" : 112},
  {"x" : 562, "y" : 134},
  {"x" : 567, "y" : 156},
  {"x" : 568, "y" : 173},
  {"x" : 568, "y" : 197},
  {"x" : 568, "y" : 217},
  {"x" : 567, "y" : 240},
  {"x" : 566, "y" : 260},
  {"x" : 565, "y" : 279},
  {"x" : 566, "y" : 299},
  {"x" : 564, "y" : 326},
  {"x" : 563, "y" : 344},
  {"x" : 568, "y" : 363},
  {"x" : 566, "y" : 389},
  {"x" : 568, "y" : 410},
  {"x" : 572, "y" : 425},
  {"x" : 572, "y" : 448},
  {"x" : 571, "y" : 466},
  {"x" : 568, "y" : 493},
  {"x" : 565, "y" : 515},
  {"x" : 561, "y" : 534},
  {"x" : 560, "y" : 554},
  {"x" : 554, "y" : 573},
  {"x" : 558, "y" : 595},
  {"x" : 565, "y" : 616},
  {"x" : 646, "y" : 115},
  {"x" : 644, "y" : 130},
  {"x" : 648, "y" : 153},
  {"x" : 646, "y" : 177},
  {"x" : 635, "y" : 198},
  {"x" : 635, "y" : 215},
  {"x" : 635, "y" : 241},
  {"x" : 633, "y" : 262},
  {"x" : 633, "y" : 280},
  {"x" : 635, "y" : 305},
  {"x" : 634, "y" : 324},
  {"x" : 634, "y" : 343},
  {"x" : 634, "y" : 366},
  {"x" : 633, "y" : 384},
  {"x" : 633, "y" : 407},
  {"x" : 633, "y" : 428},
  {"x" : 631, "y" : 449},
  {"x" : 627, "y" : 472},
  {"x" : 627, "y" : 496},
  {"x" : 627, "y" : 512},
  {"x" : 626, "y" : 537},
  {"x" : 624, "y" : 555},
  {"x" : 627, "y" : 577},
  {"x" : 628, "y" : 597},
  {"x" : 626, "y" : 616},
  {"x" : 705, "y" : 114},
  {"x" : 704, "y" : 134},
  {"x" : 705, "y" : 155},
  {"x" : 706, "y" : 177},
  {"x" : 703, "y" : 198},
  {"x" : 702, "y" : 218},
  {"x" : 705, "y" : 239},
  {"x" : 704, "y" : 261},
  {"x" : 702, "y" : 283},
  {"x" : 702, "y" : 307},
  {"x" : 699, "y" : 322},
  {"x" : 703, "y" : 347},
  {"x" : 703, "y" : 364},
  {"x" : 698, "y" : 387},
  {"x" : 703, "y" : 404},
  {"x" : 707, "y" : 425},
  {"x" : 708, "y" : 451},
  {"x" : 701, "y" : 470},
  {"x" : 701, "y" : 490},
  {"x" : 705, "y" : 512},
  {"x" : 706, "y" : 533},
  {"x" : 708, "y" : 555},
  {"x" : 704, "y" : 573},
  {"x" : 708, "y" : 594},
  {"x" : 709, "y" : 614},
  {"x" : 779, "y" : 115},
  {"x" : 776, "y" : 134},
  {"x" : 777, "y" : 154},
  {"x" : 778, "y" : 175},
  {"x" : 778, "y" : 197},
  {"x" : 774, "y" : 216},
  {"x" : 776, "y" : 239},
  {"x" : 777, "y" : 260},
  {"x" : 777, "y" : 279},
  {"x" : 777, "y" : 303},
  {"x" : 775, "y" : 323},
  {"x" : 775, "y" : 345},
  {"x" : 775, "y" : 363},
  {"x" : 776, "y" : 385},
  {"x" : 772, "y" : 407},
  {"x" : 772, "y" : 427},
  {"x" : 775, "y" : 452},
  {"x" : 775, "y" : 468},
  {"x" : 778, "y" : 489},
  {"x" : 778, "y" : 509},
  {"x" : 775, "y" : 532},
  {"x" : 775, "y" : 557},
  {"x" : 777, "y" : 573},
  {"x" : 776, "y" : 598},
  {"x" : 776, "y" : 614},
  {"x" : 860, "y" : 113},
  {"x" : 851, "y" : 134},
  {"x" : 849, "y" : 152},
  {"x" : 849, "y" : 174},
  {"x" : 849, "y" : 197},
  {"x" : 848, "y" : 219},
  {"x" : 848, "y" : 236},
  {"x" : 849, "y" : 259},
  {"x" : 849, "y" : 279},
  {"x" : 850, "y" : 301},
  {"x" : 852, "y" : 324},
  {"x" : 855, "y" : 346},
  {"x" : 855, "y" : 367},
  {"x" : 853, "y" : 385},
  {"x" : 851, "y" : 407}
]
def khoitao(filePath):
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument(
  "user-data-dir=D:\\tiktok_tool\\tiktok\\"+filePath)

  # prefs = {
  #     "profile.managed_default_content_settings.images": 2
  # }
  # chrome_options.add_experimental_option("prefs", prefs)
  driver = webdriver.Chrome(
      './chromedriver', chrome_options=chrome_options)
  return driver
def get_like(filePath):
  driver = khoitao(filePath)
  driver.get('https://www.douyin.com/recommend')
  sl = input("nhâp số lượng cần like:")
  save_list_link=open('save_link_douyin.txt','w')
  list_link=open('link_douyin.txt','r',encoding="utf-8")
  for i in range(0,int(sl)):
    pyautogui.click(x = 1300, y = 601 )
    sleep(2)
    pyautogui.click(x = 1209, y = 592 )
    text = clipboard.paste()
      
      # print(read)
    for item in text.split(sep=' '):
        # item.split(sep = ' ')
        if (item.__contains__('http')):
            links = requests.get(item)
            save_list_link.write(links.url.split(sep='?')[0].split('/')[4] +"\n")

        else:
            continue
    sleep(1)
    driver.find_elements_by_css_selector('.xgplayer-playswitch-next')[0].click()
      # set_time()
save_list_link=open('link_douyin.txt','w')

def get_link_profile_codition(filePath):
  driver = khoitao(filePath)
  driver.get('https://www.douyin.com/user/MS4wLjABAAAAX1rLy-8kpfYjUXK8_cXQOr3FV6-GhZvqw_DLkIR0IwlQu7dwdbY084raF8kXyS5M')
  # save_list_link.write("sxd" +"\n")
  sl =  input("nhap điều kiện :")
  sleep(2)
  read1 = driver.find_elements_by_css_selector('._787337747252a601a979b6885202ecb6-scss')
  sp = driver.find_elements_by_css_selector('._4c7753003fcad283963e6dd5d4aa5f1e-scss span')
  for item in range(0,len(read1)):
      # if (read1[item].get_attribute('href').__contains__('video')):
      if (sp[item].text.__contains__('w')):
        totalLike = sp[item].text.split('w')[0]
        if (Decimal(totalLike) >= Decimal(sl)):
          print(sp[item].text)
          rs_str_spl = read1[item].get_attribute('href').split('?')[0].split('/')[4]
          save_list_link.write(rs_str_spl+"\n")
def get_link_profile(filePath):
  driver = khoitao(filePath)
  driver.get('https://www.douyin.com/user/MS4wLjABAAAAX1rLy-8kpfYjUXK8_cXQOr3FV6-GhZvqw_DLkIR0IwlQu7dwdbY084raF8kXyS5M')
  # save_list_link.write("sxd" +"\n")
  input("f")
  sleep(2)
  read1 = driver.find_elements_by_css_selector('._787337747252a601a979b6885202ecb6-scss')
  for item in range(0,len(read1)):
    rs_str_spl = read1[item].get_attribute('href').split('?')[0].split('/')[4]
    save_list_link.write(rs_str_spl+"\n")
  print(len(read1))        
def get_link_profile_tiktok(filePath):
  link = input("nhap link profile tiktok: ")
  driver = khoitao(filePath)
  driver.get(link)
  # save_list_link.write("sxd" +"\n")
  input("ff")
  sleep(2)
  read1 = driver.find_elements_by_css_selector('.jsx-2261688415 a')
  print(len(read1))
  for item in range(0,len(read1)): #len(read1)
      # if (read1[item].get_attribute('href').__contains__('video')):
         rs_str_spl = read1[item].get_attribute('href').split('@')[1].split('/')[2]
         print(rs_str_spl)
         save_list_link.write(rs_str_spl+"\n")

def get_like_conditon(filePath):
  driver = khoitao(filePath)
  driver.get('https://www.douyin.com/recommend')
  sl = input("nhâp số lượng video:")
  like_cd = input("nhâp số lượng like:")
  save_list_link=open('save_link_douyin.txt','w')
  list_link=open('link_douyin.txt','r',encoding="utf-8")
  for i in range(0,int(sl)):
    like = driver.find_elements_by_css_selector('._843fa5dac3fe5b1974f1922fac115b82-scss')[0]
    if (like.text.__contains__('w')):
      totalLike = like.text.split('w')[0]
      if (Decimal(totalLike) >= Decimal(like_cd)):
        print(totalLike)
        pyautogui.click(x = 1300, y = 601 )
        sleep(2)
        pyautogui.click(x = 1209, y = 592 )
        texts = clipboard.paste()
          
          # print(read)
        for item in texts.split(sep=' '):
            # item.split(sep = ' ')
            if (item.__contains__('http')):
                links = requests.get(item)
                save_list_link.write(links.url.split(sep='?')[0].split('/')[4] +"\n")

            else:
                continue
    sleep(1)
    driver.find_elements_by_css_selector('.xgplayer-playswitch-next')[0].click()
      # set_time()

def auto_post():
  global flag
  global count
  xxx =input("nhap sl: ")
  flag =int(xxx)
  for x in range(1000):
    # input("\nnext\n")
    # print(pyautogui.position())
    # listMusic.append(pyautogui.position())
    pyautogui.click(x=287, y=438)
    set_times()
    sleep(1)
    pyautogui.click(x = listMusic[count]['x'], y = listMusic[count]['y'] ,clicks = 2 ,interval = 0.25)
    sleep(6)
    pyautogui.click(x=529, y=380)
    keyboard.press_and_release('ctrl + v')  #crt + v
    pyautogui.click(x=1365, y=626) #click sroll down
    set_times()
    pyautogui.click(x=1211, y=256) #submit
    sleep(6)
    pyautogui.click(x=660, y=428) #confirm
    set_times()
    pyautogui.click(x=1363, y=108) #scroll up
    set_times()
    if count == flag:
      # pyautogui.click(x=1342, y=8)
      input("continiu")
      flag += 30
    count += 1

def get_id(filePath):
  driver = khoitao(filePath)
  driver.get('https://www.douyin.com/user/MS4wLjABAAAAX1rLy-8kpfYjUXK8_cXQOr3FV6-GhZvqw_DLkIR0IwlQu7dwdbY084raF8kXyS5M ')
  input("ff")
  save_list_link=open('link_douyin.txt','w')
  sleep(2)

  read1 = driver.find_elements_by_css_selector('.goWork')
  print(len(read1))
  for item in range(0,len(read1)): #len(read1)
      # if (read1[item].get_attribute('href').__contains__('video')):
         rs_str_spl = read1[item].get_attribute('data-id')
         print(rs_str_spl)
         save_list_link.write("rs_str_spl" +"\n")
def auto():
  print("Chọn mode\n")
  print("1. Get like\n")
  print("2.get_link_profile_codition\n")
  print("3.Post\n")
  print("4.Get id\n")
  print("5.Get link profile tiktok\n")
  print("5.get_link_profile\n")
  s = input("Chọn mode:")
  if int(s) == 1:
    ac = input("nhap acount: ")
    get_like(ac)
  if int(s)== 3:
    auto_post()
  if int(s) == 2:
    get_link_profile_codition('n')
  if int(s) == 4:
    get_id('n')
  if int(s) == 5:
    get_link_profile_tiktok('n1')
  if int(s) == 6:
    get_link_profile('n1')
auto()
# get_like_conditon("n")

# get_link_profile_tiktok('n1')
# get_link_profile('f')

#gáixinh #gáixinhtiktok #gái_đẹp #xuhuongtiktok #fyp#gáixinh #gáixinhtiktok















# def on_press(key):
#     global break_program
#     global pasuse_keys
#     print (key)
#     if key == keyboard.Key.end:
#         print ('end pressed')
#         break_program = True
#         return False
#     if key == pasuse_key:
#       pasuse_keys = 1
# with pynput.keyboard.Listener(on_press=on_press) as listener:
  
#     for x in range(10):
#       count += 1 
#       time.sleep(2)
#       if pasuse_keys == 1:
#         input("pase")
#         pasuse_keys = 0
#       print(count)

#     listener.join()



# class AutoClass(threading.Thread):
#   def __init__(self):
#     super(AutoClass, self).__init__()
#   def start(self):
#     pause_click = True
#     self.count += 1
#   def stop(self):
#     pause_click = False

#   def run(self):
#     print("fvfb")
#     while break_program:
#       while pause_click:
#         print("runing")

      
# count = 0

# autoc = AutoClass()
# autoc.run()

# def on_press(key):

#   if key == start_key:
#     autoc.start()

#     # auto()
#   elif key == pasuse_key:
#     autoc.stop()
#   else:
#     break_program = False
#     print("exit")
# with Listener(on_press = on_press) as listener:
#   if key:
#     pass
#   listener.join()  

# on_press()
# def auto():
#   for x in range(1):
#     input("\nnext\n")
#     # print(pyautogui.position())
#   #   listMusic.append(pyautogui.position())
#     pyautogui.click(x=291, y=492)
#     sleep(1)
#     pyautogui.click(x = listMusic[x]['x'], y = listMusic[x]['y'] ,clicks = 2 ,interval = 0.25)
#     sleep(4)
#     pyautogui.click(x=578, y=417)
#     keyboard.press_and_release('ctrl + v')  #crt + v
#     pyautogui.click(x=1362, y=566) #click sroll
#     sleep(1)
#     pyautogui.click(x=1200, y=301) #submit

# auto()
# def auto():
# 	x = 1
# 	for i in range(1,240):
# 		if x == 5:
# 			x = 1
# 		if i == 1:

# 			#nhac
# 			pyautogui.click(x=1086, y=626)
# 			pyautogui.click(x = 1027, y = 590)
# 			sleep(1)
# 			pyautogui.click(x=1160, y=457)
# 			pyautogui.click(x = listMusic[x]['x'], y = listMusic[x]['y'] ,clicks = 2 ,interval = 0.25)
# 			pyautogui.click(x = 311, y = 627 )
# 			pyautogui.click(x = 354, y = 613 )

# 			pyautogui.click(x = 1060, y = 535 ,clicks = 8 ,interval = 0.25)#filter
# 			pyautogui.click(x = 777, y = 433 )#filter

# 			# pyautogui.click(x = 774, y = 500 )

# 			pyautogui.click(x = 317, y = 101 )
# 			pyautogui.click(x = 892, y = 183 )
# 			pyautogui.click(x = 897, y = 656 )
# 			pyautogui.click(x = 437, y = 622 )
# 		elif i == 2:

# 			#nhac
# 			pyautogui.click(x=1095, y=481)
# 			pyautogui.click(x = 990, y = 651)
# 			pyautogui.click(x=1161, y=512)
# 			pyautogui.click(x = listMusic[x]['x'], y = listMusic[x]['y'] ,clicks = 2 ,interval = 0.25)
# 			pyautogui.click(x = 312, y = 481 )
# 			pyautogui.click(x = 354, y = 613 )

# 			pyautogui.click(x = 1060, y = 535 ,clicks = 8 ,interval = 0.25)#filter
# 			pyautogui.click(x = 777, y = 433 )#filter

# 			# pyautogui.click(x = 774, y = 500 )

# 			pyautogui.click(x = 317, y = 101 )
# 			pyautogui.click(x = 892, y = 183 )
# 			pyautogui.click(x = 897, y = 656 )
# 			pyautogui.click(x = 475, y = 479 )
# 		elif i == 3:

# 			#nhac
# 			pyautogui.click(x=1094, y=335)
# 			pyautogui.click(x = 990, y = 502 )
# 			pyautogui.click(x=1161, y=369)
# 			pyautogui.click(x = listMusic[x]['x'], y = listMusic[x]['y'] ,clicks = 2 ,interval = 0.25)
# 			pyautogui.click(x = 312, y = 336 )
# 			pyautogui.click(x = 354, y = 613 )

# 			pyautogui.click(x = 1060, y = 535 ,clicks = 8 ,interval = 0.25)#filter
# 			pyautogui.click(x = 777, y = 433 )#filter

# 			# pyautogui.click(x = 774, y = 500 )

# 			pyautogui.click(x = 317, y = 101 )
# 			pyautogui.click(x = 892, y = 183 )
# 			pyautogui.click(x = 897, y = 656 )
# 			pyautogui.click(x = 403, y = 342 )
# 		else:

# 			pyautogui.click(x=1089, y=205)
# 			pyautogui.click(x = 1009, y = 368 )
# 			pyautogui.click(x=1159, y=235)
# 			pyautogui.click(x = listMusic[x]['x'], y = listMusic[x]['y'] ,clicks = 2 ,interval = 0.25)
# 			pyautogui.click(x = 312, y = 213 )
# 			pyautogui.click(x = 354, y = 613 )
			
# 			pyautogui.click(x = 1060, y = 535 ,clicks = 8 ,interval = 0.25)#filter
# 			pyautogui.click(x = 777, y = 433 )#filter

# 			# pyautogui.click(x = 774, y = 500 )

# 			pyautogui.click(x = 317, y = 101 )
# 			pyautogui.click(x = 892, y = 183 )
# 			pyautogui.click(x = 897, y = 656 )
# 			pyautogui.click(x = 681, y = 152 )
# 		sleep(1)
# 		x +=1
# 		keyboard.press_and_release('up')
