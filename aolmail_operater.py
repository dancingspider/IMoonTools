from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AolMailOperater:
    def __init__(self, adsp_driver: WebDriver):
        self.aolmail_home = "https://login.aol.com/"
        self.driver = adsp_driver

        # 打开gmail站点

    def open_aol_mail_site(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(self.aolmail_home)

    def login_aol_mail(self, aol_mail_username):
        aol_mail_username_textbox = self.driver.find_element_by_id("login-username")
        aol_mail_username_textbox.send_keys(aol_mail_username)
        # next_button1 = self.driver.find_element_by_id("login-signin")
        # next_button1.click()
        #
        # wait = WebDriverWait(self.fb_driver, 10)
        # wait.until(EC.presence_of_element_located((By.ID, "login")))

    def fill_aol_mail_password(self, aol_mail_password):
        aol_mail_password_textbox = self.driver.find_element_by_id("login-passwd")
        aol_mail_password_textbox.send_keys(aol_mail_password)
        # next_button1.click()
        #
        # wait = WebDriverWait(self.fb_driver, 10)
        # wait.until(EC.url_contains("https://www.aol.com/?guce_referrer="))
        #
        # self.driver.get("https://mail.aol.com/webmail-std/en-us/suite")
        # try:
        #
        #     get_started_button = self.driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/div")
        #     get_started_button.click()
        # except ZeroDivisionError as e:
        #     print('except:', e)
        # finally:
        #     print('finally...')
