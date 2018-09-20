#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Vermouth'

import sys

def test():
    args = sys.argv      # 命令行执行脚本时的参数  类名为第一个参数
    if len(args)==1:
        print('Hello world!')
    elif len(args)==2:
        print('Hello, %s!' %args[1])   # python  hello.py yangfan  打印 Hello yangfan!
    else:
        print('Too many arguments!')

# 字面意思就是  只有我自身调用这个方法的话才会运行，外部调用我这个类的时候并不会执行if段内
if __name__ =='__main__':    # 程序入口，相当于java的main函数
    test()



# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。





