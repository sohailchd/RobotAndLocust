*** Settings ***
Documentation           NBA tests for stats related to standings : 
...                     Test which checks accuracy of the overall number of wins of teams from Eastern
...                     and Western conference during regular season.
...                     url: https://stats.nba.com/standings/ 

Default Tags            all     standings    conference

Resource                utilities.robot
Resource                nba_standings_res.robot
Library                 SeleniumLibrary


Suite Setup             Initialize test browser and test setup
Suite Teardown          Close all Browsers and teardown setup



*** Variables *** 
${total_team_conference}      15
${total_team_division}        05
${total_team_nba}             30
${total_win_east_conf}        ${None}
${total_win_west_conf}        ${None}
${conf_list}                  East,West


*** Test Cases ***

Verify both the conference are shown and consists of 15 teams each 

    Verify if the NBA Stats page shows table with expected "${conf_list}" conference
    Verify if the NBA Stats page shows consistent conference with each having 15 teams
    Verify win percentage of each team is correct as per their wins and losses proportions

    Verify overall wins should be equal to sum of wins in home and road 
    Verify overall losses should be equal to sum of losses in home and road 
    