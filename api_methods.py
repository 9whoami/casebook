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

    def mob_search(self, name: str) -> dict:
        url = '/Search/Sides?name={}'.format(name)
        return self.api_request(url=url)
    
    def web_search(self, name: str) -> dict:
        post_data = {"filters": [{'mode': "Contains", "type": "Name", "value": name}], "page": 2, "count": 30}
        url = 'Search/Sides'

        return self.api_request(url=url, **post_data)

    def accounting_stat(self, inn: str) -> dict:
        url = 'Card/AccountingStat'
        post_data = {"inn": inn}

        return self.api_request(url=url, **post_data)