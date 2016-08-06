# Вход
#### Request Url: 
    https://casebook.ru/api/Account/LogOn
#### Request method: 
    POST
#### Request Pyaload: 

<pre><code>

    {
        'UserName': email_adress,
        'Password': password,
        'RememberMe': True,
        'SystemName': 'sps'
    }
    
</pre></code>

#### Response:

<pre><code>
    {
        'Message': 'Активируйте аккаунт по ссылке в письме.', 
        'Timings': None, 
        'Result': None, 
        'Success': False, 
        'ServerDate': '2016-08-05T01:02:17.0007294+03:00'
    }
</pre></code>

* Message - *(str)* Сообщение сервера, например сообщение об ошибке как в данном примере
* Timings - *(unknown)* Время ответа сервера
* Result - *(unknown)* ?
* Success - *(bool)* Результат. В данном случае входи не удался.
* ServerDate - *(unknown)* Время сервера

# Поиск компаний
#### Request Url: 
    https://casebook.ru/api/Search/Sides
#### Request method: 
    POST
#### Request Pyaload:

```
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
```

+ filtres - фильтры поиска.
    * mode - ?
    * type - Тип поиска. Возможен поиск по хэшу.
    * value - поисковая строка
- page - страница
* count - количесво элементов на странице

#### Response:

> В ответ получим json со списком компаний. Основные ключи опписаны ниже.

* Result.Items - *(list)* Список компаний
* Success - *(bool)* Результат запроса
* Message - *(str)* Сообщение сервера
+ Result - *(dict)* Резултат поиска
    * Page - *(int)* Текущая страница
    * PageSize - *(int)* Количество элементов
    * PageCount - *(int)* Количество страниц
    * TotalCount - *(int)* Общее количесво найденых компаний

# Бухгалтерская отчетность
#### Request Url: 
    https://casebook.ru/api/Card/AccountingStat
#### Request method: 
    POST
#### Request Pyaload: 

<pre><code>
    {
        "inn":"5433178674",
        "yearFrom":2009,
        "yearTo":2009
    }
</pre></code>

> Параметры yearFrom и yearTo необязательны

#### Response:

* Message - *(str)* Сообщение сервера
* Success - *(bool)* Результат запроса
+ Result:
    * AvailableDateTimeRanges - *(dict)* Список доступных временных интервалов
    * GroupReports - *(list)* ?
    * NotCompareReports - *(list)* ?

# Формирование ссылки на ЕГРЮЛ
#### Request Url: 
    https://casebook.ru/api/Card/Excerpt?Inn=5433178674&Name=%D0%9E%D0%91%D0%A9%D0%95%D0%A1%D0%A2%D0%92%D0%9E%20%D0%A1%20%D0%9E%D0%93%D0%A0%D0%90%D0%9D%D0%98%D0%A7%D0%95%D0%9D%D0%9D%D0%9E%D0%99%20%D0%9E%D0%A2%D0%92%D0%95%D0%A2%D0%A1%D0%A2%D0%92%D0%95%D0%9D%D0%9D%D0%9E%D0%A1%D0%A2%D0%AC%D0%AE%20%D0%9F%D0%A0%D0%9E%D0%A4%D0%98%D0%9B%D0%AC%D0%9D%D0%90%D0%AF%20%D0%98%D0%9D%D0%9D%D0%9E%D0%92%D0%90%D0%A6%D0%98%D0%9E%D0%9D%D0%9D%D0%90%D0%AF%20%D0%9A%D0%9E%D0%9C%D0%9F%D0%90%D0%9D%D0%98%D0%AF%20%22%D0%A5%D0%90%D0%A0%D0%A2%D0%98%D0%AF%20%D0%91%D0%95%D0%97%D0%9E%D0%9F%D0%90%D0%A1%D0%9D%D0%9E%D0%A1%D0%A2%D0%98%22&ShortName=%D0%9E%D0%9E%D0%9E%20%D0%9F%D0%98%D0%9A%20%22%D0%A5%D0%90%D0%A0%D0%A2%D0%98%D0%AF%20%D0%91%D0%95%D0%97%D0%9E%D0%9F%D0%90%D0%A1%D0%9D%D0%9E%D0%A1%D0%A2%D0%98%22&Address=630559,%20%D0%9D%D0%9E%D0%92%D0%9E%D0%A1%D0%98%D0%91%D0%98%D0%A0%D0%A1%D0%9A%D0%90%D0%AF%20%D0%9E%D0%91%D0%9B%D0%90%D0%A1%D0%A2%D0%AC,%20%D0%A0%D0%90%D0%91%D0%9E%D0%A7%D0%98%D0%99%20%D0%9F%D0%9E%D0%A1%D0%95%D0%9B%D0%9E%D0%9A%20%D0%9A%D0%9E%D0%9B%D0%AC%D0%A6%D0%9E%D0%92%D0%9E,%20%D0%A3%D0%9B%D0%98%D0%A6%D0%90%20%D0%A2%D0%95%D0%A5%D0%9D%D0%9E%D0%9F%D0%90%D0%A0%D0%9A%D0%9E%D0%92%D0%90%D0%AF,%20%D0%94.%201&Ogrn=1095475003821&Okpo=62883530&IsUnique=&IsBranch=&OrganizationId=&OrganizationDictId=&StorageId=6923889&IsNotPrecise=&HeadFio=%D0%9B%D0%AC%D0%92%D0%A3%D0%A2%D0%98%D0%9D%20%D0%9F%D0%90%D0%92%D0%95%D0%9B%20%D0%AD%D0%94%D0%A3%D0%90%D0%A0%D0%94%D0%9E%D0%92%D0%98%D0%A7&StatusId=&useCache=True
