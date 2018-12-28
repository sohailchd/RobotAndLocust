from utilities.BrowserManager import BrowserManager
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.Screenshot import Screenshot
import conf

class PythonLibraryAsListenerItself(object):
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    ROBOT_LISTENER_API_VERSION = 3


    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
        print("init_listener called...")
        BrowserManager.initialize_browser()
        self.screenShot = Screenshot(screenshot_directory=conf.report_dir,screenshot_module='wxPython')

    def start_suite(self,data, suite):
        print("start_suite listener called...")
        

    def end_suite(self,data, suite):
        print("end_suite listener called...")
        BrowserManager.teardown_suite()

    
    # def _end_suite(self, name, attrs):
    #     print('Suite %s (%s) ending.' % (name, attrs['id']))


    def start_test(self,data,result):
        pass 

    def end_test(self, data, result):
        """ The `end test` hook """
        print(f"test ended with result : {result.status} ")
        if result.status == "FAIL":
            self.screenShot.take_screenshot()
