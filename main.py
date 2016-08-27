#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simplejson
import os
import time

__author__ = "wiom"
__version__ = "0.0.0"
__date__ = "10.08.16 8:23"
__description__ = """"""

from api_methods import CasebookAPI
from api_methods import MainAPI


def page_iterator(container: list, fun: classmethod, key: str = None, **kwargs) -> None:
    page = 0
    while True:
        page += 1
        kwargs['page'] = page
        result = fun(**kwargs)

        if bool(result.get('Success')) is False:
            print(result['Message'])
            break

        if not len(result['Result'][key] if key else result['Result']) or result['Result']['PagesCount'] == page:
            break
        else:
            container += result['Result']

login = 'n.emotest@gmail.com'
passwd = 'miracle'
target_side = 'лукоил'
start_time = time.monotonic()

casebook = CasebookAPI(section='casebook')
main_server = MainAPI(section='mainapi', headers={})

l = casebook.login(email=login, passwd=passwd)
if not l is True:
    raise SystemExit(l)

page = 0
while True:
    page += 1
    search = casebook.sides_search(name=target_side, page=page)
    if search['Success'] is False:
        print(search['Message'])
        break

    if not len(search['Result']['Items']):
        print('Компании не найдены')
        break

    for side in search['Result']['Items']:
        collection_info = {}
        # получение подробной информации о компании
        buisnes_card = casebook.get_buisnes_card(**side)
        # collection_info['biusnes_card'] = buisnes_card.copy()
        company_id = main_server.add_new_accouns(buisnes_card.copy())

        # получение информации о бухгалтерской отчетности
        accounting = casebook.get_accounting_stat(inn=side['Inn'])
        accountings = []
        date_time_ranges = accounting['Result']['AvailableDateTimeRanges']

        if date_time_ranges:
            for date_time in date_time_ranges:
                buff = casebook.get_accounting_stat(inn=side['Inn'],
                                                    year_from=min(date_time_ranges[date_time]),
                                                    year_to=max(date_time_ranges[date_time]))
                accountings.append(buff['Result'])
        # collection_info['accounting'] = accountings[:]
        main_server.accounting = accountings[:]

        # получение ссылки на ЕГРЮЛ
        egrul_link = casebook.get_egrul_link(**side)
        # collection_info['egrul'] = egrul_link
        main_server.egrul = egrul_link

        # получение информации по лицензиям

        license = []
        page_iterator(license, casebook.get_license, 'Items', ogrn=side['Ogrn'], inn=side['Inn'])
        # collection_info['license'] = license[:]
        main_server.license = license[:]

        contracts = []
        page_iterator(contracts, casebook.get_state_contracts, 'contracts', inn=side['Inn'])
        # collection_info['contracts'] = contracts[:]
        main_server.contracts = contracts[:]

        audits = []
        page_iterator(audits, casebook.get_audit, 'Items', inn=side['Inn'])
        # collection_info['audits'] = audits[:]
        main_server.audits = audits[:]

        executory_processes_statistics = casebook.get_executory_processes_statistics(**side)
        # page_iterator(executory_processes_statistics, casebook.get_executory_processes_statistics, **side)
        if executory_processes_statistics:
            # collection_info['executory_processes_statistics'] = executory_processes_statistics['Result'].copy()
            main_server.executory_processes_statistics = executory_processes_statistics['Result'].copy()

        executory_processes = []
        page_iterator(executory_processes, casebook.get_executory_processes, 'ExecutoryProcesses', **side)
        # collection_info['executory_processes'] = executory_processes[:]
        main_server.executory_processes = executory_processes[:]

        cases = []
        page_iterator(cases, casebook.get_cases, 'Items', **side)
        # collection_info['cases'] = cases[:]
        main_server.cases = cases[:]

        cases_stat = casebook.get_org_stat(**side)
        # page_iterator(cases_stat, casebook.get_org_stat, **side)
        if cases_stat:
            # collection_info['cases_stat'] = cases_stat['Result'].copy()
            main_server.cases_stat = cases_stat['Result'].copy()

        main_server.run_tasks(company_id)
        main_server.waiting_for()
        break
    break

print(time.monotonic() - start_time)
