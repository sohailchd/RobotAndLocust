*** Settings ***
DOCUMENTATION       Testing the https://www.football-data.org public API 

Resource            ../res/test_football_api.robot

# Test Template         Test the API resource and verify the status code


*** Variables *** 
${status_200}            200
${status_400}            400





*** Test Cases ***

Test all the competions
    Test get competitions with uri v2/competitions and status code 200






*** Keywords *** 

Test get competitions with uri ${uri} and status code ${code}
    Request get with uri ${uri} with request type ${rtype}
    verify response ${res} status code equals expected code ${expected_code}   


# Test the API resource and verify the status code
#         [Arguments]              ${url}        ${resquest_type}       ${expected_res_code}
