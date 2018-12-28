** Settings *** 
Library        ../utilities/BrowserManager.py
Library        ../utilities/CustomUtils.py 

*** Variables ***
${base_url}        http://stats.nba.com/


*** Keywords ***
Initialize test browser and test setup
    Log      "Suite Initialized...."


Close all Browsers and teardown setup
    Log       "Suite teardown called..."

Refresh the current page 
    refresh_page
    