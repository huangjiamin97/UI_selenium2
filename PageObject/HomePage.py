from selenium.webdriver.common.by import By

from Basepage.basepage import BasePage
from PageObject.admin_page import admin_page

from until import parseConfFile
from until.parseConfFile import parseConf_file


class Home_page(BasePage):
    _url = "http://oa.zhidaitech.com:9002/login?redirect=%2Fzbtj%2Fjghx%2Fhxlv3"
    do_conf = parseConf_file()
    '''
    获取登录页用户名
    '''
    # username = do_conf.get_locators_or_account('LoginAccount','username')

    '''
    获取登录密码
    '''
    # pwd = do_conf.get_locators_or_account('LoginAccount','password')


    '''
    获取登录元素
    '''
    username_element = do_conf.get_locators_or_account('LoginPageElements','account')
    pwd_element = do_conf.get_locators_or_account('LoginPageElements','password')
    logins = do_conf.get_locators_or_account('LoginPageElements','login')


    def login(self,username,pwd):
        # self.find_element(By.CSS_SELECTOR,'.el-input__inner').send_keys('uatzzq')

        self.finds_element(*Home_page.username_element).send_keys(username)

        self.finds_element(*Home_page.pwd_element).send_keys(pwd)
        self.finds_element(*Home_page.logins).click()
        return admin_page(self._driver)




