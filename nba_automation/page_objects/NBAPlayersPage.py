
from page_objects.BasePage import BasePage,driver
import conf
from selenium.webdriver.support.ui import Select
from locators.NBAPlayersLocators import NBAPlayersLocators
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from utilities.CustomUtils import CustomUtils
import time


class NBAPlayersPage(BasePage):

    
    def get_player_details(self,team_param=None):
        '''
            params: team_list
            fetches the list of all the players details from the team_param 
            if team_param is None. return all the players form each team
        '''
        table = driver.find_element(*NBAPlayersLocators.stats_table)
        
        content = table.get_attribute('innerHTML')
        soup = BeautifulSoup(content,features='lxml')
        
        headers = []
        table_headers = soup.find_all('th')
        for h in table_headers[:30]:
            headers.append(h.text)
        
        headers.pop(0)   ## remove the first element
        print(headers)

        ## all the player details, in respective teams
        player_details = dict()

        ## save all the teams 
        team_list = set()
        all_trows = []
        ### create the final stats table
        for tr in soup.find_all('tr')[1:]:
            tdlist = tr.find_all('td')[1:]
            tdata = []
            for t in tdlist:
                if t.text:
                    tdata.append(t.text)

            ### append the team in the team_list 
            team_list.add(tdata[1])
            player_details[tdata[1]] = dict()
            ### create temp dicts
           
            tmp = {}
            tmp = dict(zip(headers,tdata))
            tmp2 = { tdata[0] : tmp }
            all_trows.append(tmp2)
            # print(f"---------------- \n {tmp2}")
            # player_details[tdata[1]].update(tmp2)
            
        
        ## compile all the table in teamwise dicts
        for row in all_trows:
            for data in row.values():
                if data['TEAM'] in player_details.keys():
                    player_details[data['TEAM']].update(row)

        
        ## filter the required player details
        rdetails = None
        if team_param == None:
            rdetails = player_details
        else:
            rdetails =  player_details[team_param]

        print(rdetails)
        return rdetails


    def get_player_PTS_details(self,team_name):
        '''
        '''
        print(f"getting player details for team : {team_name}")
        player_stats = self.get_player_details(team_name)
        player_PTS = dict()
        for player,data in player_stats.items():
            player_PTS.update({ player : data['PTS'] })
        
        return player_PTS

    
    def select_player_stats_table_pagination(self,option="All"):
        '''
        '''
        print(f"option : {option}")
        pagination_select = Select(driver.find_element(*NBAPlayersLocators.pagination_selector))
        pagination_select.select_by_visible_text(option)
        self.explicit_wait(NBAPlayersLocators.eleventh_row,10)
    

    def verify_player_pts(self,team):
        '''
        param: team (string)
            -verify if PTS is not empty 
            -verify if PTS is valid numeric 
        '''
        print(f"team: {team} ")
        player_stats = self.get_player_details(team)

        for playerName,data in player_stats.items():
            print(f"- {playerName} : PTS: {data['PTS']} ")
            assert (data['PTS'] not in ['-',' ']) == True, f"PTS for {playerName} is missing , actual PTS : {data['PTS']}"
            assert CustomUtils.verify_str_contains_numeric(data['PTS'])==True, (f"{data['PTS']} is doest not contain numeric value") 


    def apply_team_specific_filter(self,full_team=None):
        '''
        '''
        print(f"team : {full_team}")

        ## click advance filter 
        driver.find_element(*NBAPlayersLocators.advance_filter).click()
        ## reset any previous filters 
        driver.find_element(*NBAPlayersLocators.reset_filters).click()
        driver.find_element(*NBAPlayersLocators.advance_filter_team_byteam).click()
        team_options = Select(driver.find_element(*NBAPlayersLocators.advance_filter_team_byteam))
        team_options.select_by_visible_text(full_team)

        ## apply the filter with click run-it link
        driver.find_element(*NBAPlayersLocators.run_it).click()
        ## close the advance filter page
        driver.find_element(*NBAPlayersLocators.advance_filter).click()


    def verify_STATS_loading_time_within_specified(self,wait_time=1,segment=None):
        '''
            params: time (str)
            verifies if the loading time is withing specified time limit
        '''
        start = time.time()
        ## navigate to the players stats page 
        driver.get(self.page_url)

        ## wait for stats table to load in the DOM 
        self.explicit_wait(NBAPlayersLocators.stats_table)
        end = time.time()
        print(f" total time in ms : {end-start}")
        assert float(end-start) < float(wait_time)  ,  ("Loading time exceeded for the stats table on players page.")

    
