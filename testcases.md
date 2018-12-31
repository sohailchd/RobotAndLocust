# Test cases


## **load_test**

Test decribes following user behaviour and creates 1000 clients requests within 15secs.  
```
Step 1. User goes to homepage https://www.football-data.org/  
Step 2. User signin (https://www.football-data.org/client/login) using email and auth-token    
Step 3. User visits the api documentation at https://www.football-data.org/documentation/api    
```
These steps are done sequentially by each user.

------------------------------------------------------------------

## **nba_automation**
There 3 different sections of the website covered by the automation.

**Player stats page**
```
1. Test player PTS are shown and not empty for specific teams (without appying any filters)  
2. Test players PTS are shown and not empty for specific teams after appying advance filter     
3. Test player PTS shown before and after applying filters are same, not changed
4. Test loading time for the stats segment is below specified time limit 
```
**Leaders stats**
```
1. Verify stats of the top 3 players matches stats on particular player page
```  

**Team Standings**
```
1.  Verify both the conference are shown and consists of 15 teams each 
    
```


## **rest_api**

**Robot version : 5 Test cases**
```
1. List all available competitions , expected_response_code==200
2. List one particular competition, expected_response_code==200
3. Get competitions with wrong uri, expected_response_code==400
4. Get upcomming matches without auth, expected_response_code==403
5. Get redirection with multiple res, expected_response_code==301
```
**Pytest version : 10 Test cases**
