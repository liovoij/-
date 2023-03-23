# coding:utf-8
import os

# 系统根目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 测试数据目录
xlsx_dir = os.path.join(base_dir, 'testdata', '通讯工具.xlsx')
# 测试接口目录
request_dir = os.path.join(base_dir, 'requestconfig', 'requset_config.ini')


if __name__ == '__main__':
    print(base_dir)
    print(xlsx_dir)
    print(request_dir)
