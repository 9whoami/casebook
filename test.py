#!/usr/bin/python
# -*- coding: UTF-8 -*-

__project__ = 'amazon_seller2'
__date__ = ''
__author__ = 'andreyteterevkov'


import urllib.request
import urllib.parse

data = urllib.parse.urlencode({'data': 'adasdasdasd'})
data = data.encode('ascii')
with urllib.request.urlopen("http://188.187.190.2:8011/company/new/biusnes_cards", data) as f:
    print(f.read().decode('utf-8'))
