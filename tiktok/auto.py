import pyautogui
from time import sleep
import keyboard
import random
# keyboard.press_and_release('WIN + v')

listMusic = [
  {"x":221, "y":139},
  {"x":217, "y":158},
  {"x":228, "y":179},
  {"x":219, "y":201},
  {"x":828, "y":221},
  {"x":828, "y":241},
  {"x":834, "y":261},

  {"x":933, "y":283},
  {"x":931, "y":291},
  {"x":930, "y":309},
  {"x":927, "y":333},
  {"x":926, "y":352},
  {"x":923, "y":374},
  {"x":920, "y":391},
  {"x":920, "y":414},
  {"x":914, "y":436},
  {"x":915, "y":457},
  {"x":918, "y":476},
  {"x":920, "y":497},
  {"x":914, "y":518}
]


count = 1
def auto1():
	x = 1
	for i in range(1,4):
		if x == 8:
			x = 1
		if i == 1:
			pyautogui.click(x = 933, y = 628 )
			sleep(1)
			pyautogui.click(x = 1016, y = 654 )
			sleep(1)
			pyautogui.click(x = 956, y = 144 ,clicks = 2 ,interval = 0.25)
			sleep(1)
			pyautogui.click(x = 389, y = 623 )
			sleep(1)
			pyautogui.click(x = 933, y = 628 )
			sleep(1)
			pyautogui.click(x = 897, y = 560 )

			#nhac
			pyautogui.click(x=1086, y=626)
			pyautogui.click(x = 1027, y = 590)
			sleep(1)
			pyautogui.click(x=1160, y=457)
			pyautogui.click(x = listMusic[x]['x'], y = listMusic[x]['y'] ,clicks = 2 ,interval = 0.25)
			pyautogui.click(x = 311, y = 627 )
			pyautogui.click(x = 354, y = 613 )

			pyautogui.click(x = 1060, y = 535 ,clicks = 8 ,interval = 0.25)#filter
			pyautogui.click(x = 777, y = 433 )#filter

			# pyautogui.click(x = 774, y = 500 )

			pyautogui.click(x = 317, y = 101 )
			pyautogui.click(x = 892, y = 183 )
			pyautogui.click(x = 897, y = 656 )
			pyautogui.click(x = 437, y = 622 )
		elif i == 2:
			pyautogui.click(x = 920, y = 483 )
			pyautogui.click(x = 1010, y = 512 )
			pyautogui.click(x = 956, y = 144 ,clicks = 2 ,interval = 0.25)
			pyautogui.click(x = 475, y = 479 )
			pyautogui.click(x = 920, y = 483 )
			pyautogui.click(x = 900, y = 644 )
			#nhac
			pyautogui.click(x=1095, y=481)
			pyautogui.click(x = 990, y = 651)
			pyautogui.click(x=1161, y=512)
			pyautogui.click(x = listMusic[x]['x'], y = listMusic[x]['y'] ,clicks = 2 ,interval = 0.25)
			pyautogui.click(x = 312, y = 481 )
			pyautogui.click(x = 354, y = 613 )
			pyautogui.click(x = 1060, y = 535 ,clicks = 8 ,interval = 0.25)#filter
			pyautogui.click(x = 777, y = 433 )#filter

			# pyautogui.click(x = 774, y = 500 )

			pyautogui.click(x = 317, y = 101 )
			pyautogui.click(x = 892, y = 183 )
			pyautogui.click(x = 897, y = 656 )
			pyautogui.click(x = 475, y = 479 )
		elif i == 3:
			pyautogui.click(x = 943, y = 336 )
			pyautogui.click(x = 1012, y = 366 )
			pyautogui.click(x = 956, y = 144 ,clicks = 2 ,interval = 0.25)
			pyautogui.click(x = 403, y = 342 )
			pyautogui.click(x = 943, y = 336 )
			pyautogui.click(x = 917, y = 494 )
			#nhac
			pyautogui.click(x=1094, y=335)
			pyautogui.click(x = 990, y = 502 )
			pyautogui.click(x=1161, y=369)
			pyautogui.click(x = listMusic[x]['x'], y = listMusic[x]['y'] ,clicks = 2 ,interval = 0.25)
			pyautogui.click(x = 312, y = 336 )
			pyautogui.click(x = 354, y = 613 )
			pyautogui.click(x = 1060, y = 535 ,clicks = 8 ,interval = 0.25)#filter
			pyautogui.click(x = 777, y = 433 )#filter

			# pyautogui.click(x = 774, y = 500 )

			pyautogui.click(x = 317, y = 101 )
			pyautogui.click(x = 892, y = 183 )
			pyautogui.click(x = 897, y = 656 )
			pyautogui.click(x = 403, y = 342 )
		else:
			pyautogui.click(x = 833, y = 200 )
			pyautogui.click(x = 1011, y = 237 )
			pyautogui.click(x = 956, y = 144 ,clicks = 2 ,interval = 0.25)
			pyautogui.click(x = 833, y = 200 )
			pyautogui.click(x = 877, y = 365 )

			pyautogui.click(x=1089, y=205)
			pyautogui.click(x = 1009, y = 368 )
			pyautogui.click(x=1159, y=235)
			pyautogui.click(x = listMusic[x]['x'], y = listMusic[x]['y'] ,clicks = 2 ,interval = 0.25)
			pyautogui.click(x = 312, y = 213 )
			pyautogui.click(x = 354, y = 613 )
			pyautogui.click(x = 1060, y = 535 ,clicks = 8 ,interval = 0.25)#filter
			pyautogui.click(x = 777, y = 433 )#filter

			# pyautogui.click(x = 774, y = 500 )

			pyautogui.click(x = 317, y = 101 )
			pyautogui.click(x = 892, y = 183 )
			pyautogui.click(x = 897, y = 656 )
			pyautogui.click(x = 681, y = 152 )
		sleep(1)
		x +=1
		keyboard.press_and_release('up')


