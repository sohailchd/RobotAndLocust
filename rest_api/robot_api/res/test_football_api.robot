***Settings*** 

Library     ../test_src/FootBallAPICalls.py
Library     Collections


*** Variables ***
${response}    =      None


*** Keywords *** 


verify response status code equals expected code "${expected_code}"
    verify_response_with_expected_code         expected_code=${expected_code}         


Send request with uri "${uri}" and request type "${rtype}"     
    ${response}=              send_request     uri=${uri}       rtype=${rtype}   head_data=${None}
    Log       ${response}   
    Return From Keyword       ${response} 





