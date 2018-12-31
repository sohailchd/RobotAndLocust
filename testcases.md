# Test cases


## **load_test**



**Reports**     
a) Explain the test in details    
>
    Test decribes following user behaviour and creates 1000 clients requests within 15secs.      
    These steps are done sequentially by each user.   

    Step 1. User goes to homepage https://www.football-data.org/  
    Step 2. User signin (https://www.football-data.org/client/login) using email and auth-token    
    Step 3. User visits the api documentation at https://www.football-data.org/documentation/api    

Since Locust uses gevents (coroutine based lib for N/W), we can scale the user to large 
numbers compared to threads on a single machine.   
We can even setup distributed clients for simulating the load.


b) Did the load test have an impact on web application response time?      
> 
    Yes, load have an impact on the website. Average response time suffered.     
    More than 300 request took more than 3secs out of approx 1200 request.     
    All the reports are kept in  "load_test\reports_final\"

c) What is the optimal application response time for modern day web applications?   
> 
    It is all about perception and human psychology. Even the screen we are staring is not         
    continuous which flickers at 30 Hz or may be 60Hz. Anything which have have a response time above 1/10 sec can    
    be perceived by normal humans. In the age of internet and instant gratification anything which lags by     
    even 1sec is huge deal. For an web application to be usable by people should take into consideratiion 
    of the target audience and type of the service offered.   

    I feel anything which have response time of more than 3secs or 4sec affects the user experience.  

d) Analyze few HTTP/S responses
>
    - Please find the HTTP logs in "load_test\reports_final\locust_log.log" 
    - Please find the "load_test\reports_final\correlation.png" for graph 
      showing inscrease in response time with increase in users visiting the site.



## **nba_automation**
There 3 different sections of the website covered by the automation.

**- Player stats page**
>
    1. Test player PTS are shown and not empty for specific teams (without appying any filters)  
                - Go to https://stats.nba.com/players/traditional
                - Verify if PTS for players is not empty, doesn't have any special character and only numbers/decimal   

    2. Test players PTS are shown and not empty for specific teams after appying advance filter       
                -  Go to https://stats.nba.com/players/traditional    
                -  Now apply advance filter from the right corner in the table and choose team.       
                -  When the stats table updates and shows only player stats from a specific team    
                   verify if PTS for players is not empty, doesn't have any special character and only numbers/decimal       

    3. Test player PTS shown before and after applying filters are same, not changed   
                - Now verify if the stats matches and are same in above cases.   

    4. Test loading time for the stats segment is below specified time limit    
                - We try to verify if the stats table laods wihin specffic time    

> Bugs:  
    1. Test player PTS shown before and after applying filters are same, not changed      
                 - "Player PTS differ for HOU"  , Following keys have different values: Key Austin Rivers: 7.5 != 10.0   

    2. Test loading time for the stats segment is below specified time limit     # [FAILS] intermittent


**- Leaders stats**
> 
    1. Verify stats of the top 3 players matches stats on particular player page    
                - Go to leader board    
                - Compile all the player stats from the leader board page (http://stats.nba.com/leaders/)     
                - Now find the top three players with hightest PTS     
                - Individually go each player page by clicking on the player name     
                - Now verify if (points per game, assists per game, rebounds per game) are consistent with 
                  stats on leader board page.    
  

**- Team Standings**
>
    1.  Verify both the conference are shown and consists of 15 teams each 
                - Verify if the NBA Stats page shows table with both the conference EAST and WEST    
                - Verify if the NBA Stats page shows consistent conference with each having 15 teams    
                - Verify win percentage of each team is correct as per their wins and losses proportions   win%==(win)/total_mathces  
                - Verify overall wins should be equal to sum of wins in home and road colums     
                - Verify overall losses should be equal to sum of losses in home and road columns      


## **rest_api**

**Robot version : 5 Test cases**

>
    1. List all available competitions , expected_response_code==200
    2. List one particular competition, expected_response_code==200
    3. Get competitions with wrong uri, expected_response_code==400
    4. Get upcomming matches without auth, expected_response_code==403
    5. Get redirection with multiple res, expected_response_code==301

**Pytest version : 10 Test cases**
