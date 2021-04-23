from selenium.webdriver.common.by import By

from Basepage.basepage import BasePage
from PageObject.data_audit import data_audit


class admin_page(BasePage):

    def data_audit(self):
        if self.is_visible('ul.el-menu:nth-child(1) > div:nth-child(3) > li:nth-child(1) > div:nth-child(1)') is True:
            self.find_element(By.CSS_SELECTOR,'ul.el-menu:nth-child(1) > div:nth-child(3) > li:nth-child(1) > div:nth-child(1)').click()
            self.find_element(By.CSS_SELECTOR,'a.router-link-exact-active > li:nth-child(1)').click()
            return data_audit(self._driver)