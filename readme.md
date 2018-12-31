## Toptal Projects

*   **NBA Automation (nba_automation)** Automates the  https://stats.nba.com/players/traditional/  using robot and selenium
*   **Football-data org (rest_api)** Tests the API provided by football-data.org
*   **Load Testing (load_test)** Tests load on homepage with 1000 users vising in sapn of in 15sec



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


**res_api** : Testing the endpoint API from [FootBall Org](https://www.football-data.org/)   



### Prerequisites
All the solutions can be run on windows and linux (docker suport for linux).    
For running on **windows** make sure following are installed :  
1. Latest firefox and chrome browsers.
2. python3 and pip.

For running on **Ubuntu 18.04** make sure following are installed :  
1. Latest firefox and chrome browsers.
2. python3 and pip.

### **Installing python modules**
For setting up on **windows/ubuntu** follow the below steps :  
```
> git clone https://git.toptal.com/milorad/basar-sohail-chowdhury.git
> cd to project root i.e. basar-sohail-chowdhury
> pip install -r requirements.txt
```


## Running the tests

```
**nba_automation** 
```
For windows,
> nba_automation\execute_tests.bat
For linux,

```

**rest_api**
```
For running pytest version of tests :
> rest_api\pytest_api\execute_api.bat    

For running robot version of tests : 
> rest_api\robot_api\execute_robot_tests.bat 
```


## Deployment

**Jenkins**
Project can be easily integrated with Jenkins (CI)

**Docker**



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
