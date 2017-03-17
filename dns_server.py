#!/usr/bin/env python3
# coding: utf-8

"""
AUTHOR: Yuanhao Wu
获取DNS服务器信息
"""

import os, re
import subprocess


def dns_server():
    addr_list = []
    res = subprocess.run('gsh list_dns_server_address all',
                         stdout=subprocess.PIPE)
    addr_list = re.findall(r'-ip (\d+\.\d+\.\d+\.\d+)+? ', res)
    print(addr_list)

if __name__ == '__main__':
    dns_server()