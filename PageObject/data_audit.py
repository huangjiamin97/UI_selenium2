from selenium.webdriver.common.by import By

from Basepage.basepage import BasePage


class data_audit(BasePage):
    def hos_audit(self):
        self.find_element(By.CSS_SELECTOR,'.is-focus > input:nth-child(1)').click()
        self.find_element(By.CSS_SELECTOR,'span.is-checked > span:nth-child(1)').click()