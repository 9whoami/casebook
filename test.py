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

post_data = {
    "Address": "198095, Г САНКТ-ПЕТЕРБУРГ, УЛ ТРЕФОЛЕВА, 9 ЛИТЕР А ПОМ 11Н",
    "Inn": "7805441145",
    "Name": 'ЛИКВИДАЦИОННАЯ КОМИССИЯ ООО "Мир тканей" (НАЗНАЧЕНИЕ ЛИКВИДАТОРА)',
    "Ogrn": "1077847617440",
    "Okpo": "82231048",
    "IsPhysical": False,
    "OrganizationId": 0,
    "IsUnique": False
}

print(api.request(url='Card/BusinessCard', **post_data))
