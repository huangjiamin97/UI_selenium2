from time import sleep

from PageObject.HomePage import Home_page


class Test_Homepage:
    def setup(self):
        self.hp = Home_page()

    def teardown(self):

        self.hp.close_chrome()

    def test_login(self):

        self.hp.login()

        # sleep(5)
        assert self.hp.is_visible("#breadcrumb-container > span > span:nth-child(1) > span.el-breadcrumb__inner > a") is True

        sleep(5)

    def test_audit(self):
        self.hp.login().data_audit().hos_audit()

