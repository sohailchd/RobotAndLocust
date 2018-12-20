*** Settings ***
DOCUMENTATION       Testing the https://www.football-data.org public API 

Resource            ../res/test_football_api.robot


## https://github.com/robotframework/HowToWriteGoodTestCases/blob/master/HowToWriteGoodTestCases.rst

*** Variables *** 
${status_200}            200
${status_400}            400





*** Test Cases ***

Test all the competions
    Test get competitions with uri v2/competitions and status code 200






*** Keywords *** 

Test get competitions with uri ${uri} and status code ${code}
    Request get with uri ${uri} and verify if reposne status code is equal to ${code}
    Test log data data1   

