#!/usr/bin/python3
# coding: utf-8

import dns.resolver

import ping


def dns_query(addr):
    my_resolver = dns.resolver.Resolver()
    #my_resolver.nameservers = addr
    answer = my_resolver.query(input('Input your FQDN: '), 'A')
    for i in answer.response.answer:
        for j in i.items:
            print(j.address)

if __name__ == '__main__':
    dns_list = ping.get_avail_dns()
    for _ in dns_list:
        dns_query(_)