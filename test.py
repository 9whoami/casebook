#!/usr/bin/python
# -*- coding: UTF-8 -*-

from api_methods import ApiMethods

__project__ = 'casebook'
__date__ = ''
__author__ = 'andreyteterevkov'

api = ApiMethods()

url = 'Account/LogOn'
post_data = {
    'UserName': 'nemotest@gmail.com',
    'Password': 'engrave',
    'RememberMe': True,
    'SystemName': 'sps'
}

print(api.request(url=url, **post_data))
print(api.request(url='/Search/Sides?name=%D0%9B%D1%83%D0%BA%D0%BE%D0%B9%D0%BB'))