def auto2():
	sl = input("nhap sl:")
	x = 0
	for i in range(0,int(sl)):
		if x == 6:
			x = 1
		if i == 1:

			#nhac
			pyautogui.click(x=1086, y=626)
			pyautogui.click(x = 1027, y = 590)
			sleep(1)
			pyautogui.click(x=1160, y=457)
			pyautogui.click(x = listMusic[x]['x'], y = listMusic[x]['y'] ,clicks = 2 ,interval = 0.25)
			pyautogui.click(x = 311, y = 627 )
			pyautogui.click(x = 354, y = 613 )

			pyautogui.click(x = 1060, y = 535 ,clicks = 8 ,interval = 0.25)#filter
			pyautogui.click(x = 777, y = 433 )#filter

			# pyautogui.click(x = 774, y = 500 )

			pyautogui.click(x = 317, y = 101 )
			pyautogui.click(x = 892, y = 183 )
			pyautogui.click(x = 897, y = 656 )
			pyautogui.click(x = 437, y = 622 )
		elif i == 2:

			#nhac
			pyautogui.click(x=1095, y=481)
			pyautogui.click(x = 990, y = 651)
			pyautogui.click(x=1161, y=512)
			pyautogui.click(x = listMusic[x]['x'], y = listMusic[x]['y'] ,clicks = 2 ,interval = 0.25)
			pyautogui.click(x = 312, y = 481 )
			pyautogui.click(x = 354, y = 613 )

			pyautogui.click(x = 1060, y = 535 ,clicks = 8 ,interval = 0.25)#filter
			pyautogui.click(x = 777, y = 433 )#filter

			# pyautogui.click(x = 774, y = 500 )

			pyautogui.click(x = 317, y = 101 )
			pyautogui.click(x = 892, y = 183 )
			pyautogui.click(x = 897, y = 656 )
			pyautogui.click(x = 475, y = 479 )
		elif i == 3:

			#nhac
			pyautogui.click(x=1094, y=335)
			pyautogui.click(x = 990, y = 502 )
			pyautogui.click(x=1161, y=369)
			pyautogui.click(x = listMusic[x]['x'], y = listMusic[x]['y'] ,clicks = 2 ,interval = 0.25)
			pyautogui.click(x = 312, y = 336 )
			pyautogui.click(x = 354, y = 613 )

			pyautogui.click(x = 1060, y = 535 ,clicks = 8 ,interval = 0.25)#filter
			pyautogui.click(x = 777, y = 433 )#filter

			# pyautogui.click(x = 774, y = 500 )

			pyautogui.click(x = 317, y = 101 )
			pyautogui.click(x = 892, y = 183 )
			pyautogui.click(x = 897, y = 656 )
			pyautogui.click(x = 403, y = 342 )
		else:

			pyautogui.click(x=1089, y=205)
			pyautogui.click(x = 1009, y = 368 )
			pyautogui.click(x=1159, y=235)
			pyautogui.click(x = listMusic[x]['x'], y = listMusic[x]['y'] ,clicks = 2 ,interval = 0.25)
			pyautogui.click(x = 312, y = 213 )
			pyautogui.click(x = 354, y = 613 )
			
			pyautogui.click(x = 1060, y = 535 ,clicks = 8 ,interval = 0.25)#filter
			pyautogui.click(x = 777, y = 433 )#filter

			# pyautogui.click(x = 774, y = 500 )

			pyautogui.click(x = 317, y = 101 )
			pyautogui.click(x = 892, y = 183 )
			pyautogui.click(x = 897, y = 656 )
			pyautogui.click(x = 681, y = 152 )
		sleep(1)
		x +=1
		keyboard.press_and_release('up')


