*** Settings ***
Library                 ../page_objects/NBAPlayersPage.py         https://stats.nba.com/players/traditional/
Library                 Selenium2Library
Resource                ../res_files/utilities.robot


*** Keywords ***

Open the players stats page 
        open_page         

Select player stats pagination limit to ${limit} 
        select_player_stats_table_pagination         option=${limit}
        get_player_details


verify if all the player PTS for team "${team}" is consistent
        verify_player_pts              team=${team}

Apply advance filter for player stats with team "${team}"
        apply_team_specific_filter             full_team=${team}

Get player PTS for team "${team}"
        ${details}=                  get_player_PTS_details            team_name=${team}
        Return From Keyword             ${details}

Verify the loading of the players stats segment is below "${time}" secs
        verify_STATS_loading_time_within_specified                  wait_time=${time}      segment=Stats