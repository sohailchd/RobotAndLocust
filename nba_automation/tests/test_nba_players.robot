*** Settings ***
Documentation              Create a test which checks average points per game (PTS) 
...                        for players of two teams - Golden State Warriors and Houston Rockets.
...                        For this purpose use this page 
...                        https://stats.nba.com/players/traditional and search filter in top right corner to get player stats
...                        per team. We want to check the number (PTS) is correct and was not changed or not displayed.

Default Tags               all   players                 
Resource                   nba_players_res.robot 
Resource                   utilities.robot
Library                    Collections

Suite Setup             Initialize test browser and test setup
Suite Teardown          Close all Browsers and teardown setup


*** Variables ***
${golden_state_warriors}             GSW    
${houston_rockets}                   HOU


*** Test Cases *** 

Test player PTS are shown and not empty for specific teams (without appying any filters) 
    Select player stats pagination limit to All
    verify if all the player PTS for team "${golden_state_warriors}" is consistent
    verify if all the player PTS for team "${houston_rockets}" is consistent

     
Test players PTS are shown and not empty for specific teams after appying advance filter 
    [Setup]        Open the players stats page
    Apply advance filter for player stats with team "Golden State Warriors"
    verify if all the player PTS for team "${golden_state_warriors}" is consistent

    Apply advance filter for player stats with team "Houston Rockets"
    verify if all the player PTS for team "${houston_rockets}" is consistent


Test player PTS shown before and after applying filters are same, not changed

    [Setup]        Open the players stats page
    Select player stats pagination limit to All
    ${details_before_gsw}=            Get player PTS for team "${golden_state_warriors}"
    ${details_before_hou}=            Get player PTS for team "${houston_rockets}"


    Apply advance filter for player stats with team "Golden State Warriors"
    ${details_after_gsw}=            Get player PTS for team "${golden_state_warriors}"
    Apply advance filter for player stats with team "Houston Rockets"
    ${details_after_hou}=            Get player PTS for team "${houston_rockets}"

    Dictionaries Should Be Equal       ${details_before_gsw}     ${details_after_gsw}         "Player PTS differ for GSW"
    ### expected to fail
    Dictionaries Should Be Equal       ${details_before_hou}     ${details_after_hou}         "Player PTS differ for HOU"


Test loading time for the stats segment is below specified time limit 
    Verify the loading of the players stats segment is below "4" secs

    ## now refresh the page and verify again
    Refresh the current page 
    Verify the loading of the players stats segment is below "4" secs