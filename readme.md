# Toptal Projects 

*   **NBA Automation (nba_automation)** Automates the  https://stats.nba.com/players/traditional/ 
*   **Football-data org (rest_api)** Tests the API provided by football-data.org
*   **Load Testing (load_test)** Load test on the hompage of on homepage of football-data.org

Link to all the implemeted test cases [Tests](https://git.toptal.com/milorad/basar-sohail-chowdhury/blob/master/testcases.md)


## Getting Started

This project consist of three solutions.  
* load_test
* nba_automation
* rest_api


**load_test** 

Load testing script for simulating 1000 users visiting the homepage in 15sec.  
This solution uses [Locust](https://locust.io/) for simulating the load. Rather than using
threads, Locust uses coroutines which makes it more scalable to be used from a   
single machine. Lucust is based in [gevents](http://www.gevent.org/)  



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
    $ git clone https://git.toptal.com/milorad/basar-sohail-chowdhury.git     
    $ cd basar-sohail-chowdhury     
    $ pip install -r requirements.txt     



## Running the tests

### **load_test**
For windows:
>    
    $ load_test\loadRunner.bat   

    
For Linux:  
>    
    $ load_test\load_runner.sh  



### **nba_automation**

For windows:
> 
    $ nba_automation\execute_tests.bat    


For Linux :
>  
    $ nba_automation\robot_runner.sh    


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
All the windows version jobs has been ported on Jenkins.  
Please find the jobs configuration files in the 'jenkins_jobs' folder. 
You have to import the jobs in your Jenkins server. 

> 
    1. Make sure 'Test Result Analyzer' and 'Robot Results' plugins are installed in Jenkins.
    2. All the jobs are parameterized with "root_dir". Please sepecify the root of the test project.   
    For more information please drop me an email at sohail.chd0202@gmail.com.    
 
## Docker

**load_test**  
>
    $ cd basar-sohail-chowdhury/load_test
    $ sudo docker build . -t load_test
    $ sudo docker run -v ${PWD}/reports:/usr/src/app/reports -entrypoint="/bin/bash" -i load_test

    Pleas find the reports in 'reports folder'. You should be able to see logs in the console.

**rest_api**

> 
    $ cd basar-sohail-chowdhury/rest_api
    $ sudo docker build . -t rest_api_pytest
    $ sudo docker run -v ${PWD}/pytest_api/py_reports:/usr/src/pytest_api/py_reports -entrypoint="/bin/bash" -i rest_api_pytest





## Built With

* [Robotframework](http://robotframework.org/) - The BDD framework
* [Requests](http://docs.python-requests.org/en/master/) - HTTP library
* [Selenium](https://www.seleniumhq.org/) - Browser automation framework


## Authors

* **Basar Sohail** - *Github* - [sohailchd](https://github.com/sohailchd)

## License

This project is licensed under the MIT License.

## Acknowledgments

* Toptal
* NBA stats
* football-data.org
