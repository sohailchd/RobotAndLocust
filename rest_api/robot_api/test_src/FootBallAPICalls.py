import requests 
import json

from robot.api.deco import keyword
import pytest
import logging



base_url = "https://api.football-data.org/"
log = logging.getLogger(__name__)


header = {
    'X-Auth-Token' : '28d90f03ec984213bb293766a062ef44'
}


class FootBallAPICalls():

    ROBOT_LIBRARY_SCOPE = 'TEST CASE'


    def test_print(self,strp):
        print(strp)
        return "test data"

    @keyword
    def get_request(self,uri,head_data={}):
        '''
        '''
        if not uri:
            raise ValueError("uri parameter is None")
        
        url = base_url + uri
        print(url)
        
        response = None
        if head_data:
            header.update(head_data)
        
        response = requests.get(url,headers=header)
        print(response)
        res_dict = {
            'status_code' : response.status_code,
            'response_json' : response.json(),
            'response_header' : response.headers
        }

        return res_dict
    

    def verify_response_with_expected_code(self,res,expected_code):
        '''
        '''
        status_code = res['status_code']
        assert  status_code == int(expected_code),     f"status code is not equal to expected value, {status_code} != {res['status_code']}"