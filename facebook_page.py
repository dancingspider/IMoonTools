# # Facebook Login
# from typing import List
#
# from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
#
# class FBPage:
#     def __init__(self, fb_driver: WebDriver):
#         self.fb_page_home = "https://www.facebook.com/pages/?category=your_pages&ref=bookmarks"
#         self.fb_driver = fb_driver
#         self.pages_parent_div = WebElement
#         self.pages_child_divs = List[WebElement]
#         self.page_url_a_hrefs = []
#         self.block_words = "fuck,caonima,card,haox"
#
#     # 打开FB站点
#     def open_fb_page_home(self):
#         self.fb_driver.get(self.fb_page_home)
#
#     def check_fb_page_exist(self):
#         self.pages_parent_div = self.fb_driver.find_element_by_xpath("/html/body/div[1]/div/div[1]\
#                                         /div/div[3]/div/div/div[1]/div[1]\
#                                         /div[1]/div/div[2]/div[1]/div[2]")
#
#         self.pages_child_divs = self.pages_parent_div.find_elements_by_xpath("div")
#         if len(self.pages_child_divs) == 3:
#             return True
#         else:
#             return False
#
#     # 操作已存在的粉丝页--发布粉丝页---添加屏蔽词
#     def operate_page(self):
#         page_url_as = self.pages_child_divs[1].find_elements_by_tag_name("a")
#         for page_url_a in page_url_as:
#             self.page_url_a_hrefs.append(page_url_a.get_attribute("href"))
#
#         for page_url_a_href in self.page_url_a_hrefs:
#             if self.set_page_publish(page_url_a_href):
#                 self.add_page_block_words(page_url_a_href)
#                 return True
#         return False
#
#     def add_page_block_words(self, page_url):
#         self.fb_driver.get(page_url + "settings/?tab=settings&ref=page_edit&section=page_moderation&view")
#
#         wait = WebDriverWait(self.fb_driver, 10)
#         wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
#         self.fb_driver.switch_to.frame(self.fb_driver.find_element_by_tag_name(
#             "iframe"))
#
#         block_words_textbox_parent_div = self.fb_driver.find_element_by_xpath("//*[@id='u_0_0']/div/div/div/div[2]/div")
#         block_words_textbox = block_words_textbox_parent_div.find_element_by_css_selector("input[type='text']")
#         block_words_textbox.send_keys(self.block_words)
#         block_words_add_button = block_words_textbox_parent_div.find_element_by_xpath("div[2]/div[1]/div[2]/button")
#         block_words_add_button.click()
#         block_words_save_button = block_words_textbox_parent_div.find_element_by_xpath("div[2]/div[5]/button[1]")
#         block_words_save_button.click()
#         return True
#
#     # 查看粉丝页是否published
#     def set_page_publish(self, page_url):
#         self.fb_driver.get(page_url + "settings/?tab=settings&ref=page_edit&section=page_visibility")
#
#         wait = WebDriverWait(self.fb_driver, 10)
#         wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
#         self.fb_driver.switch_to.frame(self.fb_driver.find_element_by_tag_name(
#             "iframe"))
#
#         page_publish_stats_parent_div = self.fb_driver.find_element_by_xpath("//*[@id='u_0_t']/div[2]")
#         publish_stats_radios = page_publish_stats_parent_div.find_elements_by_css_selector("input[type='radio']")
#         time.sleep(2)
#         # if publish_stats_radios[0].is_selected():
#         #     return True
#         # else:
#         # publish_save_button = self.fb_driver.find_elements_by_css_selector("input[type='submit']")
#         # return self.publish_page(publish_stats_radios, publish_save_button)
#         try:
#
#             if not publish_stats_radios[0].is_selected():
#                 # publish_stats_radios[0].click()
#                 action = ActionChains(self.fb_driver)
#                 action.move_to_element(publish_stats_radios[0])
#                 action.click()
#                 action.perform()
#
#                 publish_save_button = self.fb_driver.find_element_by_css_selector("input[type='submit']")
#                 publish_save_button.click()
#
#             return True
#
#         except():
#             return False
