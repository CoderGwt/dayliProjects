# !/usr/bin/python
"""
第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，
    为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

分析：
    1.结果类似：3FSNMKHUA9GG；由12为字符组成，字符包括数字和大写字母。随机生成
        使用string模块可以直接生成A-Z和0-9 一大串字符
    2.使用random模块 和 string模块

"""
# FileName: py_01.py
# Author: weitao
# Date: 2018/09/02/15:12

import random
import string

# todo 知识点回顾
print(string.ascii_uppercase)  # todo 打印出A-Z大写
print(string.ascii_lowercase)  # todo 打印a-z小写
print(string.ascii_letters)  # todo  打印a-z小写 A-Z大写

# todo 类型全部都是字符串
print(type(string.ascii_uppercase),
      type(string.ascii_letters),
      type(string.ascii_lowercase))

print(string.digits)  # todo 打印0-9
print(type(string.digits))  # todo 类型也是字符串
print(random.choice("python"))  # todo 从一个字符串中随机获取一个字符

print(string.ascii_uppercase + string.digits)  # todo 生成A-Z0-9一大串字符


# todo 案例核心内容

print("*" * 100)


def random_str(number):
    """
        生成随机码
    :param number: 指定要生成多少位数
    :return: 随机码
    """
    result = ""  # todo 用一个变量保存生成的随机码
    for i in range(number):
        result += random.choice(string.ascii_uppercase + string.digits)
    return result


def two_hundred_code():
    """
        生成200个随机码
    :return: 200个随机码
    """
    total_num = 200  # todo 总共生成200个随机码
    number = 12  # todo 每一个随机码多少字符
    for i in range(total_num):
        print("number: {}, result: {}".format(i+1, random_str(number)))


two_hundred_code()  # todo 调用函数