#### Request method: 
    GET
#### Query String Parameters:

<pre><code>
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
</pre></code>

* useCache - всегда True. Все остальное берется из инфы о компании. 

> Все ключи обязательны, даже если они пустые

# Общая информация о компании
#### Request Url: 
    https://casebook.ru/api/Card/BusinessCard
#### Request method: 
    POST
#### Request Pyaload: 

<pre><code>
    {
        'IsUnique': None, 
        'IsPhysical': False, 
        'Okpo': '62883530', 
        'OrganizationId': 0, 
        'Name': 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ ПРОФИЛЬНАЯ ИННОВАЦИОННАЯ КОМПАНИЯ "ХАРТИЯ БЕЗОПАСНОСТИ"', 
        'Ogrn': '1095475003821', 
        'Address': '630559, НОВОСИБИРСКАЯ ОБЛАСТЬ, РАБОЧИЙ ПОСЕЛОК КОЛЬЦОВО, УЛИЦА ТЕХНОПАРКОВАЯ, Д. 1'
    }
</pre></code>

#### Response:
* Success - *(bool)* Результат запроса
* Message - *(str)* Сообщение сервера
* Result - *(dict)* Общая информация о компании

# Лицензии
#### Request URL:
    https://casebook.ru/api/Card/Licenses
#### Request Method:
    POST
#### RequestPayload: 
<pre><code>
    {
        "page":1,
        "count":30,
        "inn":"3445102073",
        "ogrn":"1093460001095"
    }
</pre></code>

> page - Страница
> count - Количетво результатов на страницу

#### Response:
* message - *(str)* Сообщение сервера
* success - *(bool)* Результат запроса
+ result:
    * page - *(int)* Текущая страница
    * pageSize -     *(int)    * Количество элементов на странице 
    * totalCount -     *(int)    * Общее количество элементов
    * pagesCount -     *(int)    * Количество страниц
    * items -     *(list)    * Список лицензий

# Госконтракты
#### Request URL:
    https://casebook.ru/api/Card/StateContracts?page=23&perpage=30&supplier=3445102073&datefrom=2016-01-01&dateto=2016-12-31
#### Request Method:
    GET
#### Query String Parameters:

<pre><code>
    page=1
    perpage=30
    supplier=3445102073
    datefrom=2016-01-01
    dateto=2016-12-31
</pre></code>

* page - страница
* perpage - количество элементов на страницу
* supplier - инн организации

#### Response:

* success - *(bool)* Результат выполнения запроса
* message - *(str)* Сообщение сервера
+ result:
    *contracts - *(list)* Список госконтрактов. Когда мы получили </br> все контракты и больше получить не можем то этот список возвращается пустым

# Проверки
#### Request URL:
    https://casebook.ru/api/Card/GetAuditPlans
#### Request Method:
    POST
#### Request Payload:

<pre><code>
    {
        "inn":"3445102073",
        "year":2016,
        "page":1
    }
</pre></code>
    
#### Response:
* success - *(bool)* Результат выполнения запроса
* message - *(str)* Сообщение сервера
+ result:
    * items - *(list)* Список проверок

# Года доступные для получения проверок
#### Request URL:
    https://casebook.ru/api/Card/GetAuditAvailableYears
