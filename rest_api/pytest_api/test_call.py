

import requests
import json
import pytest

email = "sohail.chd0202@gmail.com"
api_token = "28d90f03ec984213bb293766a062ef44"

header_data = {
    'X-Auth-Token' : api_token,
    'X-API-Version' : 'v2'
}

@pytest.mark.test_id(1501)
def test_get_data():
    url_competions = "http://api.football-data.org/v2/teams"
    r = requests.get(url_competions,headers=header_data)
    # print(r.json())
    print(r.status_code)
    print(r.headers)

@pytest.mark.test_id4(1501)
def test_get_data2():
    url_competions = "http://api.football-data.org/v2/teams"
    r = requests.get(url_competions,headers=header_data)
    # print(r.json())
    print(r.status_code)
    print(r.headers)

@pytest.mark.test_id3(1501)
def test_get_data3():
    url_competions = "http://api.football-data.org/v2/teams"
    r = requests.get(url_competions,headers=header_data)
    # print(r.json())
    print(r.status_code)
    print(r.headers)

## list the /competitions
## try to access the /competitions with invalid token
## 