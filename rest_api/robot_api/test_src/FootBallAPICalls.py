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


    def __init__(self):
        self.response = None

    def test_print(self,strp):
        print(strp)
        return "test data"

    @keyword
    def send_request(self,uri,rtype="GET",head_data={},post_data={}):
        '''
        '''
        if not uri:
            raise ValueError("uri parameter is None")
        
        url = base_url + uri
        print(f"final url : {url}")

        response = None
        if head_data:
            header.update(head_data)
        
        if rtype.upper() == "GET":
            response = requests.get(url,headers=header)
        elif rtype.upper() == "POST":
            response = requests.post(url,headers=header,data=post_data)
        elif rtype.upper() == "GET_WITHOUT_AUTH":
            response = requests.get(url)
        else:
            ## default type is GET
             response = requests.get(url,headers=header)
        
        
        print(f"Response from the {rtype} call ({url}) : {response}")

        self.res_dict = {
            'status_code' : response.status_code,
            'response_json' : response.json(),
            'response_header' : response.headers
        }

        return self.res_dict
    

    def verify_response_with_expected_code(self,expected_code):
        '''
        '''
        if not self.res_dict:
            raise ValueError("No HTTPS response found.")

        status_code = self.res_dict['status_code']
        assert  status_code == int(expected_code),     f"status code is not equal to expected value, {expected_code} != {self.res_dict['status_code']}"