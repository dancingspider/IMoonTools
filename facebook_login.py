# import json
#
# from selenium import webdriver
#
#
# # Facebook Login
# class FB:
#     def __init__(self):
#         self.options = webdriver.ChromeOptions()
#         self.proxy = "127.0.0.1:5000"
#         self.options.add_argument('--proxy-server=socks5://' + self.proxy)
#         # self.options.add_argument("--headless")
#         # self.options.add_argument("--disable-gpu")
#         self.fb_driver = None  # webdriver.Chrome(options=self.options)
#         self.fb_url = "https://www.facebook.com"
#
#         # f1 = open("cookie.txt")
#         # self.cookie = json.loads(f1.read())
#
#     # 打开FB站点
#     def open_fb_site(self):
#         self.fb_driver = webdriver.Chrome(options=self.options)
#         self.fb_driver.get(self.fb_url)
#         # for item in self.cookie:
#         #     item.pop("sameSite")
#         #     self.fb_driver.add_cookie(item)
#         # self.fb_driver.refresh()
