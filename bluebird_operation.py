from selenium.webdriver.chrome.webdriver import WebDriver

from base_ssn_info import SsnInfo


class BlueBird:
    def __init__(self, adsp_driver: WebDriver):
        self.bluebird_home = "https://secure.bluebird.com/signup1"
        self.driver = adsp_driver

    def open_bluebird_site(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(self.bluebird_home)

    def crate_bluebird_account(self, ssnInfo: SsnInfo):
        # 第一页
        next_button = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div[2]/button")
        next_button.click()
        # 第二页
        account_select_card_button = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/button[2]")
        account_select_card_button.click()

        next_button = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div[2]/button")
        next_button.click()
        # 第三页
        username_textbox = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[1]/input")
        username_textbox.clear()
        username_textbox.send_keys(ssnInfo.user_name)

        email_textbox = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/input")
        email_textbox.clear()
        email_textbox.send_keys(ssnInfo.email)

        email2_textbox = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[3]/input")
        email2_textbox.clear()
        email2_textbox.send_keys(ssnInfo.email)

        password_textbox = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[4]/input")
        password_textbox.clear()
        password_textbox.send_keys(ssnInfo.password)

        password2_textbox = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[5]/input")
        password2_textbox.clear()
        password2_textbox.send_keys(ssnInfo.password)

        next_button = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[6]/div/div/div[2]/button")
        next_button.click()
        # 第四页
        firstname_textbox = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[1]/input")
        firstname_textbox.clear()
        firstname_textbox.send_keys(ssnInfo.first_name)

        lastname_textbox = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/input")
        lastname_textbox.clear()
        lastname_textbox.send_keys(ssnInfo.last_name)

        birthday_textbox = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/input")
        birthday_textbox.clear()
        birthday_textbox.send_keys(ssnInfo.birth_month + ssnInfo.birth_day + ssnInfo.birth_year)

        next_button = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[4]/div/div/div[2]/button")
        next_button.click()
        #第五页
        phone_textbox = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[1]/input")
        phone_textbox.send_keys(ssnInfo.home_phone)

        next_button = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/div/div/div[2]/button")
        next_button.click()

        # 第6页
        zip_textbox = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[1]/input")
        zip_textbox.clear()
        zip_textbox.send_keys(ssnInfo.zip)

        next_button = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/div/div/div[2]/button")
        next_button.click()

        # #第七页
        # adress_textbox = self.driver.find_element_by_xpath(
        #     "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[1]/div/div/div[1]/div[2]/div/input")
        # adress_textbox.send_keys(ssnInfo.address)
        # adress_textbox.send_keys()
        #
        # next_button = self.driver.find_element_by_xpath(
        #     "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/div/div/div[2]/button")
        # next_button.click()