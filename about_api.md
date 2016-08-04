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

Лицензии
Request URL:https://casebook.ru/api/Card/Licenses
Request Method:POST
RequestPayload: 
    {
        "page":1,
        "count":30,
        "inn":"3445102073",
        "ogrn":"1093460001095"
    }

page - Страница
count - Количетво результатов на страницу

Response:
[message] - (str) Сообщение сервера
[success] - (bool) Результат запроса
[result][page] - (int) Текущая страница
[result][pageSize] - (int) Количество элементов на странице 
[result][totalCount] - (int) Общее количество элементов
[result][pagesCount] - (int) Количество страниц
[result][items] - (list) Список лицензий

Госконтракты
Request URL:https://casebook.ru/api/Card/StateContracts?page=23&perpage=30&supplier=3445102073&datefrom=2016-01-01&dateto=2016-12-31
Request Method:GET
Query String Parameters:
    page:1
    perpage:30
    supplier:3445102073
    datefrom:2016-01-01
    dateto:2016-12-31

page - страница
perpage - количество элементов на страницу
supplier - инн организации

Response:
[success] - (bool) Результат выполнения запроса
[message] - (str) Сообщение сервера
[result][contracts] - (list) Список госконтрактов. Когда мы получили
    все контракты и больше получить не можем то этот список возвращается пустым
    
    
Проверки
Request URL:https://casebook.ru/api/Card/GetAuditPlans
Request Method:POST
Request Payload:
    {
        "inn":"3445102073",
        "year":2016,
        "page":1
    }
    
Response:
[success] - (bool) Результат выполнения запроса
[message] - (str) Сообщение сервера
[result][items] - (list) Список проверок

Года доступные для получения проверок
Request URL:https://casebook.ru/api/Card/GetAuditAvailableYears
Request Method:GET
Response:
    {
      "message": null,
      "serverDate": "2016-08-04T22:58:39.0005428+03:00",
      "result": [
        2015,
        2016
      ],
      "success": true,
      "timings": null
    }
    
Статистика исполнительных производств
Request URL:https://casebook.ru/api/Card/ExecutoryProcessesStatistics
Request Method:POST
Request Payload:
    {
    "inn":"3445102073",
    "name":"ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ \"ЛУКОЙЛ-ТЕПЛОТРАНСПОРТНАЯ КОМПАНИЯ\"",
    "shortName":"ООО \"ЛУКОЙЛ-ТТК\"",
    "address":"400066, ВОЛГОГРАДСКАЯ ОБЛАСТЬ, ГОРОД ВОЛГОГРАД, УЛИЦА ИМ СКОСЫРЕВА, Д.  7",
    "ogrn":"1093460001095",
    "okpo":"60915315",
    "isUnique":false,
    "isBranch":false,
    "organizationDictId":null,
    "storageId":4477117,
    "statusId":null,
    "organizationName":"ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ \"ЛУКОЙЛ-ТЕПЛОТРАНСПОРТНАЯ КОМПАНИЯ\"",
    "organizationInn":"3445102073",
    "executoryObjectIds":null,
    "executoryProcessStatus":-1,
    "minSum":0,
    "maxSum":-1,
    "dateFrom":null,
    "dateTo":null,
    "page":1,
    "count":30,
    "fieldOrder":0,
    "typeOrder":1
    }
Response:
{
  "message": null,
  "serverDate": "2016-08-04T23:12:30.0000262+03:00",
  "result": {
    "totalCount": 43,
    "totalSum": 1806462.72,
    "completedCount": 39,
    "completedSum": 1748265.34,
    "currentCount": 4,
    "currentSum": 58197.38
  },
  "success": true,
  "timings": null
}

Исполнительные производства
Request URL:https://casebook.ru/api/Card/ExecutoryProcesses
Request Method:POST
Request Payload:
    {
    "inn":"3445102073",
    "name":"ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ \"ЛУКОЙЛ-ТЕПЛОТРАНСПОРТНАЯ КОМПАНИЯ\"",
    "shortName":"ООО \"ЛУКОЙЛ-ТТК\"",
    "address":"400066, ВОЛГОГРАДСКАЯ ОБЛАСТЬ, ГОРОД ВОЛГОГРАД, УЛИЦА ИМ СКОСЫРЕВА, Д.  7",
    "ogrn":"1093460001095",
    "okpo":"60915315",
    "isUnique":false,
    "isBranch":false,
    "organizationDictId":null,
    "storageId":4477117,
    "statusId":null,
    "organizationName":"ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ \"ЛУКОЙЛ-ТЕПЛОТРАНСПОРТНАЯ КОМПАНИЯ\"",
    "organizationInn":"3445102073",
    "executoryObjectIds":null,
    "executoryProcessStatus":-1,
    "minSum":0,
    "maxSum":-1,
    "dateFrom":null,
    "dateTo":null,
    "page":1,
    "count":30,
    "fieldOrder":0,
    "typeOrder":1
    }
    
page - страница
count - результатов на страницу

Response:
    [success] - (bool) Результат выполнения запроса
    [message] - (str) Сообщение сервера
    [result][pagesCount] - (int) Количесво страниц
    [result][executoryProcesses] - (list) Список производств
