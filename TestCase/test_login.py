from time import sleep

import pytest
import yaml

from PageObject.HomePage import Home_page


class Test_Homepage:
    def setup(self):
        self.hp = Home_page()

    def teardown(self):

        self.hp.close_chrome()

    '''
    用户名，密码正确，登录成功
    '''
    @pytest.mark.parametrize("username, pwd",yaml.safe_load( open('../Data/action.yaml'))[0] )
    def test_login(self,username,pwd):

        self.hp.login(username,pwd)

        # sleep(5)
        assert self.hp.is_visible("span.el-breadcrumb__item:nth-child(1) > span:nth-child(1) > a:nth-child(1)") is True

        sleep(5)

    '''
    用户名错误，登录失败
    '''
    @pytest.mark.parametrize("username, pwd", yaml.safe_load(open('../Data/action.yaml'))[1])
    def test_login_fail(self,username,pwd):
        self.hp.login(username, pwd)

        assert self.hp.is_visible(".el-message__content") is True





    # def test_audit(self):
    #     self.hp.login().data_audit().hos_audit()


if __name__ ==  '__main__':
    pytest.main(['-v','test_login.py::Test_Homepage::test_login_fail'])