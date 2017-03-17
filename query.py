#!/usr/bin/python3
# coding: utf-8

import dns.resolver


def dns_query(addr_list):
    my_resolver = dns.resolver.Resolver()
    my_resolver.nameservers = addr_list
    answer = my_resolver.query(input('Input your FQDN: '))
    print(answer.response)

if __name__ == '__main__':
    dns_query(['8.8.8.8'])