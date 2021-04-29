import yaml
from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import ui
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC



class BasePage:
    _driver = None
    _url = ""
    def __init__(self, driver:WebDriver = None):
        self.byDic = {
            'id': By.ID,
            'name': By.NAME,
            'class_name': By.CLASS_NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT,
            'css_selector':By.CSS_SELECTOR
        }
        if driver is None:
            # self._driver = webdriver.Chrome()
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            self._driver = webdriver.Chrome(chrome_options=chrome_options)


        else:
            self._driver = driver

        if  self._url !="":

            self._driver.get(self._url)

    def finds_element(self, by, locator):

        # try:
        #     # print('[Info:Starting find the element "{}" by "{}"!]'.format(locator, by))
        #     element = WebDriverWait(self._driver, timeout=20).until(lambda x: x.find_element(by, locator))
        # except TimeoutException as t:
        #     print('error: found "{}" timeout!'.format(locator), t)
        # else:
        #     return element
        return self._driver.find_element(self.byDic[by], locator)

    def close_chrome(self):
        self._driver.close()

    '''
    显示等待
    '''
    def is_visible(self,locator, timeout=10):
        try:
            ui.WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except TimeoutException:
            return False

    '''
    解析yaml文件
    '''
    # def action_yaml(self,path):
    #     with open(path) as f:
    #         actions =yaml.safe_load(f)
    #     for action in actions:
    #         if 'by' in action.keys():
    #             element = self.find_element(action["by"], action["locator"])
    #         if 'send_keys' == action['action']:
    #             element.send_keys('uatzzq')

    def get_hsource(self):
        return self._driver.page_source()