def auto3():
  sl = input("nhap sl:")
  x = 0
  for i in range(0,int(sl)):
    if x == 3:
      x = 0
    if i == 0:
      #nhac
      pyautogui.click(x=1080, y=626)
      pyautogui.click(x = 1166, y = 452)
      sleep(1)
      pyautogui.click(x = listMusic[x]['x'], y = listMusic[x]['y'] ,clicks = 2 ,interval = 0.25)
      pyautogui.click(x = 992, y = 614 )

      # pyautogui.click(x = 1060, y = 535 ,clicks = 8 ,interval = 0.25)#filter
      # pyautogui.click(x = 777, y = 433 )#filter

      pyautogui.click(x = 275, y = 624 )
      pyautogui.click(x = 893, y = 185 )
      pyautogui.click(x = 887, y = 657 )

      pyautogui.click(x = 725, y = 591 )

      # pyautogui.click(x = 317, y = 101 )
      # pyautogui.click(x = 892, y = 183 )
      # pyautogui.click(x = 897, y = 656 )
      # pyautogui.click(x = 437, y = 622 )

    elif i == 1:
      #nhac
      pyautogui.click(x=1067, y=479)
      pyautogui.click(x = 1161, y = 509)
      sleep(1)
      pyautogui.click(x = listMusic[x]['x'], y = listMusic[x]['y'] ,clicks = 2 ,interval = 0.25)
      pyautogui.click(x = 991, y = 673 )

      # pyautogui.click(x = 1060, y = 535 ,clicks = 8 ,interval = 0.25)#filter
      # pyautogui.click(x = 777, y = 433 )#filter
      pyautogui.click(x = 275, y = 482 )
      pyautogui.click(x = 893, y = 185 )
      pyautogui.click(x = 887, y = 657 )

      pyautogui.click(x = 696, y = 446 )

    elif i == 2:
      #nhac
      pyautogui.click(x=1074, y=336)
      pyautogui.click(x = 1162, y = 365)
      sleep(1)
      pyautogui.click(x = listMusic[x]['x'], y = listMusic[x]['y'] ,clicks = 2 ,interval = 0.25)
      pyautogui.click(x = 992, y = 533 )

      # pyautogui.click(x = 1060, y = 535 ,clicks = 8 ,interval = 0.25)#filter
      # pyautogui.click(x = 777, y = 433 )#filter
      pyautogui.click(x = 276, y = 336 )
      pyautogui.click(x = 893, y = 185 )
      pyautogui.click(x = 887, y = 657 )

      pyautogui.click(x = 720, y = 299 )
    else:
      #nhac
      pyautogui.click(x=1045, y=200)
      pyautogui.click(x = 1163, y = 229)
      sleep(1)
      pyautogui.click(x = listMusic[x]['x'], y = listMusic[x]['y'] ,clicks = 2 ,interval = 0.25)
      pyautogui.click(x = 992, y = 396 )

      # pyautogui.click(x = 1060, y = 535 ,clicks = 8 ,interval = 0.25)#filter
      # pyautogui.click(x = 777, y = 433 )#filter
      pyautogui.click(x = 275, y = 202 )
      pyautogui.click(x = 893, y = 185 )
      pyautogui.click(x = 887, y = 657 )

      pyautogui.click(x = 707, y = 168 )
    sleep(1)
    x +=1
    keyboard.press_and_release('up')

# def deleteItem():
# 	sl = input("nhap so luong :")
# 	for i in range(0,int(sl)):
# 		pyautogui.click(x = 1321, y = 169 )
# 		sleep(1)
# 		pyautogui.click(x = 1181, y = 273 )
# 		sleep(1)
# 		pyautogui.click(x = 688, y = 455 )
# 		sleep(2)

# print("1.auto")
# print("2.delete")
# select = input("chọn mode : ")
# if select == '1':
# 	auto2()
# if select == '2':
# 	deleteItem()
# auto1()
# auto2()
auto3()

# for x in range(15):
#   input("ne")
#   print(pyautogui.position())
# sleep(2)