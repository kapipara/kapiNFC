#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import nfc
import sys
import os

class getNFCtags():
    def __init__(self):

    def main(self):
        print("[NFC] : ready...")
        clf = nfc.ContactlessFrontend('usb:054c:06c3')
        if clf is not None:
            clf.connect(rdwr={
                'on-startup': startupNFC,
                'on-connect': connectNFC,
                'on-release': released,
            })
        else:
            print("[NFC}] : Error!")

    def startupNFC(self):
        
