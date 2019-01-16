from utilities.BrowserManager import BrowserManager
import conf
import sys
from robot.api import logger

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities




class CustomUtils():
    '''
        This class contains custom utilities and function 
        commonly required by all scenarios
    '''

    @classmethod
    def verify_str_contains_numeric(self,strvalue):
        '''
            Verifies if the given string contains only numric 
            values.
            We can try to covert the string in numric value
            if exception is raised we can verify that 
            given str is not numeric
        '''
        is_numeric = None
        try:
            float(strvalue)
            is_numeric = True
        except:
            print("given str is not numeric")
            is_numeric = False
        
        return is_numeric
    

    @classmethod
    def refresh_page(self):
        '''
            Refreshes the page
        '''
        print(f"Page refresh called on : {BrowserManager.get_browser().current_url}")
        BrowserManager.get_browser().refresh()

    @classmethod
    def take_screenshot(self,fname,dir=conf.report_dir_fs):
        '''
        '''
        fileName = conf.report_dir_fs + fname
        BrowserManager.get_browser().get_screenshot_as_file(fileName)
    

    @classmethod
    def embed_screenshot(self,imgSrc=None,test_name=None):
        logger.warn(f'<a href="{imgSrc}"> Failed screenshot for {test_name} </a>', html=True)
    

    @classmethod
    def custom_browser_for_load_verifier(self,base_url=conf.base_url):
        '''
            return a custom browser for verifying the load time of elements 
            on page
        '''
        if conf.default_browser.upper() == "FIREFOX":
                    try:
                        print(f" firefox : {conf.firefox_driver_path}\n")
                        caps = DesiredCapabilities.FIREFOX
                        caps["pageLoadStrategy"] = "eager" 

                        driver = webdriver.Firefox(executable_path=conf.firefox_driver_path,desired_capabilities=caps) 
                        print(f"driver session id :  {driver.session_id}")
                        ## implicit wait for 15secs
                        driver.implicitly_wait(conf.IMPLICIT_WAIT)
                        if conf.MODE.upper() == "HEADLESS":
                            driver.set_window_position(0, 0)
                            driver.set_window_size(*conf.DEFAULT_WINDOW_SIZE)

                        driver.maximize_window()
                        driver.get(base_url)
                        return driver
                        
                    except Exception as e:
                        print(f"[CUSTOM] browser initialization failed with error : {e}")
                        sys.exit

        elif conf.default_browser.upper() == "CHROME":
                    
                    print(f" chrome : {conf.chrome_driver_path}\n")
                    try:
                        chrome_options = Options()
                        if conf.MODE.upper() == 'HEADLESS':
                            chrome_options.add_argument('--headless')
                            chrome_options.add_argument('--no-sandbox')
                            chrome_options.add_argument("--disable-gpu")

                        chrome_options.add_argument("--disable-extensions")
                        chrome_options.add_argument("disable-infobars")
                        cap = DesiredCapabilities.CHROME
                        # cap['pageLoadStrategy'] = "eager"

                        driver = webdriver.Chrome(executable_path=conf.chrome_driver_path,
                                chrome_options=chrome_options,desired_capabilities=cap) 

                        print(f"driver session id :  {driver.session_id}")
                        ## implicit wait for 15secs
                        driver.implicitly_wait(conf.IMPLICIT_WAIT)
                        driver.set_window_position(0, 0)

                        if conf.MODE.upper() == "HEADLESS":
                            driver.set_window_position(0, 0)
                            driver.set_window_size(*conf.DEFAULT_WINDOW_SIZE)

                        driver.maximize_window()
                        driver.get(base_url)
                        return driver

                    except Exception as e:
                        print(f"Browser initialization failed with error : {e}")
                        sys.exit 
        