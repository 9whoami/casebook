# -*- coding: utf-8 -*-

from grab import Grab

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

        super().__init__(timeout=60)

    def api_request(self, url:str='', origin:'json=1 or body=0'=1, **kwargs:'post data dict') -> dict:
        try:
            url = self.base_url + url
            self.go(url, post=kwargs)
            response = self.response.json if origin else self.response.body
        except Exception as e:
            response = dict(error=e)

        return response


class CasebookAPI(ApiMethods):
    def login(self, email: str, passwd: str) -> bool:
        url = 'Account/LogOn'
        post_data = {
            'UserName': email,  # 'nemotest@gmail.com',
            'Password': passwd, # 'engrave',
            'RememberMe': True,
            'SystemName': 'sps'
        }

        response = self.api_request(url=url, **post_data)
        return bool(response.get('Success'))

    def sides_search(self, name: str, page: int=1, count: int=30) -> dict:
        post_data = {"filters": [{'mode': "Contains", "type": "Name", "value": name}], "page": page, "count": count}
        url = 'Search/Sides'

        return self.api_request(url=url, **post_data)

    def get_accounting_stat(self, inn: str, year_from: int=0, year_to: int=0) -> dict:
        url = 'Card/AccountingStat'
        # {"inn":"5433178674","yearFrom":2009,"yearTo":2009}
        post_data = {"inn": inn}

        if year_from:
            post_data['yearFrom'] = year_from
            post_data['yearTo'] = year_to if year_to else year_from

        return self.api_request(url=url, **post_data)

    def get_egrul_link(self, **kwargs):

        slots = ['Inn', 'Name', 'ShortName', 'Address', 'Ogrn', 'Okpo', 'IsUnique',
                 'IsBranch', 'OrganizationId', 'OrganizationDictId', 'StorageId',
                 'IsNotPrecise', 'HeadFio', 'StatusId']

        url = 'Card/Excerpt?'

        for slot in slots:
            url += '{}={}&'.format(slot, kwargs[slot] if kwargs.get(slot) else '')

        url += 'useCache=True'

        return self.base_url + url

    def get_buisnes_card(self, **kwargs):

        slots = ['Name', 'Address', 'Ogrn', 'IsUnique', 'IsPhysical', 'Okpo', 'OrganizationId']
        url = 'Card/BusinessCard'

        post_data = {key: kwargs.get(key) for key in slots}

        return self.api_request(url=url, **post_data)
