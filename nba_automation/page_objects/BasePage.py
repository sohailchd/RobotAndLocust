from utilities.BrowserManager import BrowserManager
import conf
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class BasePage():


    _driver =  BrowserManager.get_browser()
   
    def __init__(self,url=conf.base_url):
        print("base_page init called...")
        self.page_url = url
        BasePage._driver.get(self.page_url)
        
    
    def open_page(self,url=None):
        if not url:
            self._driver.get(self.page_url)
        else:
            self._driver.get(url)


    def get_page_url(self):
        return self.page_url
        
    
    def explicit_wait(self,locator,time=15):
        ''' 
           custom wait for given element
        '''
       
        print(f"locator : {locator}")
        target = WebDriverWait(self._driver,time).until(
            EC.presence_of_element_located(locator)
        )
        print(f"exlicit wait, found element {target} ")
        

    
## module level driver instance
driver = BasePage._driver