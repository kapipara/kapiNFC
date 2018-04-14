#!/usr/bin/env python
#! -*- codeing: utf-8 -*-

import pyudev
context = pyudev.Context()
for device in context.list_devices():
    print(device)


