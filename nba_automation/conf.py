
import json 
import os

present_dir = os.getcwd()
report_dir  = os.path.join(present_dir,'nba_automation/reports/failed_screenshots/')

##  load the settings file
setting_file_path = os.path.join(present_dir,'nba_automation/test_setup.json')
settings_file = open(setting_file_path)
settings = json.load(settings_file)['test_configurations']

print(settings)
base_url = settings['base_url']
default_browser = settings['browser']