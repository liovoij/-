# coding:utf-8
import configparser
from requestconfig.use_config import *


class ParseConfile(object):
    def __init__(self):
        self.file = request_dir
        self.conf = configparser.ConfigParser()
        self.read = self.conf.read(self.file)

    # 获取所有的sections，返回一个列表
    def get_sections(self):
        return self.conf.sections()

    # 获取指定section下所有的option，返回列表
    def get_options(self, section):
        return self.conf.options(section)

    # 获取指定section，指定option对应的数据，返回元组和字符串
    def get_account(self, section, option):
        try:
            locator = self.conf.get(section, option)
            if '->' in locator:
                locator = tuple(locator.split('->'))
            return locator
        except configparser.NoOptionError as e:
            print('error:', e)
        return 'error: No option "{}" in section : "{}" '.format(option, section)

    # 获取指定section下所有的option和对应的数据，返回字典
    def get_value(self, section):
        value = dict(self.conf.items(section))
        return value


if __name__ == '__main__':
    print(ParseConfile().get_sections())
    print(ParseConfile().get_options('new_demo'))
    print(ParseConfile().get_account('new_demo', 'host'))
    print(ParseConfile().get_value('new_demo'))

