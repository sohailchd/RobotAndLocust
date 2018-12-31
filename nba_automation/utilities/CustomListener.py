from utilities.BrowserManager import BrowserManager
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.Screenshot import Screenshot
import conf
from utilities.CustomUtils import CustomUtils
from robot.api import logger

class CustomListener(object):
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    ROBOT_LISTENER_API_VERSION = 2
    

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
        print("init_listener called...")
        BrowserManager.initialize_browser()
        

    def start_suite(self,data, suite):
        print("start_suite listener called...")
        if not BrowserManager.get_browser():
            BrowserManager.initialize_browser()
        


    def end_suite(self,data, suite):
        print("end_suite listener called...")
        

    
    # def _end_suite(self, name, attrs):
    #     print('Suite %s (%s) ending.' % (name, attrs['id']))


    def log_message(self,message):
        '''
        '''
        if message['level'] == 'FAIL':
            fname = "./failed_screenshots/" +  self.test_name  + ".png"
            logger.info(f'<a href="{fname}"> <i> SCREENSHOT </i></a>', html=True)
                        



    def start_test(self,name,attributes):
        '''
            Using hooks to save the test name
            to be used other methods.
        '''
        self.test_name = name
        pass 


    def end_test(self, name, attributes):
        """ The `end test` hook """
        print(f"test ended with result : {attributes['status']} ")
        if attributes['status'] == "FAIL":
            CustomUtils.take_screenshot(f"{name}.png")


    def close(self):
        '''
        '''
        print("close called.........")       
        BrowserManager.teardown_suite()     