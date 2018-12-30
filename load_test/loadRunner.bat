

set root_dir=%~dp0

set PYTHONPATH=%PYTHONPATH%;%root_dir%;%root_dir%locustfiles;


locust -f  %root_dir%locustfiles\Locust_footBallOrg.py --no-web -c 1000 -r 67 --run-time 15sec --print-stats --only-summary