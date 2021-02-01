# import tkinter
# from facebook_login import FB
# from facebook_page import FBPage
#
# fb = FB()
#
#
# # 打开粉丝页
# def open_fb_page_home_event():
#     fb_page = FBPage(fb.fb_driver)
#     fb_page.open_fb_page_home()
#
#
# def check_fb_page_exist_event():
#     fb_page = FBPage(fb.fb_driver)
#     page_exist = fb_page.check_fb_page_exist()
#     print(page_exist)
#     if page_exist:
#         fb_page.operate_page()
#
#
# fo_window = tkinter.Tk()
# fo_window.title = "Facebook 操作"
# ww = 350
# wh = 350
# wx = (fo_window.winfo_screenwidth() - ww) / 2
# wy = (fo_window.winfo_screenheight() - wh) / 2
# fo_window.geometry("%dx%d+%d+%d" % (ww, wh, wx, wy))
#
# # 打开Facebook网站按钮
# open_fb_site = tkinter.Button(fo_window, text="打开Facebook", command=fb.open_fb_site)
# open_fb_site.pack()
#
# # 打开Facebook page网站按钮
# open_fb_page = tkinter.Button(fo_window, text="打开粉丝页", command=open_fb_page_home_event)
# open_fb_page.pack()
#
# # 查询粉丝页是否存在
# check_fb_page = tkinter.Button(fo_window, text="检查粉丝页", command=check_fb_page_exist_event)
# check_fb_page.pack()
# fo_window.mainloop()
