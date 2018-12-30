root_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

export PYTHONPATH=$PYTHONPATH:$root_dir:$root_dir/res:$root_dir/test_src:$root_dir/tests

python -m robot.run --outputdir=$root_dir/robot_reports  $root_dir/tests