# -*- coding: utf-8 -*-

import os
import simplejson
import logging
import urllib.request
import urllib.parse

from grab import Grab
from config import Conf
from threadpool import ThreadPool
from logger import Logger


__author__ = 'whoami'
__version__ = '1.3.3'
__date__ = '19.02.16 23:14'
__description__ = """
Набор методов для работы с апи
"""

conf = Conf(section='base')
th_pool = ThreadPool(max_threads=int(conf.thread_count))
del conf


class AbstractAPI(Grab):
    def __init__(self, loggining=False, section='api'):
        if loggining:
            logger = logging.getLogger('grab')
            logger.addHandler(logging.StreamHandler())
            logger.setLevel(logging.DEBUG)

        config = Conf(section=section)
        self.base_url = config.main_url

        super().__init__(timeout=60, connect_timeout=15, debug=True)

        self.setup(
            log_dir=os.path.abspath('casebook_logs'),
            headers={
                "Content-type": "application/json", "Accept": "application/json"
            }
        )

    def api_request(self, uri: str = '', post_data: dict=None) -> dict:
        response = {'Message': 'Unknown error'}
        try:

            if post_data:
                post_data = simplejson.dumps(post_data, ensure_ascii=False)
            uri = ''.join((self.base_url, uri,))

            self.request(url=uri, post=post_data)
            response = self.response.json

            if isinstance(response, dict) and response.get('error'):
                raise Exception(response['error'])

        except Exception as e:
            response = {'Message': str(e)}
        finally:
            return response


class MainAPI(AbstractAPI):
    """
        188.187.190.2:8011/company/new/{param}

        param:
            accouns
            audits
            biusnes_cards
            cases
            cases_stats
            contracts
            egrul
            executory_processes
            executory_processes_statistics
            license

        Первая всегда идет accouns в post запрос data кладешь json весь в ответ
        получаешь json c id компанией дальше этот аккаунт передаешь со всеми
        остальными те при создании компании 1 параметр data
        со всеми остальными data и id

        В случае успеха
        accouns:
            ['param'=> $param, 'id' => $model->id, 'result' => 1]
        other:
            ['param'=> $param,'result' => 1]

        В случае неудачи
            ['param'=> $param, 'error' => $error]
    """
    _tasks = dict()
    _default_error_message = 'Unknown error'
    _last_error = _default_error_message
    task_id = 1

    def __init__(self, debug=True, log_path='main_server/',
                 loggining=False, section='api'):
        super().__init__(loggining=loggining, section=section)
        # self.logger = Logger(debug=debug, log_path=log_path)

    @th_pool.thread
    def run_tasks(self, company_id):
        if company_id == -1:
            raise ValueError('Account id not found!')

        tasks = self._get_tasks()

        for task_id in tasks:
            # prepare post data
            tasks[task_id]['post_data']['id'] = company_id
            tasks[task_id]['t_id'] = task_id

            # sending post data
            self.api_request(**tasks[task_id])

        return None

    def waiting_for(self):
        th_pool.loop()

    def get_last_error(self):
        return self._last_error

    def add_new_accouns(self, value):
        task = self._make_task(uri=self.biusnes_cards, post_data=value)
        task['t_id'] = self.task_id
        response = self.api_request(**task)

        self._last_error = response.get('Message', self._default_error_message)

        return response.get('id', -1)

    @th_pool.in_lock
    def api_request(self, uri: str = '', post_data=None, t_id=0):
        response = {'Message': 'Unknown error'}
        request_logfile = 'main_server/{}.log'.format(t_id)
        response_logfile = 'main_server/{}.html'.format(t_id)

        try:
            uri = ''.join((self.base_url, uri,))

            with open(request_logfile, 'w') as f:
                request_data = "url: {}\n\npost_data: {}\n"
                f.write(request_data.format(uri, simplejson.dumps(post_data, ensure_ascii=False, indent=2),))

            if post_data:
                post_data = urllib.parse.urlencode(post_data).encode('ascii')

            with urllib.request.urlopen(uri, post_data) as f:
                response = simplejson.loads(f.read().decode('utf-8'))

            with open(response_logfile, 'w') as f:
                f.write(simplejson.dumps(response, ensure_ascii=False, indent=2))

            if response.get('error'):
                raise Exception(response['error'])

        except Exception as e:
            response = {'Message': str(e)}
        finally:
            return response

    @property
    def audits(self):
        return "audits"

    @audits.setter
    def audits(self, value):
        task = self._make_task(uri=self.audits, post_data=value)
        self._add_task(task=task)

    @property
    def accounting(self):
        return "accounting"

    @accounting.setter
    def accounting(self, value):
        task = self._make_task(uri=self.accounting, post_data=value)
        self._add_task(task=task)

    @property
    def biusnes_cards(self):
        return "biusnes_cards"

    @biusnes_cards.setter
    def biusnes_cards(self, value):
        task = self._make_task(uri=self.biusnes_cards, post_data=value)
        self._add_task(task=task)

    @property
    def cases(self):
        return "cases"

    @cases.setter
    def cases(self, value):
        task = self._make_task(uri=self.cases, post_data=value)
        self._add_task(task=task)

    @property
    def cases_stats(self):
        return "audits"

    @cases_stats.setter
    def cases_stats(self, value):
        task = self._make_task(uri=self.cases_stats, post_data=value)
        self._add_task(task=task)

    @property
    def contracts(self):
        return "contracts"

    @contracts.setter
    def contracts(self, value):
        task = self._make_task(uri=self.contracts, post_data=value)
        self._add_task(task=task)

    @property
    def egrul(self):
        return "egrul"

    @egrul.setter
    def egrul(self, value):
        task = self._make_task(uri=self.egrul, post_data=value)
        self._add_task(task=task)

    @property
    def executory_processes(self):
        return "executory_processes"

    @executory_processes.setter
    def executory_processes(self, value):
        task = self._make_task(uri=self.executory_processes, post_data=value)
        self._add_task(task=task)

    @property
    def executory_processes_statistics(self):
        return "executory_processes_statistics"

    @executory_processes_statistics.setter
    def executory_processes_statistics(self, value):
        task = self._make_task(uri=self.executory_processes_statistics, post_data=value)
        self._add_task(task=task)

    @property
    def license(self):
        return "license"

    @license.setter
    def license(self, value):
        task = self._make_task(uri=self.license, post_data=value)
        self._add_task(task=task)

    @th_pool.in_lock
    def _get_tasks(self):
        tasks = self._tasks.copy()
        self._tasks.clear()
        return tasks

    def _add_task(self, task):
        self._tasks[self.task_id] = task
        self.task_id += 1

    @staticmethod
    def _make_task(uri, post_data):
        data = {'data': post_data}
        task = {'uri': uri, 'post_data': data}
        return task


