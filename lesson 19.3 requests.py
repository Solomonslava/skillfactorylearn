import json.decoder

import requests as re


def get_api(email, password):
    site = 'https://petfriends.skillfactory.ru/api/key'
    res = re.get(site, headers={'email': email, 'password': password})
    status = res.status_code
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    return status, result

print(get_api('solomonslava1991@gmail.com', 'solomon0204'))


