from locust import Locust,TaskSet,task, HttpLocust , TaskSequence, seq_task
import sys, os 

sys.path.append(os.getcwd())
from common import conf 
import locust.stats
import datetime

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
    def without_login_homepage(self):
        response = self.client.get(conf.base_url)
        try:
            assert response.elapsed < datetime.timedelta(seconds = 3), "Request took more than 1 second"
        except:
            print("request took more than 3secs to load.")


    @task(5)
    class LoginFlow(TaskSequence):

            @seq_task(2)
            def visiting_api_page(self):
                response = self.client.get(conf.api_url)
                print(f"Response status code : {response.status_code}")
                print(f"Response header : {response.headers}")


            @seq_task(1)
            def user_login(self):
                response = self.client.post(conf.login_url, {'email' : conf.user_email, "password" : conf.auth_token})
                print(f"login response status code : {response.status_code}")
                assert response.headers['Connection'] == 'keep-alive', "Unexpected connection header: " + response.headers['Connection']



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
