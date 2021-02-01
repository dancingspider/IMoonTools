import requests
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class AdspowerController:
    def __init__(self):
        self.chrome_driver_exe = "chromedriver.exe"
        self.open_url = "http://local.adspower.net:50325/api/v1/browser/start?user_id="
        self.close_url = "http://local.adspower.net:50325/api/v1/browser/stop?user_id="
        self.set_proxy_url = "http://local.adspower.net:50325/api/v1/user/update?user_id="
        self.driver = None

    def open_adspower(self, ads_id):
        resp = requests.get(self.open_url + ads_id).json()
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
        self.driver = webdriver.Chrome(self.chrome_driver_exe, options=chrome_options)

    def close_adspower_browser(self, ads_id):
        requests.get(self.close_url + ads_id)

    def set_proxy_city(self, user_id, country, region, city):
        data = {'user_id': user_id, 'country': country, 'region': region, 'city': city}
        # myjson = json.dumps(data)
        print(data)
        resp = requests.post(self.set_proxy_url, data).json()
        print(resp)
        if resp["msg"] == "Success":
            return True
        else:
            return False
