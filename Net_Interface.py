#!/usr/bin/env python

import netifaces
import socket

def decor(func):
    def wrap():
        print('\n=======================')
        print(func)
        print('=======================\n')
    return wrap

class Network(object):
    """Compile interfaces with IPv4."""
    def __init__(self, hostname, interfaces):
        self.hostname = hostname
        self._interfaces = interfaces


    def interfaces_f(self):
        return netifaces.interfaces()

    def hostname_f(self):
        return self.hostname

    def get_card(self, card):
        for interface in self.interfaces_f():
            if card in interface:
                return card

    def attempt_ip(self, arg):
        ip_card = netifaces.ifaddresses(arg)[2][0]['addr']
        return ip_card

def main():
    network = Network(socket.gethostname(), netifaces.interfaces())

    decorated = decor(network.hostname_f())
    decorated()

    for index in network.interfaces_f():
        try:
            print('{}: {}'.format(index, network.attempt_ip(index)))
        except:
            pass

if __name__ == '__main__':
    main()