#### Request Method:
    GET
#### Response:

<pre><code>
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
</pre></code>
    
# Статистика исполнительных производств
#### Request URL:
    https://casebook.ru/api/Card/ExecutoryProcessesStatistics
#### Request Method:
    POST
#### Request Payload:

<pre><code>
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
</pre></code>
    
#### Response:

<pre><code>
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
</pre></code>

# Исполнительные производства
#### Request URL:
    https://casebook.ru/api/Card/ExecutoryProcesses
#### Request Method:
    POST
#### Request Payload:

<pre><code>
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
</pre></code>
    
* page - страница
* count - результатов на страницу

#### Response:

* success - *(bool)* Результат выполнения запроса
* message - *(str)* Сообщение сервера
+ result:
    * pagesCount - *(int)* Количесво страниц
    * executoryProcesses - *(list)* Список производств
    
    
#Список арбитражных дел
#### Request URL:
    https://casebook.ru/api/Search/Cases
#### Request Method:
    POST
#### Request Payload:

<pre><code>
{
    'accuracy': 0,
    'bankruptStages': None,
    'caseCategoryId': None,
    'caseResults': None,
    'caseTypes': None,
    'coSides': [],
    'considerType': -1,
    'count': 30,
    'courtType': -1,
    'courts': None,
    'dateFrom': "2009-03-05",
    'dateTo': None,
    'delegate': "",
    'executionObject': None,
    'executionStatus': -1,
    'executionsDateFrom': None,
    'executionsDateTo': None,
    'finalDocFrom': None,
    'finalDocTo': None,
    'generalCaseTypes': None,
    'generalCourts': None,
    'instances': None,
    'isCasesTracking': True,
    'isMessageFrTracking': True,
    'isNeedAccuracy': 2,
    'isNeedFnsChanges': True,
    'isNeedMAClaims': True,
    'isNeedNewCasesTracking': True,
    'isNeedWritsTracking': False,
    'judges': None,
    'maxExecutionSum': -1,
    'maxSum': -1,
    'minExecutionSum': 0,
    'minSum': 0,
    'monitoredStatus': -1,
    'orderBy': "incoming_date_ts desc, case_number desc",
    'page': 1,
    'sessionFrom': None,
    'sessionTo': None,
    'side': None,
    'sideTypes': None,
    'sides': [
        {
            'address': "400066, ВОЛГОГРАДСКАЯ обл, ВОЛГОГРАД г, ИМ СКОСЫРЕВА ул, д.7",
            'inn': "3445102073",
            'isBranch': False,
            'isOriginal': True,
            'name': "ООО ЛУКОЙЛ - Теплотранспортная компания",
            'ogrn': "1093460001095",
            'okpo': "",
            'shortName': "ООО ЛУКОЙЛ - Теплотранспортная компания",
            'statusId': None,
            'statusName': None,
        },
        {
            'address': "400066, ВОЛГОГРАДСКАЯ ОБЛАСТЬ, ГОРОД ВОЛГОГРАД, УЛИЦА ИМ СКОСЫРЕВА, Д.  7",
            'inn': "3445102073",
            'isBranch': False,
            'isUnique': False,
            'name': 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "ЛУКОЙЛ - ТЕПЛОТРАНСПОРТНАЯ КОМПАНИЯ"',
            'ogrn': "1093460001095",
            'okpo': "60915315",
            'organizationDictId': None,
            'shortName': "ООО ЛУКОЙЛ - ТТК",
            'statusId': None,
            'storageId': 4477117,
        }
    ],
    'stateOrganizations': None,
    'statusEx': None,
}
</pre></code>

* dateFrom - дата регистрации компании (RegistrationDate)
* dateTo - дата ликвидации ?

#### Response:

