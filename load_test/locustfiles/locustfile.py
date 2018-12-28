from locust import HttpLocust, TaskSet, task
from pyquery import PyQuery
import random

class UserBehaviour(TaskSet):
    urls_from_page = []

    def on_start(self):
        # on starting, we will login and get session then 
        # we wil be able to send request to login required page "/my-account"
        self.client.post("/", {"email": "test@testrisk.com", "password": "Passw0rd"})  
        request = self.client.get("/my-account")
        print(request)
        # from content of the page, we will take all links and then store them to a variable 
        pq = PyQuery(request.content)

        # PyQuery can optain data from the page by jQuery
        link_elements = pq(".link > a")
        for url in link_elements:
            self.urls_from_page.append(url.attrib["href"])

    @task
    def load_page(self):
        # this is a task to run performance testing
        # we will send http request the url taken from "my-account" page
        try:
            url = random.choice(self.urls_from_page)
            self.client.get(url)
        except IndexError:
            print("... something wrong check, pq!")
            pass


class User(HttpLocust):
    host = "http://www.myhabit.com"
    task_set = UserBehaviour
    
    # stop the test after 120 seconds
    stop_timeout = 120 

    # time for user behaviour
    # we can assume that they wait 0.5 to 6 seconds on a page
    min_wait = 500
    max_wait = 6000