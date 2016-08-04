Вход
Request Url: https://casebook.ru/api/Account/LogOn
Request method: POST
Request Pyaload:
    {
        'UserName': email_adress,
        'Password': password,
        'RememberMe': True,
        'SystemName': 'sps'
    }

Response:
    {
        'Message': 'Активируйте аккаунт по ссылке в письме.', 
        'Timings': None, 
        'Result': None, 
        'Success': False, 
        'ServerDate': '2016-08-05T01:02:17.0007294+03:00'
    }
    
[Message] - (str) Сообщение сервера, например сообщение об ошибке как в данном примере
[Timings] - (unknown) Время ответа сервера
[Result] - (unknown) ?
[Success] - (bool) Результат. В данном случае входи не удался.
[ServerDate] - (unknown) Время сервера

Поиск компаний
Request Url: https://casebook.ru/api/Search/Sides
Request method: POST
Request Pyaload:
    {
        "filters": [
            {
                'mode': "Contains", 
                "type": "Name", 
                "value": 'лукоил'
            }
        ], 
        "page": 1, 
        "count": 30
    }

filtres - фильтры поиска.
    mode - ?
    type - Тип поиска. Возможен поиск по хэшу.
    value - поисковая строка
page - страница
count - количесво элементов на странице

Response:
В ответ получим json со списком компаний. Основные ключи опписаны ниже.
[Result][Items] - (list) Список компаний
[Success] - (bool) Результат запроса
[Message] - (str) Сообщение сервера
[Result][Page] - (int) Текущая страница
[Result][PageSize] - (int) Количество элементов
[Result][PageCount] - (int) Количество страниц
[Result][TotalCount] - (int) Общее количесво найденых компаний

Бухгалтерская отчетность
Request Url: https://casebook.ru/api/Card/AccountingStat
Request method: POST
Request Pyaload:
    {
        "inn":"5433178674",
        "yearFrom":2009,
        "yearTo":2009
    }

    Параметры yearFrom и yearTo необязательны

Response:
[Message] - (str) Сообщение сервера
[Success] - (bool) Результат запроса
[Result][AvailableDateTimeRanges] - (dict) Список доступных временных интервалов
[Result][GroupReports] - (list) ?
[Result][NotCompareReports] - (list) ?

Получение ссылки на ЕГРЮЛ
Request Url: https://casebook.ru/api/Card/Excerpt?Inn=5433178674&Name=%D0%9E%D0%91%D0%A9%D0%95%D0%A1%D0%A2%D0%92%D0%9E%20%D0%A1%20%D0%9E%D0%93%D0%A0%D0%90%D0%9D%D0%98%D0%A7%D0%95%D0%9D%D0%9D%D0%9E%D0%99%20%D0%9E%D0%A2%D0%92%D0%95%D0%A2%D0%A1%D0%A2%D0%92%D0%95%D0%9D%D0%9D%D0%9E%D0%A1%D0%A2%D0%AC%D0%AE%20%D0%9F%D0%A0%D0%9E%D0%A4%D0%98%D0%9B%D0%AC%D0%9D%D0%90%D0%AF%20%D0%98%D0%9D%D0%9D%D0%9E%D0%92%D0%90%D0%A6%D0%98%D0%9E%D0%9D%D0%9D%D0%90%D0%AF%20%D0%9A%D0%9E%D0%9C%D0%9F%D0%90%D0%9D%D0%98%D0%AF%20%22%D0%A5%D0%90%D0%A0%D0%A2%D0%98%D0%AF%20%D0%91%D0%95%D0%97%D0%9E%D0%9F%D0%90%D0%A1%D0%9D%D0%9E%D0%A1%D0%A2%D0%98%22&ShortName=%D0%9E%D0%9E%D0%9E%20%D0%9F%D0%98%D0%9A%20%22%D0%A5%D0%90%D0%A0%D0%A2%D0%98%D0%AF%20%D0%91%D0%95%D0%97%D0%9E%D0%9F%D0%90%D0%A1%D0%9D%D0%9E%D0%A1%D0%A2%D0%98%22&Address=630559,%20%D0%9D%D0%9E%D0%92%D0%9E%D0%A1%D0%98%D0%91%D0%98%D0%A0%D0%A1%D0%9A%D0%90%D0%AF%20%D0%9E%D0%91%D0%9B%D0%90%D0%A1%D0%A2%D0%AC,%20%D0%A0%D0%90%D0%91%D0%9E%D0%A7%D0%98%D0%99%20%D0%9F%D0%9E%D0%A1%D0%95%D0%9B%D0%9E%D0%9A%20%D0%9A%D0%9E%D0%9B%D0%AC%D0%A6%D0%9E%D0%92%D0%9E,%20%D0%A3%D0%9B%D0%98%D0%A6%D0%90%20%D0%A2%D0%95%D0%A5%D0%9D%D0%9E%D0%9F%D0%90%D0%A0%D0%9A%D0%9E%D0%92%D0%90%D0%AF,%20%D0%94.%201&Ogrn=1095475003821&Okpo=62883530&IsUnique=&IsBranch=&OrganizationId=&OrganizationDictId=&StorageId=6923889&IsNotPrecise=&HeadFio=%D0%9B%D0%AC%D0%92%D0%A3%D0%A2%D0%98%D0%9D%20%D0%9F%D0%90%D0%92%D0%95%D0%9B%20%D0%AD%D0%94%D0%A3%D0%90%D0%A0%D0%94%D0%9E%D0%92%D0%98%D0%A7&StatusId=&useCache=True
Request method: GET
Query String Parameters:
    Inn=5433178674
    Name=ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ ПРОФИЛЬНАЯ ИННОВАЦИОННАЯ КОМПАНИЯ "ХАРТИЯ БЕЗОПАСНОСТИ"
    ShortName=ООО ПИК "ХАРТИЯ БЕЗОПАСНОСТИ"
    Address=630559, НОВОСИБИРСКАЯ ОБЛАСТЬ, РАБОЧИЙ ПОСЕЛОК КОЛЬЦОВО, УЛИЦА ТЕХНОПАРКОВАЯ, Д. 1 
    Ogrn=1095475003821
    Okpo=62883530 
    IsBranch=
    OrganizationId=
    OrganizationDictId=
    StorageId=6923889
    IsNotPrecise=
    HeadFio=ЛЬВУТИН ПАВЕЛ ЭДУАРДОВИЧ
    StatusId= 
    useCache=True
    
useCache - всегда True. Все остальное берется из инфы о компании. 
Все ключи обязательны, даже если они пустые

Общая информация о компании
Request Url: https://casebook.ru/api/Card/BusinessCard
Request method: POST
Request Pyaload:
    {
        'IsUnique': None, 
        'IsPhysical': False, 
        'Okpo': '62883530', 
        'OrganizationId': 0, 
        'Name': 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ ПРОФИЛЬНАЯ ИННОВАЦИОННАЯ КОМПАНИЯ "ХАРТИЯ БЕЗОПАСНОСТИ"', 
        'Ogrn': '1095475003821', 
        'Address': '630559, НОВОСИБИРСКАЯ ОБЛАСТЬ, РАБОЧИЙ ПОСЕЛОК КОЛЬЦОВО, УЛИЦА ТЕХНОПАРКОВАЯ, Д. 1'
    }
    
Response:
[Success] - (bool) Результат запроса
[Message] - (str) Сообщение сервера
[Result] - (dict) Общая информация о компании

