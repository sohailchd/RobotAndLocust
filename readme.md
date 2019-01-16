# Projects 

*   **NBA Automation (nba_automation)** Automates the  https://stats.nba.com/players/traditional/ 
*   **Football-data org (rest_api)** Tests the API provided by football-data.org
*   **Load Testing (load_test)** Load test on the hompage of on homepage of football-data.org

Link to all the implemeted test cases [Tests](https://github.com/sohailchd/RobotAndLocust.git/blob/master/testcases.md)


## Getting Started

This project consist of three solutions.  
* load_test
* nba_automation
* rest_api


**load_test** 

Load testing script for simulating 1000 users visiting the homepage in 15sec.      
This solution uses [Locust](https://locust.io/) for simulating the load. Rather than using      
threads, Locust uses coroutines which makes it more scalable to be used from a      
single machine. Lucust is based on [gevents](http://www.gevent.org/)      



**nba_atomation**  
Test the statistics on nba.com.  
Automation is built using robotframework, python and selenium. Tests can be executed on windows and linux.  
> 
            .nba_automation
                ├── locators                     # all the selenium page locators     
                ├── page_objects                 # python page objects    
                ├── reports                      # robot reports     
                ├── res_files                    # keyword resoucres    
                ├── tests                        # Actual tests  
                ├── utilities                    # framework utilities, BrowserManager and Custom robot listeners   
                   └── drivers                   # contains win,linux driver for firerefox and chrome
                └── conf.py                      # global vars     
                └── execute_tests.bat            # windows test runner     
                └── robot_runner.sh              # linux test runner   
                └── test_setup.json              # defines automation settings    




**res_api** : Testing the endpoint API from [FootBall Org](https://www.football-data.org/)     
There are 2 different verions of the same tests as mentioned below.   

>
            .rest_api
                ├── pytest_api                   # pytest version of tests (10 tests)    
                    ├── py_reports               # pytest reports     
                    ..
                    ├── execute_api.bat          # runs the tests on windows     
                    ├── pytest_api.sh            # runs the tests on linux    
                    ├── test_pytest.py           # actual tests      
                ├── robot_api                    # robot version of tests (5 tests, can be easily extend to cover more)      
                    ├── res                      # res files for data driver keyword    
                    ├── robot_reports            # final report   
                    ├── test_src                 # keyword implementation   
                    ├── test                     # actual tests   
                    ├── execute....bat           # command to execute tests in windows    
                    ├── robot.....sh             # command to execute tests in linux   




## **Prerequisites**
All the solutions can be run on windows and linux (docker suport for linux).    
For running on **windows** make sure following are installed :  
1. Latest firefox and chrome browsers.
2. python3 and pip.

For running on **Ubuntu 18.04** make sure following are installed :  
1. Latest firefox and chrome browsers.
2. python3 and pip.


## **Installing python modules**
For setting up on **windows/ubuntu** follow the below steps :  
>
    $ git clone https://github.com/sohailchd/RobotAndLocust.git     
    $ cd basar-sohail-chowdhury     
    $ pip install -r requirements.txt     



# Running the tests

### **load_test**
For windows:
>    
    $ load_test\loadRunner.bat                    ## Please find all the reports in the "reports" folder

    
For Linux:  
>    
    $ load_test\load_runner.sh                    ## Please find all the reports in the "reports"

    Note: 
    - 1. reports_final conatains reports from from test run by me.
    - 2. You can change the number of users by changing batch script. Change the '-c' and '-r' value  
        c= number of users
        r= users created per sec from locust






### **nba_automation**
**For windows:**
> 
    $ nba_automation\execute_tests.bat               ## Please find all the reports in the "nba_automation/reports"
    
    If you want to run particular test cases, add robot tag.   
        Step 1: Add tag to test case  
            Test loading time for the stats segment is below specified time limit 
                [tags]     wip
                Verify the loading of the players stats segment is below "4" secs
        Step 2: Run the command with tag name
            $ nba_automation\execute_tests.bat wip

    *Note : for windows we have to manually privide the chromedriver.exe and geckodriver.exe in the 
    utilities\drivers\wins folder. Make sure drivers are named as mentioned. 


Download [ChromeDriver](https://chromedriver.storage.googleapis.com/index.html?path=2.45/)  
Download [geckodriver 64bit](https://github.com/mozilla/geckodriver/releases)


**For Linux :**
>  
    $ nba_automation\robot_runner.sh                  ## Please find all the reports in the "nba_automation/reports"

    **shell script will download the drivers automatically.

**rest_api**  
Windows:
> 
    $ rest_api\pytest_api\execute_api.bat              ### run pytest, find report in 'py_reports/football_api.html'
    $ rest_api\robot_api\execute_robot_tests.bat       ### run robot tests, find report in 'robot_reports/report.html'
 

Linux:
>  
    $ rest_api\pytest_api\execute_api.sh              ### run pytest, find report in 'py_reports/football_api.html'
    $ rest_api\robot_api\execute_robot_tests.sh       ### run robot tests, find report in 'robot_reports/report.html'
 



## Deployment
     
**Jenkins**    
All the windows version of script has been ported on Jenkins.  
Please find the jobs configuration files in the 'jenkins_jobs' folder. 
You have to import the jobs in your Jenkins server. 

> 
    1. Make sure 'Test Result Analyzer' and 'Robot Results' plugins are installed in Jenkins.
    2. All the jobs are parameterized with "root_dir". Please sepecify the root of the test project.      
    For more information please drop me an email at sohail.chd0202@gmail.com.    



# Docker  

All the three projects can be run on docker. Project has been tested on Ubuntu 18.04.  


**load_test**  
>
    $ cd basar-sohail-chowdhury/load_test
    $ sudo docker build . -t load_test
    $ sudo docker run -v ${PWD}/reports:/usr/src/load_test/reports -entrypoint="/bin/bash" -i load_test

    Please find the reports in 'reports folder'. You should be able to see logs in the console.

**rest_api**

> 
    $ cd basar-sohail-chowdhury/rest_api
    $ sudo docker build . -t rest_api_pytest
    $ sudo docker run -v ${PWD}/pytest_api/py_reports:/usr/src/rest_api/pytest_api/py_reports -entrypoint="/bin/bash" -i rest_api_pytest

**nba_automation**
>
    $ cd basar-sohail-chowdhury/nba_automation
    $ sudo docker build . -t nba_test
    $ sudo docker run -v ${PWD}/reports:/usr/src/app/reports  -entrypoint="/bin/bash" -i nba_test  headless

    ## Please find all the reports in the "nba_automation/reports" of the host system.  
    
    *Note:  Only chrome browser has been tested in docker, for using firefox change the test_setup.json   
        build the image and run.


## Built With

* [Robotframework](http://robotframework.org/) - The BDD framework
* [Requests](http://docs.python-requests.org/en/master/) - HTTP library
* [Selenium](https://www.seleniumhq.org/) - Browser automation framework
* [Locust](https://locust.io/)

## Authors

* **Basar Sohail** - *Github* - [sohailchd](https://github.com/sohailchd)

## License

This project is licensed under the MIT License.

## Acknowledgments

* NBA stats
* football-dataorg
