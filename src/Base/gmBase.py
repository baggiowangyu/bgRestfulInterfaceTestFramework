# -*- coding: utf-8 -*-

import sys

def print_chinese(string):
    # 首先判断当前运行环境是什么编码的，如果不是utf-8的就转成GBK
    print string#.decode("utf-8").encode("gbk")


if __name__ == '__main__':
    print_chinese("汉字")