# -*- coding: utf-8 -*-

from grab import Grab
import os
import simplejson

try:
    from logger import Logger
except ImportError:
    pass

from config import Conf

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

class ApiMethods(Grab):
    BODY = 0
    JSON = 1

    online_only = None
    acc_status = None

    def __init__(self, loggining=False):
        if loggining:
            try:
                self.logger = Logger()
            except NameError:
                raise SystemExit('В данный момент логгер не поддерживается!')

        config = Conf(section='api')
        self.base_url = config.main_url

        super().__init__(timeout=60, connect_timeout=15, debug=True)
        self.setup(log_dir='/'.join((os.getcwd(), 'grab_logs')), headers={"Content-type": "application/json", "Accept": "application/json"})

    def api_request(self, uri: str = '', **kwargs: dict) -> dict:
        try:
            uri = ''.join((self.base_url, uri,))
            post_data = simplejson.dumps(kwargs)
            self.request(url=uri, post=post_data)
            response = self.response.json
        except Exception as e:
            response = dict(Message=e)

        return response


class CasebookAPI(ApiMethods):
    def login(self, email: str, passwd: str) -> bool:
        uri = 'Account/LogOn'
        post_data = {
            'UserName': email,  # 'nemotest@gmail.com',
            'Password': passwd,  # 'engrave',
            'RememberMe': True,
            'SystemName': 'sps'
        }

        response = self.api_request(uri=uri, **post_data)
        return response.get('Success') if response.get('Success') else response.get('Message')

    def sides_search(self, name: str, page: int = 1, count: int = 30) -> dict:
        post_data = {'Filters': [{'Mode': 'Contains', 'Type': 'Name', 'Value': name}], 'Page': page, 'Count': count}
        uri = 'Search/Sides'

        return self.api_request(uri=uri, **post_data)

    def get_accounting_stat(self, inn: str, year_from: int = 0, year_to: int = 0) -> dict:
        uri = 'Card/AccountingStat'
        # {"inn":"5433178674","yearFrom":2009,"yearTo":2009}
        post_data = {"inn": inn}

        if year_from:
            post_data['YearFrom'] = year_from
            post_data['YearTo'] = year_to if year_to else year_from

        return self.api_request(uri=uri, **post_data)

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

        return self.api_request(uri=uri, **post_data)

    def get_license(self, inn: str, ogrn: str, page: int = 1, count: int = 30):
        uri = 'Card/Licenses'
        post_data = {"Page": page, "Count": count, "Inn": inn, "Ogrn": ogrn}

        return self.api_request(uri=uri, **post_data)

    def get_state_contracts(self, inn: str, page: str = '1', perpage: str = '30', datefrom: str = '2016-01-01', dateto: str = '2016-12-31'):
        uri = 'Card/StateContracts'
        query_data = '?Page={}&Perpage={}&Supplier={}&Datefrom={}&Dateto={}'.format(page, perpage, inn, datefrom, dateto)

        return self.api_request(uri=''.join((uri, query_data)))

    def get_audit(self, inn: str, year: int = 2016, page: int = 1):
        uri = 'https://casebook.ru/api/Card/GetAuditPlans'
        post_data = {"Inn": inn, "Year": year, "Page": page}

        return self.api_request(uri=uri, **post_data)

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
        return self.api_request(uri=uri, **post_data)

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
        return self.api_request(uri=uri, **post_data)

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

        return self.api_request(uri=uri, **post_data)

    def get_cases(self, **kwargs):
        return self._case_info(uri='Search/Cases', **kwargs)

    def get_org_stat_short(self, **kwargs):
        return self._case_info(uri='Card/OrgStatShort', **kwargs)

    def get_org_stat(self, **kwargs):
        return self._case_info(url='Card/OrgStatBySideTypes', **kwargs)