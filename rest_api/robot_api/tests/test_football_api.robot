*** Settings ***
DOCUMENTATION       Testing the https://www.football-data.org public API 

Resource            ../res/test_football_api.robot

Test Template         Test the API resource and verify the status code


*** Variables *** 
${status_200}            200
${status_400}            400

        

*** Test Cases ***                          resquest_type               url                                      expected_res_code    
List all available competitions               GET                   v2/competitions/                                    200
List one particular competition               GET                   v2/competitions                                     200
Get competitions with wrong uri               GET                   v2/competitions/areases                             400
Get upcomming matches without auth       GET_WITHOUT_AUTH       v2/teams/86/matches?status=SCHEDULED                    403            
Get redirection with multiple res        GET_DISABLE_REDIRECT           /                                               301




*** Keywords *** 

Test the API resource and verify the status code
        [Arguments]              ${resquest_type}              ${url}            ${expected_res_code}       
        
        Send request with uri "${url}" and request type "${resquest_type}"
        verify response status code equals expected code "${expected_res_code}"