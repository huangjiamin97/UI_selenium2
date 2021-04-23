from selenium.webdriver.common.by import By

from Basepage.basepage import BasePage
from PageObject.admin_page import admin_page


class Home_page(BasePage):
    _url = "http://oa.zhidaitech.com:9002/login?redirect=%2Fzbtj%2Fjghx%2Fhxlv3"

    def login(self):
        # self.find_element(By.CSS_SELECTOR,'.el-input__inner').send_keys('uatzzq')
        self.action_yaml('../Data/action.yaml')
        self.find_element(By.CSS_SELECTOR,'div.el-form-item:nth-child(3) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)').send_keys('Mandala#p@ssw0rd')
        self.find_element(By.CSS_SELECTOR,'.el-button').click()
        return admin_page(self._driver)