<pre><code>
{
  "message": "",
  "serverDate": "2016-08-06T12:22:30.0000153+03:00",
  "result": {
    "maxSum": -1.0,
    "foundSideIdByCaseId": {
      "1cbcf7e3-601d-4cb1-8ade-bd47df34e62d": 0
    },
    "page": 1,
    "pageSize": 30,
    "totalCount": 1,
    "pagesCount": 1,
    "items": [
      {
        "caseId": "1cbcf7e3-601d-4cb1-8ade-bd47df34e62d",
        "foundInstanceId": "00000000-0000-0000-0000-000000000000",
        "caseNumber": "А40-250397/2015",
        "startDate": "2015-12-23T00:00:00",
        "finishDate": "2016-02-20T00:00:00",
        "judgeId": "00000000-0000-0000-0000-000000000000",
        "judge": null,
        "court": null,
        "instances": [
          {
            "court": "АС города Москвы",
            "judge": "Завершено в",
            "courtTag": "MSK",
            "instanceLevel": 1,
            "finishState": 2,
            "finishDate": "2016-02-20T00:00:00",
            "incomingDate": "2015-12-23T00:00:00",
            "judgeId": "00000000-0000-0000-0000-000000000000",
            "judges": [
              {
                "id": "beb7f6ea-4caa-447c-a275-572bbe223aa6",
                "role": 0
              }
            ]
          }
        ],
        "courts": null,
        "sides": [
          {
            "sideType": 0,
            "type": 0,
            "fakeId": 7668492,
            "sideId": null,
            "typeName": null,
            "birthPlace": null,
            "birthDate": null,
            "snils": null,
            "statusName": null,
            "statusId": null,
            "organizationId": 0,
            "cardType": 0,
            "isBranch": false,
            "isUnique": null,
            "isNotPrecise": false,
            "region": null,
            "orgForm": null,
            "headFio": null,
            "storageId": null,
            "isPhysical": false,
            "isMonitored": false,
            "inFolders": null,
            "organizationDictId": null,
            "isFavorite": false,
            "comment": null,
            "registrationDate": "0001-01-01T00:00:00",
            "shortName": "ООО \"ГЛОБУС\"",
            "name": "ООО \"ГЛОБУС\"",
            "inn": "7733850530",
            "ogrn": "1137746698616",
            "okpo": null,
            "hidePersonalData": null,
            "address": "125363, Москва г, Фабрициуса ул, 33А, стр. 17"
          },
          {
            "sideType": 0,
            "type": 0,
            "fakeId": 7668495,
            "sideId": null,
            "typeName": null,
            "birthPlace": null,
            "birthDate": null,
            "snils": null,
            "statusName": null,
            "statusId": null,
            "organizationId": 0,
            "cardType": 0,
            "isBranch": false,
            "isUnique": null,
            "isNotPrecise": false,
            "region": null,
            "orgForm": null,
            "headFio": null,
            "storageId": null,
            "isPhysical": false,
            "isMonitored": false,
            "inFolders": null,
            "organizationDictId": null,
            "isFavorite": false,
            "comment": null,
            "registrationDate": "0001-01-01T00:00:00",
            "shortName": "ООО Глобус",
            "name": "ООО Глобус",
            "inn": "",
            "ogrn": "",
            "okpo": null,
            "hidePersonalData": null,
            "address": "142101, Московская обл, Подольск г ул Плещеевская д 56 а/я 16"
          },
          {
            "sideType": 1,
            "type": 1,
            "fakeId": 7668493,
            "sideId": null,
            "typeName": null,
            "birthPlace": null,
            "birthDate": null,
            "snils": null,
            "statusName": null,
            "statusId": null,
            "organizationId": 0,
            "cardType": 0,
            "isBranch": false,
            "isUnique": null,
            "isNotPrecise": false,
            "region": null,
            "orgForm": null,
            "headFio": null,
            "storageId": null,
            "isPhysical": false,
            "isMonitored": false,
            "inFolders": null,
            "organizationDictId": null,
            "isFavorite": false,
            "comment": null,
            "registrationDate": "0001-01-01T00:00:00",
            "shortName": "ООО \"ЛУКОИЛ-БРЕНД\"",
            "name": "ООО \"ЛУКОИЛ-БРЕНД\"",
            "inn": "5009098617",
            "ogrn": "1155009001806",
            "okpo": null,
            "hidePersonalData": null,
            "address": "142063, Московская обл, Домодедово г, Поздново, стр. 20"
          }
        ],
        "lastEvents": [
          {
            "date": "2016-03-25T00:00:00",
            "description": "Возврат госпошлины",
            "contentTypes": null,
            "decisionType": null,
            "documentId": null,
            "court": "АС города Москвы",
            "instanceLevel": 1,
            "judge": null,
            "judgeId": "00000000-0000-0000-0000-000000000000",
            "declarer": null,
            "declarerInfo": null,
            "instanceNumber": "А40-250397/2015",
            "instanceId": "00000000-0000-0000-0000-000000000000",
            "needJudges": false,
            "typeName": null,
            "documentFileName": null,
            "appealedDocuments": null
          }
        ],
        "nextEvent": null,
        "bankruptStage": null,
        "status": "Рассмотрение дела завершено",
        "caseTypeMCode": "Г",
        "caseCategory": "О неисполнении или ненадлежащем исполнении обязательств по договорам поставки",
        "caseCategoryId": "f205f4d1-bbb4-4766-835d-300e262fe38a",
        "caseType": "",
        "claimSum": 1326931.0,
        "recoverySum": null,
        "comment": "ООО \"ГЛОБУС\" против ООО \"ЛУКОИЛ-БРЕНД\". О неисполнении или ненадлежащем исполнении обязательств по договорам поставки. ",
        "isMonitored": false,
        "inFolders": [],
        "isFavorite": false,
        "updatesCount": 0,
        "isGJ": false,
        "isSimpleJustice": false,
        "isFlBankruptcy": false,
        "responsibleUsers": null,
        "lastComment": null,
        "caseResult": 0,
        "caseDuration": 60
      }
    ]
  },
  "success": true,
  "timings": [
    "GetCasesIdsFormSearcher 00:00:00.2020000",
    "ElasticSearch 00:00:00.2020000",
    "Elastic.Took 00:00:00.1650000",
    "GetCasesList.monitoredCases 00:00:00.0500000",
    "GetCasesList.nonViewedCases 00:00:00.0130000",
    "GetUserFavoriteCasesIds 00:00:00.0090000",
    "GetCasesList.favoriteCases 00:00:00.0090000",
    "GetCasesList.comments 00:00:00.0040000",
    "GetCasesList.bankruptStages 00:00:00",
    "jsonCamelCase 00:00:00",
    "GetCasesList.Sql 00:00:00",
    "GetCasesList.SortAndMerge 00:00:00"
  ]
}
</pre></code>

