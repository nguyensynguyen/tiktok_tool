import json

import requests
from tkinter import *

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36"}
linhk_video_trend = "https://www.iesdouyin.com/share/billboard/"
link_json_video_trend = 'https://www.iesdouyin.com/web/api/v2/hotsearch/billboard/aweme/'

root = Tk()
root.title("test")
root.geometry("900x650")
box1 = Text(root, width=80, height=2, fg="#000000")
box1.pack(pady=20)

box = Text(root, width=80, height=25, fg="#000000")
box.pack(pady=20)


def hot_trend():
    box.delete(1.0, END)
    get_data_box = box1.get(1.0, END)
    get_word_box = get_data_box[0:len(get_data_box) - 1]
    hot_word = [
        '赵丽颖换造型师',
        "殷世航评论",
        '观众席全是肖战灯牌',
        '殷世航 矮love后面的你们来说'

    ]
    hot_reading = 'https://aweme-hl.snssdk.com/aweme/v1/hot/search/video/list/?hotword={}'.format(get_word_box)
    hot_json = requests.get(hot_reading, headers=headers).json()

    for item in range(0, len(hot_json['aweme_list'])):
        print(hot_json['aweme_list'][item]['share_url'])

        box.insert(END, hot_json['aweme_list'][item]['share_url'] + "\n\n")


def get_list_video_trend():
    list_video = requests.get(link_json_video_trend, headers=headers).json()
    for item in range(0, len(list_video)):
        print(item)
        print(list_video['aweme_list'][item]['aweme_info']['share_url'])


def hot_word_search():
    box.delete(1.0, END)
    url = 'https://aweme-hl.snssdk.com/aweme/v1/hot/search/list/'
    list_word = requests.get(url, headers=headers).json()
    for index in range(0, len(list_word['data']['word_list'])):
        box.insert(END, list_word['data']['word_list'][index]['word'] + "\n")


# hot_word_search()
B = Button(root, text="Get Data", bg='#008000', command=hot_trend).pack(pady=0)
B1 = Button(root, text="Get word Search Hot", bg='#008000', command=hot_word_search).pack(pady=2)
# get_list_video_trend()
# hot_trend()
# print("=============================================")
# hot_search = requests.get(
#     'https://aweme-hl.snssdk.com/aweme/v1/hot/search/list/?detail_list=1&mac_address=08:00:27:29:D2:F5&os_api=23&device_type=MI%205s&device_platform=android&ssmix=a&iid=92152480453&manifest_version_code=860&dpi=320&uuid=008796750074613&version_code=860&app_name=aweme&version_name=8.6.0&ts=1577932778&openudid=c055533a0591b2dc&device_id=69918538596&resolution=810*1440&os_version=6.0.1&language=zh&device_brand=Xiaomi&app_type=normal&ac=wifi&update_version_code=8602&aid=1128&channel=tengxun_new&_rticket=1577932779592',
#     headers=headers).json()
# for index in range(0, len(hot_search)):
#     print(hot_search['data']['word_list'][index]['word'])
root.mainloop()
