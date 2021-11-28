import json
import requests
import os
from time import sleep
# import urllib.parse
# import urllib.request
# import urllib

# url = "https://tiktok-trending-data.p.rapidapi.com/m"

# headers = {
#     'x-rapidapi-key': "666cbb3d98msh46425591c14bd86p1513efjsne4e2095e1d9d",
#     'x-rapidapi-host': "tiktok-trending-data.p.rapidapi.com"
#     }

# response = requests.request("GET", url, headers=headers)

# print(response.text)

def download(StrCount):
    folder = "v3"
    # folder_path = "D:/video/" + folder
    # disr = os.makedirs(folder_path)
    list_link=open('link_douyin.txt','r',encoding="utf-8")
    read = list_link.readlines()
    base_url = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids="

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
     # This seems to be very important
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',
    }


    urls = "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0d00fg10000c3pv9fjc77u2kln47vag&ratio=720p&line=0"

    for i in range(1,len(read)):
        
        stx =  read[i].split("/")[4]
        id_video = stx.split("?")[0]
        url = base_url + id_video
        print(id_video)
        #goi api
        videoBin = requests.get(url = urls,headers = headers)
        print(videoBin.status_code)
        data = videoBin.text 
        # print(data)
        datas = json.dumps(data)
        print(datas)
        base_link = datas['item_list'][0]['video']['play_addr']['url_list'][0]
        link_result = base_link.replace("playwm", "play")
        filename =StrCount+" ({}).mp4".format(i)
        videoBin = requests.get(urls,headers)
        with open('D:\\video\\{}\\'.format(folder) + filename, 'ab+') as f:
            filename =  'c.mp4'
            f.write(videoBin.content)
    print("success")

def download1(StrCount):
    folder = "v3"
    # folder_path = "D:/video/" + folder
    # disr = os.makedirs(folder_path)
    list_link=open('link_douyin_m.txt','r',encoding="utf-8")
    read = list_link.readlines()

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
     # This seems to be very important
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',
    }

    for i in range(0,len(read)):
        print(read[i])
        filename =StrCount+" ({}).mp4".format(i)
        videoBin = requests.get(read[i],headers)
        with open('D:\\video\\{}\\'.format(folder) + filename, 'ab+') as f:
            filename =  'c.mp4'
            f.write(videoBin.content)
    print("success")

download1("v")
# import requests

# url = "https://tiktok-trending-data.p.rapidapi.com/t"

# headers = {
#     'x-rapidapi-host': "tiktok-trending-data.p.rapidapi.com",
#     'x-rapidapi-key': "7059e5e837mshb45caa01e5c79fap128ca0jsn5425bbce94a6"
#     }

# response = requests.request("GET", url, headers=headers)

# print(response.text)







# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
# }
# urls = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=6976564869134961920"
# videoBin = requests.get(url = urls)
# data = videoBin.text
# print(data)
# datas = json.loads(data)
# base_link = datas['item_list'][0]['video']['play_addr']['url_list'][0]
# link_result = base_link.replace("playwm", "play")
# filename =  "hghg.mp4"
# videoBin = requests.get(link_result, headers=headers)
# with open('D:\\videos\\' + filename, 'ab+') as f:
#     filename =  'c.mp4'
#     f.write(videoBin.content)
# print("success")


# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
# }
# urls = "https://video-sin6-3.xx.fbcdn.net/v/t42.9040-2/10000000_2631797920220345_2643565148215705600_n.mp4?_nc_cat=104&vs=43d19795a9d01c3d&_nc_vs=HBksFQAYJEdJQ1dtQUM1eENjMG0xa0pBQUFBQUFCLTFLOGtibEFqQUFBRhUAAsgBABUAGCRHSUNXbUFBSFU1ZVlGNkVDQUFBQUFBRFZwYUJVYnY0R0FBQUYVAgLIAQBLBogScHJvZ3Jlc3NpdmVfcmVjaXBlATEgbWVhc3VyZV9vcmlnaW5hbF9yZXNvbHV0aW9uX3NzaW0AKGNvbXB1dGVfc3NpbV9vbmx5X2F0X29yaWdpbmFsX3Jlc29sdXRpb24AEWRpc2FibGVfcG9zdF9wdnFzAA1zdWJzYW1wbGVfZnBzABB2bWFmX2VuYWJsZV9uc3ViABUAJQAcAAAm%2BJfu1vvEgAIVAigCQzMYC3Z0c19wcmV2aWV3HBdAvzMSLQ5WBBgYZGFzaF92NF9ocTJfZnJhZ18yX3ZpZGVvEgAYGHZpZGVvcy52dHMuY2FsbGJhY2sucHJvZDgSVklERU9fVklFV19SRVFVRVNUGwSIFW9lbV90YXJnZXRfZW5jb2RlX3RhZwZvZXBfaGQTb2VtX3JlcXVlc3RfdGltZV9tcw0xNjI0NjcyOTY5OTY3DG9lbV9jZmdfcnVsZQd1bm11dGVkE29lbV9yb2lfcmVhY2hfY291bnQCMTMlAhwAJcQBGwaIAXMENzA2OAJjZAoyMDE5LTEyLTExA3JjYgEwA2FwcAVWaWRlbwJjdApHUk9VUF9QT1NUAnRzD29lcF9wcm9ncmVzc2l2ZQA%3D&ccb=1-3&_nc_sid=41a7d5&efg=eyJ2ZW5jb2RlX3RhZyI6Im9lcF9oZCJ9&_nc_ohc=7X6t7nDGkX0AX9PNgZj&_nc_ht=video-sin6-3.xx&oh=e6396e691eca8e82b69e81edcc909dc1&oe=60D810D6&_nc_rid=aa50c7d8a1be4f7&_nc_vts_prog=1&_nc_vts_internal=1"
# filename =  "hghdg.mp4"
# print("downloading.... ")

# videoBin = requests.get(urls, headers=headers)
# with open('D:\\videos\\' + filename, 'ab+') as f:
#     filename =  'c.mp4'
#     f.write(videoBin.content)
# print("success")