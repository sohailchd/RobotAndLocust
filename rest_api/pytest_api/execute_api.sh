#!/bin/bash

root_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

python -m pytest --capture=sys -m all --html=$root_dir/py_reports/football_api.html --self-contained-html --junit-xml=$root_dir/py_reports/xml_report.xml  
