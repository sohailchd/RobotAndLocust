*** Settings ***
Documentation                    Create a test which checks top three players on this page :- 
...                              http://stats.nba.com/leaders/. 
...                              Please check if the following stats of these players (points per game, assists per game, 
...                              rebounds per game) are matching same stats categories displayed on their player page.

Resource                         nba_leaders_res.robot 
Resource                         utilities.robot 

Default Tags                     all     leaders  

*** Variables ***
${top}                           3


*** Test Cases *** 
Verify stats of the top 3 players 

    @{TOP_PLAYERS}=       Get the stats of the top "${3}" players on the leader board

    :FOR    ${ELEMENT}    IN    @{TOP_PLAYERS}
    \       Log     ${ELEMENT}


    ### grab all the details in the leader board play 
    ### go to each player page and assert the stats from the leader board page
    ### we are comparing (points per game, assists per game, rebounds per game) of the players 
    ### from leader board to their player page
    verify if the top "${top}" players in leader board have consistent stats compared to thier player page
