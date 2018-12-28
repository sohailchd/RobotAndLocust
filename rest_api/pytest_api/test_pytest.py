
import requests 
import json 
import pytest
import logging


base_url = "https://api.football-data.org/"
log = logging.getLogger(__name__)

auth_token = {
    'X-Auth-Token' : '28d90f03ec984213bb293766a062ef44'
}


##### additional summary 


@pytest.mark.competitions
@pytest.mark.all
class TestCompetitions():


    
    def test_get_competitions(self):
        '''
        uri : /v2/competitions/
        action : List all available competitions.
        test : verify response status == 200 OK
               verify if the response contains competitions
        '''
        uri = base_url + "/v2/competitions"
        response = requests.get(uri,headers=auth_token)
        print(f"Response : {response.status_code}")
        print(response.headers)
        ## assert expected status code
        assert response.status_code == 200
        ## assert response 
        response_content = response.json() 
        print(response_content)
        assert response_content , ("Response is empty")



    
    @pytest.mark.competitions_filter
    def test_get_competitions_with_filter_plan(self):
        ''' uri : /v2/competitions
            action : List one particular competition.
            test :  verify response status == 200 OK
                    test filter type plan={PLAN}
        '''
      
        ## test for each type of plan filter
        ## verify that response contains only the given filter and nothing else
        tiers_list = ['TIER_ONE','TIER_TWO','TIER_THREE','TIER_FOUR']
        for tier in tiers_list:
            uri_plan = base_url + "/v2/competitions?plan=" + str(tier)
            response = requests.get(url=uri_plan,headers=auth_token)
            assert response.status_code == 200
            print(f"Response code for {tier} : {response.status_code}")
            json_res = response.json()
            for com in json_res['competitions']:
                assert com['plan'] == str(tier)
        

    @pytest.mark.particular_competition
    def test_particular_competition(self):
        '''
            uri : /v2/competitions/2000
            action : List one particular competition.
            test : verify status == 200 OK 
                   response should have details of particular competitions
        '''
        uri = base_url + "/v2/competitions/2000"
        response = requests.get(uri,headers=auth_token)
        print(f"Response : {response.status_code}")
        assert response.status_code == 200
        print(response.json())
        assert response.json()['area'] , ("area info for competition id: 2000 is empty")



    @pytest.mark.error_code
    @pytest.mark.xfail
    def test_get_competitions_wrong_uri(self):
        ''' 
          url : v2/competitions/areases
          action : Error message 
          test : verify if the status == 400
                 verify the response message
        '''
        url = base_url + "v2/competitions/areases"
        response = requests.get(url,headers=auth_token)
        assert response.status_code == 400
        ## verify if proper error msg is send in the response
        expected_error_msg = "Parameter 'competitionId' is expected to be either an integer in a specified range or a competition code."
        print(response.json()['message'])
        print(f"Response : {response.status_code}")
        assert response.json()['message'] == expected_error_msg
    


@pytest.mark.teams
@pytest.mark.all
class TestTeams():

   
    def test_list_team_for_competition_id(self):
        '''
        uri : "/v2/competitions/{id}/teams" 
        action : List all teams for a particular competition.
        test : verify if uri returns team for a competition id 
               status == 200
        '''
        url = base_url + "/v2/competitions/2000/teams"
        response = requests.get(url,headers=auth_token)
        print(f"Response : {response.status_code}")
        assert response.status_code == 200 
        ## verify if the json have competition with id=2000 
        print(response.json()['competition']['id'])
        assert response.json()['competition']['id'] == 2000



    
    def test_list_team_competition_id(self):
        '''
        uri : "/v2/competitions/{id}/teams" 
        action : List all teams for a particular competition.
        test : verify if uri returns team for a competition id 
               status == 405 
        '''
        url = base_url + "/v2/competitions/2000/teams"
        response = requests.post(url,headers=auth_token)
        print(response.json())
        print(f"Response : {response.status_code}")
        assert response.status_code == 405




@pytest.mark.matches
@pytest.mark.all
class TestMatches():
    

        @pytest.mark.error_code
        @pytest.mark.xfail 
        def test_upcomming_matches_without_auth(self):
            '''
                uri : "v2/teams/86/matches?status=SCHEDULED"
                test : expected status == 403
            '''
            uri = base_url + "v2/teams/86/matches?status=SCHEDULED"
            ### send request without auth-token
            response = requests.get(uri)
            print(f"Response : {response.status_code}")
            assert response.status_code == 403

        
        def test_upcomming_matches(self):
            '''
                uri : "v2/teams/86/matches?status=SCHEDULED"
                test : expected status == 200
            '''
            uri = base_url + "v2/teams/86/matches?status=SCHEDULED"
            ### send request without auth-token
            response = requests.get(uri,headers=auth_token)
            print(f"Response : {response.status_code}")
            assert response.status_code == 200
            print(response.json())
            assert response.json()['count'] == 24



        @pytest.mark.error_code
        @pytest.mark.xfail
        def test_match_across_competitions_with_wrong_uri(self):
            '''
                uri : /v2/matche "instead of" /v2/macthes
                test : List matches across (a set of) competitions.
                       expected response code == 404
            '''

            url = base_url + '/v2/matche'

            response = requests.get(url,headers=auth_token)
            print(f"Response : {response.status_code}")
            assert response.status_code == 404
            print(response.headers)



        @pytest.mark.error_code
        @pytest.mark.xfail
        def test_match_across_competitions(self):
            '''
                uri : /
                test : disable redirection verify
                       expected response code == 301
            '''

            url = base_url + '/'

            response = requests.get(url,headers=auth_token,allow_redirects=False)
            print(f"Response : {response.status_code}")
            assert response.status_code == 301
            print(response.headers)
        

                


@pytest.mark.areas
@pytest.mark.all
class TestAreas():
    

    def list_one_particular_area(self):
        '''
            uri : /v2/areas/
            test : List all available areas.
                   expected_status code == 200
        '''
        url = base_url + "/v2/areas"
        response = requests.get(url,headers=auth_token)
        print(f"Response : {response.status_code}")
        assert response.status_code == 200 

        
