#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import monotonic
from api_methods import MainAPI

__project__ = 'casebook'
__date__ = ''
__author__ = 'andreyteterevkov'


main_site = MainAPI(section='mainapi')
start_time = monotonic()

for i in range(3):
    post_data = {'first': i, 'second': i+1}
    print('+'*10, i, '+'*10)
    main_site.audits = post_data
    main_site.contracts = post_data
    main_site.license = post_data
    main_site.executory_processes = post_data
    main_site.executory_processes_statistics = post_data
    main_site.cases = post_data
    main_site.cases_stats = post_data
    main_site.run_tasks(main_site.add_new_accouns(post_data))

print(monotonic() - start_time)
