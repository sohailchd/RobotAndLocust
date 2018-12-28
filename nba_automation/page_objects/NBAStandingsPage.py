from locators.NBAStandingsLocators import NBAStandingsLocators
from page_objects.BasePage import BasePage, driver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import math

class NBAStandingsPage(BasePage):


    def filter_by_season_type(self,season_type=""):         
        driver.find_element(*NBAStandingsLocators.FILTER_SEASONTYPE)
    

    def verify_if_two_conference_shown(self,expected_conf):
        table = driver.find_elements(*NBAStandingsLocators.CONF_TABLES)
        print(f"no. of tables : {len(table)}")
        expected_conf_list = expected_conf.split(",")
        self.actual_list = []
        for tab in table:
            self.actual_list.append(tab.find_element(By.CSS_SELECTOR,"div.nba-stat-table__caption").text)

        assert expected_conf_list == self.actual_list,     (f"Conference names are inconsistent. actual {self.actual_list} , expected : {expected_conf_list}")
    

    def get_team_stats(self,conf_zone):
        '''
        '''
        table = driver.find_elements(*NBAStandingsLocators.CONF_TABLES)
        print(f"no. of tables : {len(table)}")

        if conf_zone.upper() == "EAST":
            target_table = table[0]
            print(f"choosing 1st table for EAST")
        else:
            target_table = table[1]
            print(f"choosing 2nd table for WEST")

        table_content = target_table.get_attribute('innerHTML')
        soup = BeautifulSoup(table_content,features='lxml')
        print(f"Total rows in page : {len(soup.find_all('tr'))}")
        
        
        trlist =  soup.find_all('tr')
        thdeaders = []
        hd_data = trlist[0]
        ## find the columns
        for th in hd_data.find_all('th'):
            thdeaders.append(th.text)
        #### adjustmenst for header names of table 
        thdeaders.pop(0)  ## remove the first col i.e. Team
        thdeaders[9] = 'LAST 10'
        print(thdeaders)
        
        # ## find the teams list
        # teams = soup.find_all('td',{"class" : "team"})
        # teams_list = []
        # for t in teams:
        #     teams_list.append(t.text.rstrip().lstrip().split('.')[1].rstrip())
    

        self.team_list = []    
        new_trs = trlist[1:16] 
        self.team_data = {}
        for t in new_trs:
            lst = t.text.split('\n')
            self.team_list.append(lst[5])
            clist = list(filter(lambda x: x != '', lst[10:-1]))
            self.team_data[lst[5]] = clist
        
        
        self.complete_dict = {}
        for team in  self.team_list:
            tmp = dict(zip(thdeaders, self.team_data[team]))
            self.complete_dict[team] = tmp

        print("------------------------------")  
        
        self.conf_dict = {}
        self.conf_dict[conf_zone] = self.complete_dict
        print(self.conf_dict)
        return self.conf_dict

    
    def verify_conf_team_counts(self,expected_count):
        '''
        '''
        east_team_stats = self.get_team_stats("EAST")['EAST']   ## east 
        west_team_stats = self.get_team_stats("WEST")['WEST']   ## west
        ex_east,ex_west = expected_count.split(',')[0],expected_count.split(',')[1]
        assert len(east_team_stats.keys()) == int(ex_east),   (f"EAST : actual {len(east_team_stats.keys())} and expected {ex_east} not equal")
        assert len(west_team_stats.keys()) == int(ex_west),   (f"WEST : actual {len(west_team_stats.keys())} and expected {ex_west} not equal")
        
        
    def verify_win_percentage(self,conf_zone):
        ''' 
            verifies if the win% is consistent for each team
        '''
        zone_table = self.get_team_stats(conf_zone)[conf_zone]
        for team in zone_table.keys():
            win_pc = float(zone_table[team]['WIN%'])
            win_loss = float(zone_table[team]['W']) / ( float(zone_table[team]['W'])+float(zone_table[team]['L']))
            assert win_pc == round(win_loss,3)
        
    
    def verify_win_vs_loss_between_conf(self):
        '''
          Since, all the games are no tie, all the wins in conf should be equal 
          to all the loss in other conf teams i.e.
          sum_of_all_wins_east == sum_of_all_losses_west and vice versa
        '''
        east_table = self.get_team_stats('East')['East']
        west_table = self.get_team_stats('West')['West']
        ewins,wwins = 0,0
        for eteam in east_table.keys():
            print(east_table[eteam]['CONF'].split('-')[0])
            ewins += int(east_table[eteam]['CONF'].split('-')[0])

        for eteam in west_table.keys():
            print(west_table[eteam]['CONF'].split('-')[1])
            wwins += int(west_table[eteam]['CONF'].split('-')[1])
        
        print(f" {ewins} {wwins}")
        assert  ewins == wwins,     ("win and loss are inconsistent between conf zones")
        

    def verify_overall_wins_with_road_home(self,win=True):
        '''
            params : win (boolean),
            if win == True
            verifies : total_wins = win_home + win_road
            else verifies : total_loss = loss_home + loss_road
        '''
        east_table = self.get_team_stats('East')['East']
        west_table = self.get_team_stats('West')['West']
        
        ## combine both the tables
        east_table.update(west_table)

        ## for east zone 
        for data in east_table.values():
            
            if win:
                win = int(data['W'])
                home_win = int(data['HOME'].split('-')[0])
                road_win = int(data['ROAD'].split('-')[0])
                assert win == (home_win+road_win)  , (f"inconsistent wins {win} != {home_win+road_win}")
            else:
                loss = int(data['L'])
                home_loss = int(data['HOME'].split('-')[1])
                road_loss = int(data['ROAD'].split('-')[1])
                assert loss == (home_loss+road_loss)  , (f"inconsistent wins {win} != {home_loss+road_loss}")
            
