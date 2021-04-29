import configparser

from config.conf import config_path


class parseConf_file(object):

    def __init__(self):
        self.confpath = config_path
        self.conf = configparser.ConfigParser()
        self.conf.read(self.confpath,encoding='utf-8')

    def get_all_sections(self):
        return self.conf.sections()

    def get_all_options(self,section):
        return self.conf.options(section)


    def get_locators_or_account(self, section, option):
        """获取指定section, 指定option对应的数据, 返回元祖和字符串"""
        try:
            locator = self.conf.get(section, option)
            if ('->' in locator):
                locator = tuple(locator.split('->'))
            return locator
        except configparser.NoOptionError as e:
            print('error:', e)
        return 'error: No option "{}" in section: "{}"'.format(option, section)

    def get_option_value(self, section):
        """获取指定section下所有的option和对应的数据，返回字典"""
        value = dict(self.conf.items(section))
        return value
