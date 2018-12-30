from locust import Locust,TaskSet,task, HttpLocust
import sys, os 
sys.path.append(os.getcwd())
from common import conf 
import locust.stats
import logging


locust.stats.CSV_STATS_INTERVAL_SEC = 1


class TaskSetOne(TaskSet):
    '''
        Defines associated behaviours for a particular user/locust
        * NOT USED IN THIS TEST
    '''

    @task(10)
    def home(self):
        '''
            Simulates user visiting home page
            url : https://www.football-data.org/
        '''
        with self.client.get('/',catch_response=True) as response:
            print(f"response content : {response.content}")
            print(f"response : {response}")
    

    @task(4)
    def api_documentation(self):
        '''
            Simulates user visiting the api documentation page
            url : https://www.football-data.org/documentation/quickstart
        '''
        with self.client.get('/documentation/quickstart',catch_response=True) as response:
            print(f"response content : {response.content}")
            print(f"response : {response}")



class VistHomePageTask(TaskSet):
    '''
        Simulates login and visit homepage
    '''

    @task(10)
    def visiting_home_page(self):
        response = self.client.get(conf.base_url)
        # print(f"Response status code : {response.status_code}")
        # print(f"Response content : {response.content}")


    @task(7)
    def user_login(self):
        res = self.client.post(conf.login_url, {'email' : conf.user_email, "password" : conf.auth_token})
        # print(res.text)




class LoadFootballOrg(HttpLocust):
    '''
        This class helps in making HTTPS calls
        when using this class, each instance gets 'client' attribute for 
        making http calls
    ''' 
    task_set = VistHomePageTask
    host = conf.base_url
    min_wait = 500    ## min wait for 0.5 secs
    max_wait = 4000   ## max wait for 4 secs 
