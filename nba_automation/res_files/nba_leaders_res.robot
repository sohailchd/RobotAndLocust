*** Settings ***
     
Library                 ../page_objects/NBALeadersPage.py         http://stats.nba.com/leaders/
Library                 Selenium2Library
Resource                ../res_files/utilities.robot


*** Keywords *** 
Get the stats of the top "${top}" players on the leader board
    @{top_players}=            get_leaders_details           top=${top}
    Return From Keyword        @{top_players}

verify if the top "${top}" players in leader board have consistent stats compared to thier player page  
    verify_player_details_matches_leader_tables         top=${top}