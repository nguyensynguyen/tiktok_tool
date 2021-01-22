import asyncio
from tiktokpy import TikTokPy
from tkinter import *

root = Tk()
root.title("test")
root.geometry("900x650")

box = Text(root,width = 80,height = 25,fg = "#000000")
box.pack(pady=20)

async def main():
    async with TikTokPy() as bot:
        # Do you want to get trending videos? You can!
        # await bot.login_session()
        trending_items = await bot.trending(amount=10)
        list_user = trending_items
        # print(list_user[0].author.username + ":" + list_user[0].id)
        for item in range(0,len(list_user)):
            print("https://www.tiktok.com/@" + list_user[item].author.username + "/video/" + list_user[item].id + "?lang=vi-VN")
            print("***************************************")
            box.insert(END,"https://www.tiktok.com/@" + list_user[item].author.username + "/video/" + list_user[item].id + "?lang=vi-VN\n\n")
# B = Button(root, text ="Get Data",bg='#008000',command = asyncio.run(main())).pack(pady = 0)
asyncio.run(main())
root.mainloop()
