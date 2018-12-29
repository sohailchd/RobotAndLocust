set root_dir=%~dp0

set PYTHONPATH=%PYTHONPATH%;%root_dir%;%root_dir%test_src;%root_dir%res

del %root_dir%robot_reports\*.xml
del %root_dir%robot_reports\*.html

C:\python\python.exe -m  robot.run   --outputdir=%root_dir%robot_reports  %root_dir%tests