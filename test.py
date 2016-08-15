#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

__project__ = 'casebook'
__date__ = ''
__author__ = 'andreyteterevkov'


t = time.monotonic()
time.sleep(0.2)
print(time.monotonic() - t)