class CasebookAPI(AbstractAPI):
    def login(self, email: str, passwd: str) -> bool:
        uri = 'Account/LogOn'
        post_data = {
            'UserName': email,  # 'nemotest@gmail.com',
            'Password': passwd,  # 'engrave',
            'RememberMe': True,
            'SystemName': 'sps'
        }

        response = self.api_request(uri=uri, post_data=post_data)
        return response.get('Success', response.get('Message'))

    def sides_search(self, name: str, page: int = 1, count: int = 30) -> dict:
        post_data = {'Filters': [{'Mode': 'Contains', 'Type': 'Name', 'Value': name}], 'Page': page, 'Count': count}
        uri = 'Search/Sides'

        return self.api_request(uri=uri, post_data=post_data)

    def get_accounting_stat(self, inn: str, year_from: int = 0, year_to: int = 0) -> dict:
        uri = 'Card/AccountingStat'
        # {"inn":"5433178674","yearFrom":2009,"yearTo":2009}
        post_data = {"inn": inn}

        if year_from:
            post_data['YearFrom'] = year_from
            post_data['YearTo'] = year_to if year_to else year_from

        return self.api_request(uri=uri, post_data=post_data)

    def get_egrul_link(self, **kwargs):

        slots = ['Inn', 'Name', 'ShortName', 'Address', 'Ogrn', 'Okpo', 'IsUnique',
                 'IsBranch', 'OrganizationId', 'OrganizationDictId', 'StorageId',
                 'IsNotPrecise', 'HeadFio', 'StatusId']

        uri = 'Card/Excerpt?'

        for slot in slots:
            uri += '{}={}&'.format(slot, kwargs.get(slot, ''))

        uri += 'UseCache=True'

        return ''.join((self.base_url, uri,))

    def get_buisnes_card(self, **kwargs):
        slots = ['Name', 'Address', 'Ogrn', 'IsUnique', 'IsPhysical', 'Okpo', 'OrganizationId']
        uri = 'Card/BusinessCard'

        post_data = {key: kwargs.get(key) for key in slots}

        return self.api_request(uri=uri, post_data=post_data)

    def get_license(self, inn: str, ogrn: str, page: int = 1, count: int = 30):
        uri = 'Card/Licenses'
        post_data = {"Page": page, "Count": count, "Inn": inn, "Ogrn": ogrn}

        return self.api_request(uri=uri, post_data=post_data)

    def get_state_contracts(self, inn: str, page: str = '1', perpage: str = '30', datefrom: str = '2016-01-01', dateto: str = '2016-12-31'):
        uri = 'Card/StateContracts'
        query_data = '?Page={}&Perpage={}&Supplier={}&Datefrom={}&Dateto={}'.format(page, perpage, inn, datefrom, dateto)

        return self.api_request(uri=''.join((uri, query_data)))

    def get_audit(self, inn: str, year: int = 2016, page: int = 1):
        uri = 'Card/GetAuditPlans'
        post_data = {"Inn": inn, "Year": year, "Page": page}

        return self.api_request(uri=uri, post_data=post_data)

    def get_audit_available_years(self):
        uri = 'Card/GetAuditAvailableYears'
        return self.api_request(uri=uri)

    def get_executory_processes_statistics(self, page: int = 1, count: int = 30, **kwargs):
        slots = ['Inn', 'Name', 'ShortName', 'Address', 'Ogrn', 'Okpo',
                 'IsUnique', 'IsBranch', 'OrganizationDictId', 'StorageId',
                 'StatusId', 'OrganizationName', 'OrganizationInn', 'ExecutoryObjectIds',
                 'ExecutoryProcessStatus', 'MinSum', 'MaxSum', 'DateFrom', 'DateTo',
                 'FieldOrder', 'TypeOrder']

        def_params = {'MinSum': 0, 'MaxSum': -1, 'DateFrom': None, 'DateTo': None, 'FieldOrder': 0,
                      'TypeOrder': 1, 'ExecutoryObjectIds': None, 'OrganizationInn': kwargs.get('Inn'),
                      'OrganizationName': kwargs.get('Name'), 'ExecutoryProcessStatus': -1}

        uri = 'Card/ExecutoryProcessesStatistics'
        post_data = {key: def_params[key] if def_params.get(key) else kwargs.get(key) for key in slots}
        post_data['Page'] = page
        post_data['Count'] = count
        return self.api_request(uri=uri, post_data=post_data)

    def get_executory_processes(self, page: int = 1, count: int = 30, **kwargs):
        slots = ['Inn', 'Name', 'ShortName', 'Address', 'Ogrn', 'Okpo',
                 'IsUnique', 'IsBranch', 'OrganizationDictId', 'StorageId',
                 'StatusId', 'OrganizationName', 'OrganizationInn', 'ExecutoryObjectIds',
                 'ExecutoryProcessStatus', 'MinSum', 'MaxSum', 'DateFrom', 'DateTo',
                 'FieldOrder', 'TypeOrder']

        def_params = {'MinSum': 0, 'MaxSum': -1, 'DateFrom': None, 'DateTo': None, 'FieldOrder': 0,
                      'TypeOrder': 1, 'ExecutoryObjectIds': None, 'OrganizationInn': kwargs.get('Inn'),
                      'OrganizationName': kwargs.get('Name'), 'ExecutoryProcessStatus': -1}

        uri = 'Card/ExecutoryProcesses'
        post_data = {key: def_params[key] if def_params.get(key) else kwargs.get(key) for key in slots}
        post_data['Page'] = page
        post_data['Count'] = count
        return self.api_request(uri=uri, post_data=post_data)

    def _case_info(self, uri: str = '', **kwargs):
        post_data = {
            'Accuracy': 0,
            'BankruptStages': None,
            'CaseCategoryId': None,
            'CaseResults': None,
            'CaseTypes': None,
            'CoSides': [],
            'ConsiderType': -1,
            'Count': 30,
            'CourtType': -1,
            'Courts': None,
            'DateFrom': "2009-08-21",
            'DateTo': None,
            'Delegate': "",
            'ExecutionObject': None,
            'ExecutionStatus': -1,
            'ExecutionsDateFrom': None,
            'ExecutionsDateTo': None,
            'FinalDocFrom': None,
            'FinalDocTo': None,
            'GeneralCaseTypes': None,
            'GeneralCourts': None,
            'Instances': None,
            'IsCasesTracking': True,
            'IsMessageFrTracking': True,
            'IsNeedAccuracy': 2,
            'IsNeedFnsChanges': True,
            'IsNeedMAClaims': True,
            'IsNeedNewCasesTracking': True,
            'IsNeedWritsTracking': False,
            'Judges': None,
            'MaxExecutionSum': -1,
            'MaxSum': -1,
            'MinExecutionSum': 0,
            'MinSum': 0,
            'MonitoredStatus': -1,
            'OrderBy': "incoming_date_ts desc, case_number desc",
            'Page': 1,
            'SessionFrom': None,
            'SessionTo': None,
            'Side': None,
            'SideTypes': None,
            'Sides': [
                {key: kwargs.get(key) for key in ['Address', 'Inn', 'IsBranch', 'IsOriginal', 'Name', 'Ogrn',
                                                  'Okpo', 'ShortName', 'StatusId', 'StatusName']},
                {key: kwargs.get(key) for key in ['Address', 'Inn', 'IsBranch', 'IsUnique', 'Name', 'Ogrn',
                                                  'Okpo', 'ShortName', 'StatusId', 'OrganizationDictId', 'StorageId']}
            ],
            'StateOrganizations': None,
            'StatusEx': None,
        }

        return self.api_request(uri=uri, post_data=post_data)

    def get_cases(self, **kwargs):
        return self._case_info(uri='Search/Cases', **kwargs)

    def get_org_stat_short(self, **kwargs):
        return self._case_info(uri='Card/OrgStatShort', **kwargs)

    def get_org_stat(self, **kwargs):
        return self._case_info(uri='Card/OrgStatBySideTypes', **kwargs)