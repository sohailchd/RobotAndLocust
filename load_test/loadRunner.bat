

set root_dir=%~dp0

set PYTHONPATH=%PYTHONPATH%;%root_dir%;%root_dir%locustfiles;
del %root_dir%reports\*.csv
del %root_dir%reports\*.log


C:\Python\Scripts\locust.exe -f  %root_dir%locustfiles\Locust_footBallOrg.py --no-web -c 1000 -r 67 --run-time 15sec --print-stats --only-summary ^
--csv=%root_dir%reports\locust_report  --logfile %root_dir%reports\locust_log.log