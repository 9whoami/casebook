#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

from api_methods import CasebookAPI
from api_methods import MainAPI
from config import Conf

__author__ = "wiom"
__version__ = "1.1.3"
__date__ = "10.08.16 8:23"
__description__ = """"""
start_time = time.monotonic()


def check_result(result):
    if bool(result.get('Success')) is False:
        raise Exception(result.get('Message', result))
    else:
        return result


def page_iterator(fun: classmethod, key: str = None, **kwargs) -> tuple:
    container = tuple()
    page = 0

    while True:
        page += 1
        kwargs['page'] = page

        result = check_result(fun(**kwargs))

        items = result['Result'][key] if key else result['Result']

        if not len(items) or page > result['Result'].get('PagesCount', page):
            break
        else:
            container += tuple(items)

    return container

casebook = CasebookAPI(section='casebook')
main_server = MainAPI(section='mainapi')
config = Conf(section='base')

login_result = casebook.login(email=config.login, passwd=config.password)
if not login_result is True:
    raise SystemExit(login_result)

line_start = int(config.start_line)
count_line_limit = int(config.line_count)
count_line = 0


for line, company_name in enumerate(open(config.filename, 'r'), 1):
    if line_start and line < line_start:
        continue
    else:
        count_line += 1

    if count_line_limit and count_line > count_line_limit:
        break

    sides = page_iterator(casebook.sides_search, 'Items', name=company_name)

    print(line, company_name, 'items: ', len(sides))

    for i, side in enumerate(sides, 1):
        print(i, '/', len(sides))

        company_id = main_server.add_new_accouns(
            casebook.get_buisnes_card(**side))
        if company_id == -1:
            raise SystemExit(main_server.get_last_error())

        # получение информации о бухгалтерской отчетности
        accounting = check_result(casebook.get_accounting_stat(inn=side['Inn']))

        accountings = []
        date_time_ranges = accounting['Result']['AvailableDateTimeRanges']

        if date_time_ranges:
            for date_time in date_time_ranges:

                buff = casebook.get_accounting_stat(
                    inn=side['Inn'],
                    year_from=min(date_time_ranges[date_time]),
                    year_to=max(date_time_ranges[date_time]))

                accountings.append(buff['Result'])

        main_server.accounting = accountings

        # получение ссылки на ЕГРЮЛ
        main_server.egrul = casebook.get_egrul_link(**side)

        # получение информации по лицензиям
        main_server.license = page_iterator(casebook.get_license, 'Items',
                                            ogrn=side['Ogrn'], inn=side['Inn'])

        main_server.contracts = page_iterator(
            casebook.get_state_contracts, 'contracts', inn=side['Inn'])

        main_server.audits = page_iterator(
            casebook.get_audit, 'Items', inn=side['Inn'])

        main_server.executory_processes = page_iterator(
            casebook.get_executory_processes, 'ExecutoryProcesses', **side)

        main_server.cases = page_iterator(casebook.get_cases, 'Items', **side)

        main_server.executory_processes_statistics = \
            check_result(casebook.get_executory_processes_statistics(**side))

        main_server.cases_stat = check_result(casebook.get_org_stat(**side))

        main_server.run_tasks(company_id)

main_server.waiting_for()

print('Elapsed rime: {}'.format(time.monotonic() - start_time))
