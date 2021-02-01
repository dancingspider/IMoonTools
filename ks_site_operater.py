import json
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_ssn_info import SsnInfo


class KSGov:
    def __init__(self, adsp_driver: WebDriver):
        self.ks_home = "https://www.getkansasbenefits.gov/BenefitsStartMenu.aspx"
        self.ks_signUpHome = "https://www.getkansasbenefits.gov/Account/Register.aspx"
        self.ks_lginHome = "https://www.getkansasbenefits.gov/Account/Login.aspx"
        self.browser_clear_url = "chrome://settings/clearBrowserData"
        self.driver = adsp_driver

    # 打开KS站点
    def open_ks_site(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(self.ks_signUpHome)

    def clear_browser_info(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

        # navigate to the settings page
        self.driver.get('chrome://settings/clearBrowserData')

        # wait for the button to appear
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body")))

        time.sleep(3)
        clearButton = self.driver.execute_script(
            "return document.querySelector('settings-ui').shadowRoot.querySelector('settings-main').shadowRoot.querySelector('settings-basic-page').shadowRoot.querySelector('settings-section > settings-privacy-page').shadowRoot.querySelector('settings-clear-browsing-data-dialog').shadowRoot.querySelector('#clearBrowsingDataDialog').querySelector('#clearBrowsingDataConfirm')")
        # click on the clear button now
        clearButton.click()
        # chrome_clear_body = self.driver.find_element_by_xpath('/html/body/settings-ui//div[2]/settings-main//settings-basic-page//div[1]/settings-section[4]/settings-privacy-page//settings-clear-browsing-data-dialog//cr-dialog[1]/div[4]/cr-button[2]')
        # chrome_clear_body.send_keys(Keys.ENTER)
        # chrome_clear_body.click()

        # get_clear_browsing_button = self.driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')
        #
        # # click the button to clear the cache
        # get_clear_browsing_button(self.driver).click()
        #
        # # wait for the button to be gone before returning
        # wait.until_not(get_clear_browsing_button)

    # def create_ksgov_account(self):
    #     crate_button = self.driver.find_element_by_id("btnCreate")
    #     crate_button.click()
    #
    # def check_ksgov_stats(self):
    #     if self.driver.current_url == "https://www.getkansasbenefits.gov/NotAvailable.aspx":
    #         return False
    #     else:
    #         return True

    def fill_create_ksgov_account(self, ssnInfo: SsnInfo):
        username_textbox = self.driver.find_element_by_id("UserName")
        username_textbox.send_keys(ssnInfo.user_name)

        password_textbox = self.driver.find_element_by_id("Password")
        password_textbox.send_keys(ssnInfo.password)

        confirmPassword_textbox = self.driver.find_element_by_id("ConfirmPassword")
        confirmPassword_textbox.send_keys(ssnInfo.password)

        ssn_textbox = self.driver.find_element_by_id("SSN")
        ssn_textbox.send_keys(ssnInfo.ssn)

        confirmSSN_textbox = self.driver.find_element_by_id("ConfirmSSN")
        confirmSSN_textbox.send_keys(ssnInfo.ssn)

        firstname_textbox = self.driver.find_element_by_id("FirstName")
        firstname_textbox.send_keys(ssnInfo.first_name)

        lastname_textbox = self.driver.find_element_by_id("LastName")
        lastname_textbox.send_keys(ssnInfo.last_name)

        birthday_textbox = self.driver.find_element_by_id("txtDOB")
        birthday_textbox.send_keys(ssnInfo.birth_month + "/" + ssnInfo.birth_day + "/" + ssnInfo.birth_year)

        securityword_textbox = self.driver.find_element_by_id("txtMothersMaiden")
        securityword_textbox.send_keys(ssnInfo.security_code)

        phone_textbox = self.driver.find_element_by_id("Phone")
        phone_textbox.send_keys(ssnInfo.home_phone)

        email_textbox = self.driver.find_element_by_id("Email")
        email_textbox.send_keys(ssnInfo.email)

        pin_textbox = self.driver.find_element_by_id("PIN")
        pin_textbox.send_keys(ssnInfo.pin_code)

        pin2_textbox = self.driver.find_element_by_id("ConfirmPIN")
        pin2_textbox.send_keys(ssnInfo.pin_code)

        # 打开KS站点

    def login_ks_site(self, ssnInfo: SsnInfo):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(self.ks_lginHome)

        username_textbox = self.driver.find_element_by_id("UserName")
        username_textbox.clear()
        username_textbox.send_keys(ssnInfo.user_name)

        password_textbox = self.driver.find_element_by_id("Password")
        password_textbox.clear()
        password_textbox.send_keys(ssnInfo.password)

        pin_textbox = self.driver.find_element_by_id("PIN")
        pin_textbox.clear()
        pin_textbox.send_keys(ssnInfo.pin_code)

    def fill1_ks_all_info(self, ssnInfo: SsnInfo, isContinue):
        waitload = WebDriverWait(self.driver, 10)
        waitload.until(EC.presence_of_element_located((By.ID, "BodyContent_MainContent_btnInitial")))

        if isContinue:
            fill_ks_all_info_textbox = self.driver.find_element_by_id("BodyContent_MainContent_btnInitial")
            fill_ks_all_info_textbox.click()

    # 填写基本信息2
    def fill2_ks_all_info(self, ssnInfo: SsnInfo, isContinue):
        waitload = WebDriverWait(self.driver, 10)
        waitload.until(EC.presence_of_element_located((By.ID, "btnNext")))

        genderM_radio = self.driver.find_element_by_id("rblGender_1")
        genderF_radio = self.driver.find_element_by_id("rblGender_0")
        action = ActionChains(self.driver)
        if ssnInfo.gender == "M":
            action.move_to_element(genderM_radio)
        else:
            action.move_to_element(genderF_radio)
        action.click()
        action.perform()

        birthday_textbox = self.driver.find_element_by_id("txtDOB")
        birthday_textbox.clear()
        birthday_textbox.send_keys(ssnInfo.birth_month + "/" + ssnInfo.birth_day + "/" + ssnInfo.birth_year)

        firstname_textbox = self.driver.find_element_by_id("txtFirstName")
        firstname_textbox.clear()
        firstname_textbox.send_keys(ssnInfo.first_name)

        lastname_textbox = self.driver.find_element_by_id("txtLastName")
        lastname_textbox.clear()
        lastname_textbox.send_keys(ssnInfo.last_name)

        mailAddress_textbox = self.driver.find_element_by_id("txtMailAddr")
        mailAddress_textbox.clear()
        mailAddress_textbox.send_keys(ssnInfo.address)

        zip_textbox = self.driver.find_element_by_id("txtZip")
        zip_textbox.clear()
        zip_textbox.send_keys(ssnInfo.zip)

        city_textbox = self.driver.find_element_by_id("txtCity")
        city_textbox.clear()
        city_textbox.send_keys(ssnInfo.city)

        selectStata = self.driver.find_element_by_id("ddnState")
        for i in range(101):
            time.sleep(1)
            print(i)
            if selectStata.get_attribute("value") != "":
                break

        checkMail_textbox = self.driver.find_element_by_id("chkMailVerify")
        checkMail_textbox.click()

        zipLive_textbox = self.driver.find_element_by_id("txtResidentZIP")
        zipLive_textbox.clear()
        zipLive_textbox.send_keys(ssnInfo.zip)

        txtDriversLic_textbox = self.driver.find_element_by_id("txtDriversLic")
        txtDriversLic_textbox.click()

        selectCounty = self.driver.find_element_by_id("ddnResidentCounty")
        for i in range(101):
            time.sleep(1)
            if selectCounty.get_attribute("value") != "":
                break

        city_textbox = self.driver.find_element_by_id("txtCity")
        city_textbox.clear()
        city_textbox.send_keys(ssnInfo.city)

        if isContinue:
            btnNext = self.driver.find_element_by_id("btnNext")
            btnNext.click()

    def fill3_ks_all_info(self, ssnInfo: SsnInfo, isContinue):

        waitload = WebDriverWait(self.driver, 10)
        waitload.until(EC.presence_of_element_located((By.ID, "btnNext")))

        rblRace_5 = self.driver.find_element_by_id("rblRace_5")
        action = ActionChains(self.driver)
        action.move_to_element(rblRace_5)
        action.click()
        action.perform()

        rblEthnic_2 = self.driver.find_element_by_id("rblEthnic_2")
        action = ActionChains(self.driver)
        action.move_to_element(rblEthnic_2)
        action.click()
        action.perform()

        rblCitizen_0 = self.driver.find_element_by_id("rblCitizen_0")
        action = ActionChains(self.driver)
        action.move_to_element(rblCitizen_0)
        action.click()
        action.perform()

        BodyContent_MainContent_fvUserForm_rblVeteran_1 = self.driver.find_element_by_id(
            "BodyContent_MainContent_fvUserForm_rblVeteran_1")
        action = ActionChains(self.driver)
        action.move_to_element(BodyContent_MainContent_fvUserForm_rblVeteran_1)
        action.click()
        action.perform()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "rblSpouseVeteran_1")))

        rblSpouseVeteran_1 = self.driver.find_element_by_id(
            "rblSpouseVeteran_1")
        action = ActionChains(self.driver)
        action.move_to_element(rblSpouseVeteran_1)
        action.click()
        action.perform()

        rblMigrant_1 = self.driver.find_element_by_id(
            "rblMigrant_1")
        action = ActionChains(self.driver)
        action.move_to_element(rblMigrant_1)
        action.click()
        action.perform()

        ddnHighestEducation_select = self.driver.find_element_by_id("ddnHighestEducation")
        allOptions = ddnHighestEducation_select.find_elements_by_tag_name("option")
        for option in allOptions:
            if "Less than High School" in option.text:
                option.click()
                break

        BodyContent_MainContent_fvUserForm_ddnTrainVocational_select = self.driver.find_element_by_id(
            "BodyContent_MainContent_fvUserForm_ddnTrainVocational")

        allOptions2 = BodyContent_MainContent_fvUserForm_ddnTrainVocational_select.find_elements_by_tag_name("option")
        for option in allOptions2:
            if "Never attended" in option.text:
                option.click()
                break

        rblWorkAnyEmployer_1 = self.driver.find_element_by_id(
            "rblWorkAnyEmployer_1")
        action = ActionChains(self.driver)
        action.move_to_element(rblWorkAnyEmployer_1)
        action.click()
        action.perform()

        txtMothersMaiden_textbox = self.driver.find_element_by_id("txtMothersMaiden")
        txtMothersMaiden_textbox.clear()
        txtMothersMaiden_textbox.send_keys(ssnInfo.security_code)

        if isContinue:
            btnNext = self.driver.find_element_by_id("btnNext")
            btnNext.click()

    # 填写第四页 https://www.getkansasbenefits.gov/Initial/ExQuestions.aspx
    def fill4_ks_all_info(self, isContinue):

        waitload = WebDriverWait(self.driver, 10)
        waitload.until(EC.presence_of_element_located((By.ID, "btnNext")))

        rblWorkedOutsideKS_1 = self.driver.find_element_by_id(
            "rblWorkedOutsideKS_1")
        action = ActionChains(self.driver)
        action.move_to_element(rblWorkedOutsideKS_1)
        action.click()
        action.perform()

        rblWorkedFederal_1 = self.driver.find_element_by_id(
            "rblWorkedFederal_1")
        action = ActionChains(self.driver)
        action.move_to_element(rblWorkedFederal_1)
        action.click()
        action.perform()

        rblActiveMilitary_1 = self.driver.find_element_by_id(
            "rblActiveMilitary_1")
        action = ActionChains(self.driver)
        action.move_to_element(rblActiveMilitary_1)
        action.click()
        action.perform()

        rblOtherClaims_1 = self.driver.find_element_by_id(
            "rblOtherClaims_1")
        action = ActionChains(self.driver)
        action.move_to_element(rblOtherClaims_1)
        action.click()
        action.perform()

        rblRailroad_1 = self.driver.find_element_by_id(
            "rblRailroad_1")
        action = ActionChains(self.driver)
        action.move_to_element(rblRailroad_1)
        action.click()
        action.perform()

        if isContinue:
            btnNext = self.driver.find_element_by_id("btnNext")
            btnNext.click()

    # 填写第四页 https://www.getkansasbenefits.gov/Initial/MyEmployers.aspx
    def fill4_1_ks_all_info(self, ssnInfo: SsnInfo, isContinue):

        waitload = WebDriverWait(self.driver, 10)
        waitload.until(EC.presence_of_element_located((By.ID, "btnEmpAddNone")))

        if isContinue:
            btnEmpAddNone = self.driver.find_element_by_id("btnEmpAddNone")
            btnEmpAddNone.click()
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.ID, "empManual")))
            if isContinue:
                empManual = self.driver.find_element_by_id("empManual")
                empManual.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "BodyContent_MainContent_txtManualName")))

        BodyContent_MainContent_txtManualName = self.driver.find_element_by_id("BodyContent_MainContent_txtManualName")
        BodyContent_MainContent_txtManualName.clear()
        BodyContent_MainContent_txtManualName.send_keys(ssnInfo.employer)

        BodyContent_MainContent_txtManualAddr = self.driver.find_element_by_id("BodyContent_MainContent_txtManualAddr")
        BodyContent_MainContent_txtManualAddr.clear()
        BodyContent_MainContent_txtManualAddr.send_keys(ssnInfo.address)

        BodyContent_MainContent_txtManualCity = self.driver.find_element_by_id("BodyContent_MainContent_txtManualCity")
        BodyContent_MainContent_txtManualCity.clear()
        BodyContent_MainContent_txtManualCity.send_keys(ssnInfo.city)

        ddnManualState = self.driver.find_element_by_id(
            "ddnManualState")
        allOptions1 = ddnManualState.find_elements_by_tag_name("option")
        for option in allOptions1:
            if ssnInfo.state in option.get_attribute("value"):
                option.click()
                break

        BodyContent_MainContent_txtManualZIP = self.driver.find_element_by_id("BodyContent_MainContent_txtManualZIP")
        BodyContent_MainContent_txtManualZIP.clear()
        BodyContent_MainContent_txtManualZIP.send_keys(ssnInfo.zip)

        BodyContent_MainContent_ddnNAICS = self.driver.find_element_by_id(
            "BodyContent_MainContent_ddnNAICS")
        allOptions2 = BodyContent_MainContent_ddnNAICS.find_elements_by_tag_name("option")
        for option in allOptions2:
            if "721110" in option.get_attribute("value"):
                option.click()
                break

        if isContinue:
            btnManualAdd = self.driver.find_element_by_id("btnManualAdd")
            btnManualAdd.click()

    # 填写第四页 https://www.getkansasbenefits.gov/Initial/EditEmployer.aspx
    def fill4_2_ks_all_info(self, ssnInfo: SsnInfo, isContinue):

        waitload = WebDriverWait(self.driver, 10)
        waitload.until(EC.presence_of_element_located((By.ID, "btnSave")))

        BodyContent_MainContent_txtWorkFirstDt = self.driver.find_element_by_id(
            "BodyContent_MainContent_txtWorkFirstDt")
        BodyContent_MainContent_txtWorkFirstDt.clear()
        BodyContent_MainContent_txtWorkFirstDt.send_keys(ssnInfo.job_begin)

        BodyContent_MainContent_txtWorkLastDt = self.driver.find_element_by_id(
            "BodyContent_MainContent_txtWorkLastDt")
        BodyContent_MainContent_txtWorkLastDt.clear()
        BodyContent_MainContent_txtWorkLastDt.send_keys(ssnInfo.job_end_date)

        BodyContent_MainContent_txtWorkLocation = self.driver.find_element_by_id(
            "BodyContent_MainContent_txtWorkLocation")
        BodyContent_MainContent_txtWorkLocation.clear()
        BodyContent_MainContent_txtWorkLocation.click()
        BodyContent_MainContent_txtWorkLocation.send_keys(ssnInfo.city)

        ddnReasonLeaving = self.driver.find_element_by_id(
            "ddnReasonLeaving")
        allOptions1 = ddnReasonLeaving.find_elements_by_tag_name("option")
        for option in allOptions1:
            if "8" in option.get_attribute("value"):
                option.click()
                break

        # BodyContent_MainContent_divUnionHiring = self.driver.find_element_by_id(
        #     "BodyContent_MainContent_divUnionHiring")
        # BodyContent_MainContent_rblUnionHiring_0 = BodyContent_MainContent_divUnionHiring.find_element_by_tag_name(
        #     "label")
        # BodyContent_MainContent_rblUnionHiring_0.click()
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.presence_of_element_located((By.ID, "BodyContent_MainContent_rblUnionHiring_0")))
        #
        BodyContent_MainContent_rblUnionHiring_0 = self.driver.find_element_by_id(
            "BodyContent_MainContent_rblUnionHiring_0")

        self.driver.execute_script("arguments[0].click();", BodyContent_MainContent_rblUnionHiring_0)
        # time.sleep(3)
        # self.driver.execute_script('window.scrollTo(800,0);')
        # BodyContent_MainContent_rblUnionHiring_0.click()
        # action = ActionChains(self.driver)
        # action.move_to_element(BodyContent_MainContent_rblUnionHiring_0)
        # action.click()
        # action.perform()
        #
        # print(BodyContent_MainContent_rblUnionHiring_0)

        txtJobTitle = self.driver.find_element_by_id("txtJobTitle")
        txtJobTitle.clear()
        if ssnInfo.occupation == "":
            txtJobTitle.send_keys("owner")
        else:
            txtJobTitle.send_keys(ssnInfo.occupation)

        txtSkillSet1 = self.driver.find_element_by_id("txtSkillSet1")
        txtSkillSet1.clear()
        if ssnInfo.occupation == "":
            txtSkillSet1.send_keys("owner")
        else:
            txtSkillSet1.send_keys(ssnInfo.occupation)

        txtSkillSet2 = self.driver.find_element_by_id("txtSkillSet2")
        txtSkillSet2.clear()
        if ssnInfo.occupation == "":
            txtSkillSet2.send_keys("owner")
        else:
            txtSkillSet2.send_keys(ssnInfo.occupation)

        if isContinue:
            btnSave = self.driver.find_element_by_id("btnSave")
            btnSave.click()

    # 填写第四页
    def fill4_3_ks_all_info(self, isContinue):

        waitload = WebDriverWait(self.driver, 10)
        waitload.until(EC.presence_of_element_located((By.ID, "btnNext")))

        if isContinue:
            btnNext = self.driver.find_element_by_id("btnNext")
            btnNext.click()

    # 填写第5项目
    def fill5_ks_all_info(self, isContinue):

        waitload = WebDriverWait(self.driver, 10)
        waitload.until(EC.presence_of_element_located((By.ID, "btnNext")))

        rblIsRecvSSDPayments_1 = self.driver.find_element_by_id("rblIsRecvSSDPayments_1")
        action = ActionChains(self.driver)
        action.move_to_element(rblIsRecvSSDPayments_1)
        action.click()
        action.perform()

        rblIsCorpOfficer_1 = self.driver.find_element_by_id("rblIsCorpOfficer_1")
        action = ActionChains(self.driver)
        action.move_to_element(rblIsCorpOfficer_1)
        action.click()
        action.perform()

        rblSelfEmployed_1 = self.driver.find_element_by_id("rblSelfEmployed_1")
        action = ActionChains(self.driver)
        action.move_to_element(rblSelfEmployed_1)
        action.click()
        action.perform()

        rblHasSeverance_1 = self.driver.find_element_by_id("rblHasSeverance_1")
        action = ActionChains(self.driver)
        action.move_to_element(rblHasSeverance_1)
        action.click()
        action.perform()

        if isContinue:
            btnNext = self.driver.find_element_by_id("btnNext")
            btnNext.click()

    # 填写第6项目
    def fill6_ks_all_info(self, isContinue):

        waitload = WebDriverWait(self.driver, 10)
        waitload.until(EC.presence_of_element_located((By.ID, "btnNext")))

        chkReadUnderstood = self.driver.find_element_by_id("chkReadUnderstood")
        chkReadUnderstood.click()

        chkCovid19 = self.driver.find_element_by_id("chkCovid19")
        self.driver.execute_script("arguments[0].click();", chkCovid19)

        chkCertYes = self.driver.find_element_by_id("chkCertYes")
        self.driver.execute_script("arguments[0].click();", chkCertYes)

        if isContinue:
            btnNext = self.driver.find_element_by_id("btnNext")
            btnNext.click()

        # 填写第6项目

    def fill6_1_ks_all_info(self, isContinue):

        waitload = WebDriverWait(self.driver, 10)
        waitload.until(EC.presence_of_element_located((By.ID, "btnUpdate")))

        txtRoutingNumber = self.driver.find_element_by_id("txtRoutingNumber")
        txtRoutingNumber.clear()
        txtRoutingNumber.send_keys("073972181")

        txtBankAccount = self.driver.find_element_by_id("txtBankAccount")
        txtBankAccount.clear()
        txtBankAccount.send_keys("3250146480445")

        txtVerifyBankAccount = self.driver.find_element_by_id("txtVerifyBankAccount")
        txtVerifyBankAccount.clear()
        txtVerifyBankAccount.send_keys("3250146480445")

        if isContinue:
            btnUpdate = self.driver.find_element_by_id("btnUpdate")
            btnUpdate.click()

    def fill9_ks_all_info(self, isContinue):
        UserAndDate = self.driver.find_element_by_id("UserAndDate")
        uid1 = UserAndDate.get_attribute("innerHTML")
        # print(uid1)
        paraKansasWorksRegNew = self.driver.find_element_by_id("paraKansasWorksRegNew")
        uid2 = paraKansasWorksRegNew.get_attribute("innerHTML")
        # print(uid2)
