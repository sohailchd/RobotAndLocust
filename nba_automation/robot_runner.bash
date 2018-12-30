root_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

export PYTHONPATH=$PYTHONPATH:$root_dir:$root_dir/locators:$root_dir/tests:/$root_dir/page_objects:$root_dir/reports:$root_dir/utilities:$root_dir/res_files

python -m robot.run   --outputdir=$root_dir/reports  --listener=$root_dir/utilities/CustomListener.py    \
$root_dir/tests/test_nba_leaders.robot  \
$root_dir/tests/test_nba_players.robot   \
$root_dir/tests/test_nba_standings.robot  \