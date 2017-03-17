#!/usr/bin/env python3
# coding: utf-8

"""
Author: Yuanhao Wu
用于PING的模块
为了兼容WINDOWS和LINUX，增加系统判断，及对应参数赋值
"""

import os, subprocess


def ping(addr_list):
    if os.name == 'nt':
        count = '-n'
        # output = '> nul'
    else:
        count = '-c'
        # output = '&> /dev/null'
    for addr in addr_list:
        res = subprocess.run(('ping {} 3 {}'.format(count, addr)),
                             shell=True, stdout=subprocess.DEVNULL)
        if res.returncode:
            print('DNS server {} cannot connect...'.format(addr))
        else:
            print('DNS server {} OK!'.format(addr))

if __name__ == '__main__':
    addr_list = ['8.8.8.8', '1.1.1.1']
    ping(addr_list)
