*** Settings ***
DOCUMENTATION       Testing the https://www.football-data.org public API 

Resource            ../res/test_football_api.robot

Test Template         Test the API resource and verify the status code


*** Variables *** 
${status_200}            200
${status_400}            400

        

*** Test Cases ***                          resquest_type               url                         expected_res_code    
List all available competitions               GET                   /v2/competitions/                  200
List one particular competition               GET                   /v2/competitions





*** Keywords *** 

Test the API resource and verify the status code
        [Arguments]              ${resquest_type}              ${url}           ${post_data}                 ${expected_res_code}       
        
        Send request with uri "${url}" and request type "GET"
        verify response status code equals expected code "${expected_res_code}"