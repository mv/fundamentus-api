#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import requests
import requests_cache

requests_cache.install_cache('.example_cache')

def main():

    # Once cached, delayed page will be taken from cache
    # redirects also handled
    print('\nEnabled:')
    with requests_cache.enabled():
        for i in range(5):
            j = requests.get('https://httpbin.org/uuid').json()['uuid']
            r = requests.get('https://httpbin.org/delay/2')
            print('  Request {}: code = {}, uuid = {}, cached = {}'.format(i,r,j,r.from_cache))


    # And if we need to get fresh page or don't want to cache it?
    print('\n\nDisabled:')
    with requests_cache.disabled():
        print('  IP  : ' + requests.get('http://httpbin.org/ip').json()['origin'])
        print('  UUID: ' + requests.get('http://httpbin.org/uuid').json()['uuid'])

    # Debugging info about cache
#   print(requests_cache.get_cache())

if __name__ == "__main__":
    t = time.time()
    main()
    print('\nElapsed: %.3f seconds/n' % (time.time() - t))