# Краткая статистика арбитражных дел
#### Request URL: 
    https://casebook.ru/api/Card/OrgStatShort
#### Request Method:
    POST
#### Request Payload:

<pre><code>
{
    "statusEx":null,
    "sideTypes":null,
    "monitoredStatus":-1,
    "considerType":-1,
    "courtType":-1,
    "caseResults":null,
    "caseTypes":null,
    "caseCategoryId":null,
    "bankruptStages":null,
    "courts":null,
    "instances":null,
    "judges":null,
    "delegate":"",
    "stateOrganizations":null,
    "isNeedFnsChanges":true,
    "isNeedMAClaims":true,
    "isNeedAccuracy":2,
    "isNeedWritsTracking":false,
    "isNeedNewCasesTracking":true,
    "isMessageFrTracking":true,
    "isCasesTracking":true,
    "dateFrom":"2009-03-05",
    "dateTo":null,
    "sessionFrom":null,
    "sessionTo":null,
    "finalDocFrom":null,
    "finalDocTo":null,
    "minSum":0,
    "maxSum":-1,
    "sides":[
        {
            "name":"ООО \"ЛУКОЙЛ-Теплотранспортная компания\"",
            "shortName":"ООО \"ЛУКОЙЛ-Теплотранспортная компания\"",
            "inn":"3445102073",
            "ogrn":"1093460001095",
            "okpo":"",
            "address":"400066, ВОЛГОГРАДСКАЯ обл, ВОЛГОГРАД г, ИМ СКОСЫРЕВА ул, д.7",
            "statusId":null,
            "statusName":null,
            "isBranch":false,
            "isOriginal":true
        },
        {
            "inn":"3445102073",
            "name":"ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ \"ЛУКОЙЛ-ТЕПЛОТРАНСПОРТНАЯ КОМПАНИЯ\"","shortName":"ООО \"ЛУКОЙЛ-ТТК\"",
            "address":"400066, ВОЛГОГРАДСКАЯ ОБЛАСТЬ, ГОРОД ВОЛГОГРАД, УЛИЦА ИМ СКОСЫРЕВА, Д.  7",
            "ogrn":"1093460001095",
            "okpo":"60915315",
            "isUnique":false,
            "isBranch":false,
            "organizationDictId":null,
            "storageId":4477117,
            "statusId":null
        }
    ],
    "coSides":[],
    "accuracy":0,
    "generalCaseTypes":null,
    "side":null,
    "executionObject":null,
    "executionStatus":-1,
    "minExecutionSum":0,
    "maxExecutionSum":-1,
    "executionsDateFrom":null,
    "executionsDateTo":null,
    "generalCourts":null
}
</pre></code>

#### Response:

