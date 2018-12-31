import json
import os
from time import sleep

import robot
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import conf
from selenium.webdriver.chrome.options import Options


present_dir = conf.present_dir
print(f"present_dir : {present_dir}")
if os.name == 'nt':
    print("platform : WIN")
    firefox_driver_path = os.path.join(present_dir,'utilities/drivers/win/geckodriver.exe')
    chrome_driver_path = os.path.join(present_dir,'utilities/drivers/win/chromedriver.exe')  ## path to the chrome driver
elif os.name == 'posix':
    print("platform : LINUX")
    firefox_driver_path = os.path.join(present_dir,'utilities/drivers/linux/geckodriver')
    chrome_driver_path = os.path.join(present_dir,'utilities/drivers/linux/chromedriver')

safari_driver_path = ""  ## path to the safari driver


BASE_URL = conf.base_url
DEFAULT_BROWSER = conf.default_browser



class BrowserManager():
   
            @classmethod
            def initialize_browser(cls):
                    '''
                        Creates browser of specified types 
                        param: browser_type
                        return: cls.driver
                    ''' 
                    base_url = BASE_URL 
                    browser_type = DEFAULT_BROWSER
                    print(f"base_url : {base_url}, browser_type: {browser_type}")
                    if not base_url:
                        raise TypeError("base_url not provided, please check if base_url is set")       
                    elif browser_type.upper() == "FIREFOX":
                        cls._initialize_firefox(base_url)
                    elif browser_type.upper() == "CHROME":
                        cls._initialize_chrome(base_url)
                    elif browser_type.upper() == "SAFARI":
                        cls._initialize_safari(base_url)
                    elif browser_type.upper() == "EDGE":
                        cls._initialize_edge(base_url)
                    else:
                        ## default is firefox
                        cls._initialize_firefox(base_url)

                    

            @classmethod
            def get_browser(cls):
                    if cls.driver:
                        return cls.driver
                    else:
                        raise TypeError("webdriver is not initialized.") 



            @classmethod
            def _initialize_firefox(cls,base_url):
                    '''
                        initialises firefox browser
                    '''
                    print(f" firefox : {firefox_driver_path}\n")
                    cls.driver = webdriver.Firefox(executable_path=firefox_driver_path) 
                    print(f"driver session id :  {cls.driver.session_id}")
                    ## implicit wait for 15secs
                    cls.driver.implicitly_wait(conf.IMPLICIT_WAIT)
                    cls.driver.maximize_window()
                    cls.driver.get(base_url)
                    sleep(3)
                    return cls.driver



            @classmethod
            def _initialize_chrome(cls,base_url):
                    '''
                        Initialises the chrome driver
                    '''
                    print(f" chrome : {chrome_driver_path}\n")
                    chrome_options = Options()
                    if conf.MODE.upper() == 'HEADLESS':
                        chrome_options.add_argument('--headless')
                        chrome_options.add_argument('--no-sandbox')
                        chrome_options.add_argument("--disable-gpu")

                    chrome_options.add_argument("--disable-extensions")
                    chrome_options.add_argument("disable-infobars")
                    
                    cls.driver = webdriver.Chrome(executable_path=chrome_driver_path,chrome_options=chrome_options) 
                    print(f"driver session id :  {cls.driver.session_id}")
                    ## implicit wait for 15secs
                    cls.driver.implicitly_wait(conf.IMPLICIT_WAIT)
                    cls.driver.maximize_window()
                    cls.driver.get(base_url)
                    sleep(3)
                    return cls.driver



            @classmethod
            def _initialize_safari(cls,base_url):
                    pass


            @classmethod
            def _initialize_edge(cls,base_url):
                    pass 

            @classmethod
            def teardown_suite(cls):
                    if cls.driver:
                        try:
                            cls.driver.close()
                            print("Browser Successfully closed.")
                        except WebDriverException:
                            print(f"")
                    else:
                        raise TypeError("No browser initailzed.")