
import json 
import os

present_dir = os.path.dirname(os.path.realpath(__file__))
report_dir_fs  = os.path.join(present_dir,'reports/failed_screenshots/')
report_dir  = os.path.join(present_dir,'reports/failed_screenshots/')

##  load the settings file
setting_file_path = os.path.join(present_dir,'test_setup.json')
settings_file = open(setting_file_path)
settings = json.load(settings_file)['test_configurations']

print(settings)
base_url = settings['base_url']
default_browser = settings['browser']

IMPLICIT_WAIT = 15
MODE = settings['mode']