<pre><code>
{
  "message": null,
  "serverDate": "2016-08-06T09:08:27.0002762+03:00",
  "result": {
    "counts": {
      "casesAny": 5172,
      "plaintiff": 4537,
      "respondent": 312,
      "third": 457
    },
    "sums": {
      "casesAny": 5848898563.829999,
      "plaintiff": 6285478904.4599991,
      "respondent": 436580340.63000005,
      "third": 338465131.16
    },
    "sumsKey": null
  },
  "success": true,
  "timings": [
    "jsonCamelCase 00:00:00"
  ]
}
</pre></code>

* casesAny - *(int)* количесво арбитражных дел
* plaintiff - *(int)* в качестве исца
* respondent - *(int)* в качестве ответчика
* third - *(int)* в качестве третьего лица
* sums - *(int)* исковые требования

# Статистика арбитражных дел
#### Request URL:
    https://casebook.ru/api/Card/OrgStatBySideTypes
#### Request Method:
    POST
#### Request Payload:

<pre><code>
{
    "statusEx":null,
    "sideTypes":null,
    "monitoredStatus":-1,
    "considerType":-1,
    "courtType":-1,
    "caseResults":null,
    "caseTypes":null,
    "caseCategoryId":null,
    "bankruptStages":null,
    "courts":null,
    "instances":null,
    "judges":null,
    "delegate":"",
    "stateOrganizations":null,
    "isNeedFnsChanges":true,
    "isNeedMAClaims":true,
    "isNeedAccuracy":2,
    "isNeedWritsTracking":false,
    "isNeedNewCasesTracking":true,
    "isMessageFrTracking":true,
    "isCasesTracking":true,
    "dateFrom":"2015-08-06",
    "dateTo":"2016-08-06",
    "sessionFrom":null,
    "sessionTo":null,
    "finalDocFrom":null,
    "finalDocTo":null,
    "minSum":0,
    "maxSum":-1,
    "sides":[
        {
            "name":"ООО \"ЛУКОЙЛ-Теплотранспортная компания\"","shortName":"ООО \"ЛУКОЙЛ-Теплотранспортная компания\"",
            "inn":"3445102073",
            "ogrn":"1093460001095",
            "okpo":"",
            "address":"400066, ВОЛГОГРАДСКАЯ обл, ВОЛГОГРАД г, ИМ СКОСЫРЕВА ул, д.7",
            "statusId":null,
            "statusName":null,
            "isBranch":false,
            "isOriginal":true
        },
        {
            "inn":"3445102073",
            "name":"ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ \"ЛУКОЙЛ-ТЕПЛОТРАНСПОРТНАЯ КОМПАНИЯ\"","shortName":"ООО \"ЛУКОЙЛ-ТТК\"",
            "address":"400066, ВОЛГОГРАДСКАЯ ОБЛАСТЬ, ГОРОД ВОЛГОГРАД, УЛИЦА ИМ СКОСЫРЕВА, Д.  7",
            "ogrn":"1093460001095",
            "okpo":"60915315",
            "isUnique":false,
            "isBranch":false,
            "organizationDictId":null,
            "storageId":4477117,
            "statusId":null
        }
    ],
    "coSides":[],
    "accuracy":0,
    "page":1,
    "count":30,
    "generalCaseTypes":null,
    "side":null,
    "executionObject":null,
    "executionStatus":-1,
    "minExecutionSum":0,
    "maxExecutionSum":-1,
    "executionsDateFrom":null,
    "executionsDateTo":null,
    "generalCourts":null
}
</pre></code>

#### Response:

<pre><code>
{
  "message": null,
  "serverDate": "2016-08-06T09:38:44.0001942+03:00",
  "result": {
    "counts": {
      "plaintiff": 1464,
      "respondent": 59,
      "third": 158,
      "other": 17,
      "casesAny": 1685
    },
    "sums": {
      "plaintiff": 2471010788.57,
      "respondent": 97253007.219999984,
      "third": 33892329.84,
      "other": 4315210.26,
      "casesAny": 0.0
    },
    "sumsKey": null
  },
  "success": true,
  "timings": [
    "jsonCamelCase 00:00:00"
  ]
}
</pre></code>

* plaintiff - *(int)* в качестве исца
* respondent - *(int)* в качестве ответчика
* third - *(int)* в качестве третьего лица
* casesAny - *(int)* в качестве иного лица
* counts - *(int)* количесво дел
* sums - *(int)* исковые требования
