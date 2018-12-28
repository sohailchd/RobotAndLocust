*** Settings ***
Library          ../page_objects/NBAStandingsPage.py      https://stats.nba.com/standings/


*** Keywords ***
Test function call       
    filter_by_season_type


Verify if the NBA Stats page shows table with expected "${expected_conf}" conference
    verify_if_two_conference_shown           expected_conf=${expected_conf}

Verify if the NBA Stats page shows consistent conference with each having 15 teams
    verify_conf_team_counts                  15,15

Verify win percentage of each team is correct as per their wins and losses proportions
    verify_win_percentage                    East


To be implemented 
    verify_win_vs_loss_between_conf

Verify overall wins should be equal to sum of wins in home and road 
    verify_overall_wins_with_road_home

Verify overall losses should be equal to sum of losses in home and road 
    verify_overall_wins_with_road_home      win=${TRUE}

