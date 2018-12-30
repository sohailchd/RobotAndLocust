#!/bin/bash

echo "Locust load test started...."


echo "Setting root dir"
root_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo "root_dir : "$root_dir" "

export PYTHONPATH=$PYTHONPATH:$root_dir:$root_dir/common:$root_dir/locustfiles:$root_dir/reports

echo "starting locust..."
locust -f  $root_dir/locustfiles/Locust_footBallOrg.py --no-web -c 1000 -r 67 --run-time 15sec --print-stats --only-summary \
--csv=$root_dir/reports/locust_report  --logfile=$root_dir/reports/locustfile.log