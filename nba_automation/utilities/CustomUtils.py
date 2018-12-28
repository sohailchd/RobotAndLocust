from utilities.BrowserManager import BrowserManager

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

