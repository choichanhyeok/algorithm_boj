

# 'https://jsonmock.hackerrank.com/api/countries?name=Afghanistan'
import requests


def fuck():
    phoneNumber = '01077741874'
    countries = 'Afghanistan'

    res = requests.get('https://jsonmock.hackerrank.com/api/countries?name='+countries)
    json_res = res.json()

    result = '+' + json_res['data'][0].get('callingCodes')[0] + ' ' + phoneNumber
    return result

print(fuck())