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
    res = subprocess.run(['nslookup', 'www.google.com'],
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    addr_list = re.findall(r'Address:\s+(\d+\.\d+\.\d+\.\d+)+?',
                           res.stdout.decode('utf-8'))
    return addr_list

if __name__ == '__main__':
    dns_server()