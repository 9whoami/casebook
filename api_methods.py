# -*- coding: utf-8 -*-

import os
import simplejson
import urllib.request
import urllib.parse
from grab import Grab
from config import Conf
from threadpool import ThreadPool
try:
    from logger import Logger
except ImportError:
    pass

__author__ = 'whoami'
__version__ = '1.3.3'
__date__ = '19.02.16 23:14'
__description__ = """
Набор методов для работы с апи
"""

import logging
logger = logging.getLogger('grab')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


class AbstractAPI(Grab):
    def __init__(self, loggining=False, section='api'):
        if loggining:
            try:
                self.logger = Logger()
            except NameError:
                raise SystemExit('В данный момент логгер не поддерживается!')

        config = Conf(section=section)
        self.base_url = config.main_url

        super().__init__(timeout=120, connect_timeout=15, debug=True)
        self.setup(log_dir='/'.join((os.getcwd(), 'grab_logs')), headers={"Content-type": "application/json", "Accept": "application/json"})

    def api_request(self, uri: str = '', post_data: dict = None) -> dict:
        try:
            uri = ''.join((self.base_url, uri,))
            if post_data:
                post_data = simplejson.dumps(post_data, ensure_ascii=False)

            self.request(url=uri, post=post_data)
            response = self.response.json

            if response.get('error'):
                response['Message'] = response['error']
                del response['error']

        except Exception as e:
            response = dict(Message=str(e))

        return response

    def main_api_request(self, uri: str, post_data):
        data = urllib.parse.urlencode(post_data)
        data = data.encode('ascii')
        uri = ''.join((self.base_url, uri,))

        try:
            with urllib.request.urlopen(uri, data) as f:
                response = simplejson.loads(f.read().decode('utf-8'))
        except Exception as e:
            response = {'Message': str(e)}

        return response


th_pool = ThreadPool(max_threads=10)


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
    task_id = 0

    @th_pool.thread
    def run_tasks(self, company_id):
        if company_id == -1:
            raise ValueError('Account id not found!')

        tasks = self._get_tasks()

        for task_id in tasks:
            # prepare post data
            tasks[task_id]['post_data']['id'] = company_id

            # sending post data
            response = self.main_api_request(**tasks[task_id])
            print(response)

        return None

    def waiting_for(self):
        th_pool.loop()

    def add_new_accouns(self, value):
        task = self._make_task(uri=self.biusnes_cards, post_data=value)

        response = self.main_api_request(**task)
        if response.get('id'):
            return response['id']
        else:
            print(response['Message'])
            return -1

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
        return response.get('Success') if response.get('Success') else response.get('Message')

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
            uri += '{}={}&'.format(slot, kwargs[slot] if kwargs.get(slot) else '')

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