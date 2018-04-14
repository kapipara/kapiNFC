#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import nfc 

def on_connect(tag):
    tmp = str(tag)
    splitOut = tmp.replace('=',' ').split()
    print splitOut[2]

def on_startup(tag):
    print("[NFCreader] : ready")
    return tag

def main():
    with nfc.ContactlessFrontend('usb') as clf:
        clf.connect(rdwr = {
            'on-startup':on_startup,
            'on-connect':on_connect
            })

if __name__ == '__main__':
    main()

