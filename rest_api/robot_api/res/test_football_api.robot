***Settings*** 

Library     ../test_src/FootBallAPICalls.py
Library     Collections


*** Keywords *** 


verify response ${res} if status code equals expected code ${expected_code}
    verify_response_with_expected_code     res=${res}      expected_code=${expected_code}       

Request get with uri ${uri} and verify if reposne status code is equal to ${expected_code}
    ${res}=         get_request     uri=${uri}         head_data=${None}
    Log       ${res}  
    verify response ${res} if status code equals expected code ${expected_code}        

Test log data ${data1}
    Log   "Simple text"
    ${test_data}=       test_print    strp=${data1}
    LOG     ${test_data}