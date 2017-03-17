#!/usr/bin/env python3
# coding: utf-8

"""
Author: Yuanhao Wu
用于PING的模块
为了兼容WINDOWS和LINUX，增加系统判断，及对应参数赋值
"""

import os, subprocess

import dns_server


def _ping(addr):
    if os.name == 'nt':
        count = '-n'
        # output = '> nul'
    else:
        count = '-c'
        # output = '&> /dev/null'
    res = subprocess.run(('ping {} 3 {}'.format(count, addr)),
                         shell=True, stdout=subprocess.DEVNULL)
    if res.returncode:
        print('DNS server {} cannot connect...'.format(addr))
        return -1
    else:
        print('DNS server {} OK!'.format(addr))
        return None


def get_avail_dns():
    addr_list = dns_server.dns_server()
    avail_dns = set()
    for _ in addr_list:
        # If the dns is ping-able, add the DNS ip into the set
        if not _ping(_):
            avail_dns.add(_)

    if not avail_dns:
        print('There is no available DNS server.')
    else:
        return avail_dns


if __name__ == '__main__':
    get_avail_dns()
