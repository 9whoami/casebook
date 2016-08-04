#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pickle

from api_methods import CasebookAPI
from base64 import b64encode, b64decode
import simplejson

__project__ = 'casebook'
__date__ = ''
__author__ = 'andreyteterevkov'


def char_escape(in_str: str) -> str:
    escape_chars = ['"', "'", '(', ')']
    out_str = ''
    for char in in_str:
        if char in escape_chars:
            out_str += '\\'
        out_str += char
    return out_str


def store_backup(obj, dmp_file='obj.dmp'):
    with open(dmp_file, 'wb') as f:
        pickle.dump(obj=obj, file=f, protocol=-1)


def load_backup(dmp_file='obj.dmp'):
    obj = None
    try:
        with open(dmp_file, 'rb') as f:
            obj = pickle.load(file=f)
    except Exception:
        obj = None
    finally:
        return obj


api = CasebookAPI()

if not api.login(email='nemotest@gmail.com', passwd='engrave'):
    raise SystemExit('Не удалось войти')

company = api.web_search(name='лукоил')

# company = load_backup()

if company.get('error') or company.get('Success') is False:
    print(company)
else:
    # target_company_info = {key: company['Result']['Items'][6].get(key) for key in ["Address", "Name", "Ogrn", "Okpo", "IsPhysical", "OrganizationId", "IsUnique"]}
    # print(target_company_info['Name'])
    # target_company_info = simplejson.dumps(target_company_info)
    # print(b64encode(target_company_info.encode('utf-8')))
    # print(company['Result']['Items'][6])
    for x in company['Result']['Items']:
        inn = str(x['Inn'])
        stat = api.accounting_stat(inn)
        print(stat['Result']['AvailableDateTimeRanges'])
