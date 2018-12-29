set root_dir=%~dp0
echo "Starting nba_automation, make sure you have installed drivers for firefox and chrome"
echo "For choosing browser, change the settings at 'test_setup.json file'"

del %root_dir%reports\failed_screenshots\*.png
del %root_dir%reports\failed_screenshots\*.jpg
del %root_dir%reports\*.xml
del %root_dir%reports\*.html


set PYTHONPATH=%PYTHONPATH%;%root_dir%;%root_dir%\locators;%root_dir%\res_files;%root_dir%\page_objects;^
%root_dir%\utilities;%root_dir%\utilities\drivers;%root_dir%\tests;%root_dir%test_setup.json;%root_dir%\conf.py


C:\python\python.exe -m robot.run   --outputdir=%root_dir%reports  --listener=%root_dir%utilities\CustomListener.py    ^
%root_dir%tests\test_nba_leaders.robot   ^
%root_dir%tests\test_nba_players.robot   ^
%root_dir%tests\test_nba_standings.robot 
 