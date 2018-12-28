from page_objects.BasePage import BasePage
from page_objects.BasePage import driver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import conf 

from locators.NBALeadersLocators import NBALeadersLocators , NBAPlayerPage


class NBALeadersPage(BasePage):


    def select_leader_stats_table_pagination(self,option="All"):
        '''
        '''
        print(f"option : {option}")
        pagination_select = Select(driver.find_element(*NBALeadersLocators.pagination_selector))
        pagination_select.select_by_visible_text(option)
        self.explicit_wait(NBALeadersLocators.eleventh_row,10)
    

    def get_leaders_details(self,top=None):
        '''
            params: top,
            fetches the list of all the player in leader board 
            if top is None. return all the players rankings
        '''
        self.select_leader_stats_table_pagination()
        table = driver.find_element(*NBALeadersLocators.player_leader_table)
        

        content = table.get_attribute('innerHTML')
        soup = BeautifulSoup(content,features='lxml')
        
        headers = []
        table_headers = soup.find_all('th')
        for h in table_headers[:30]:
            headers.append(h.text)
        
        headers.pop(0)   ## remove the first element
        headers.append('PlayerUrl')
        print(headers)

        ## all the player details, in respective teams
        leader_details = dict()

        ## save all the teams 
      
        all_trows = []
        player_page_links = []
        ### create the final stats table
        for tr in soup.find_all('tr')[1:]:
            tdlist = tr.find_all('td')[1:]

            ### now prepare the player page urls
            url = tdlist[0].find('a',href=True)['href']
            player_url = conf.base_url + url
            player_page_links.append(player_url)

            tdata = []
            for t in tdlist:
                if t.text:
                    tdata.append(t.text)


            ## append the link in the player data list 
            tdata.append(player_url)
            
            leader_details[tdata[1]] = dict()
            ### create temp dicts
           
            tmp = {}
            tmp = dict(zip(headers,tdata))
            tmp2 = { tdata[0] : tmp }
            all_trows.append(tmp2)
        
        if top == None:
            print(all_trows)
            return all_trows
        else:
            nth = int(top)
            print(all_trows[:nth])
            return all_trows[:nth]



    def get_player_details_from_player_page(self,url=None):
        '''
            params: top (no. of top player to be fetched)
            default = 3
        '''
        driver.get(url)
        player_name = driver.find_element(*NBAPlayerPage.player_name).text.split('\n')
        stats_list = driver.find_element(*NBAPlayerPage.player_stats_div).text.split('\n')[:-2]
        stats_dict = dict()
        pname = player_name[0]+ " "+player_name[1]
        
        stats_dict.update( { pname : dict(zip(stats_list[::2],stats_list[1::2])) })
        print(stats_dict)
        return stats_dict
    


    def verify_player_details_matches_leader_tables(self,top):
        '''
        '''
        print(f"top : {top}")
        player_details = self.get_leaders_details(top)
        error_count = []
        for player in player_details:
            for playerName,data in player.items():
                print(playerName)
                tdict = self.get_player_details_from_player_page(data['PlayerUrl'])
                print(tdict[playerName].items(),data.items())
               
                ## continue if assertion error so that we can find all the inconsistent 
                ## players with diff values
                try:
                    assert tdict[playerName].items() <=  data.items()
                except Exception:
                    error_count.append(f" data mismatch {tdict[playerName]} NOT MATCHES {data}")

        if len(error_count):
            print("----- assertion error -----------")
            print(error_count)
            raise AssertionError