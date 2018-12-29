
:: runs the pytest version of API tests

set root_dir=%~dp0

set PYTHONPATH=%PYTHONPATH%;%root_dir%;

del %root_dir%py_reports\*.xml
del %root_dir%py_reports\*.html


C:\python\python.exe -m pytest --capture=sys -m all --html=%root_dir%py_reports\football_api.html --self-contained-html --junit-xml=%root_dir%py_reports\xml_report.xml  
