#!/bin/bash

echo "Robot tests starting for NBA_stats  testing..."

# read -p "Press enter to continue"

root_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo "root_dir : "${root_dir}" "

chromed="$root_dir/utilities/drivers/linux/chromedriver"
geckod="$root_dir/utilities/drivers/linux/geckodriver"


if [ ! -f $chromed ]; then
    echo "chromedriver not found not found!. Trying to download"
    wget -q "https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d $root_dir/utilities/drivers/linux/   \
    && rm /tmp/chromedriver.zip \
    && ln -fs $chromed /usr/bin/chromedriver
fi
echo "chromedriver setup done."
chmod 777 $chromed



if [ ! -f $geckod ]; then
    echo "geckodriver not found not found!. Trying to download"
    wget -q "https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz" -O /tmp/geckodriver.tgz \
    && tar zxf /tmp/geckodriver.tgz -C $root_dir/utilities/drivers/linux/  \
    && rm /tmp/geckodriver.tgz \
    && ln -fs $geckod /usr/bin/geckodriver
fi
echo "geckodriver setup done. "
chmod 777 $geckod


# read -p "Press enter to continue"


# echo "starting xvfb server for display"
# Xvfb :99 -screen 0 1920x1080x16 &
# export DISPLAY=:99.0
# echo "xvfb started successfylly..."


rm -f $root_dir/reports/failed_screenshots/*.png
rm -f $root_dir/reports/*.xml
rm -f $root_dir/reports/*.log
rm -f $root_dir/reports/*.html



export PYTHONPATH=$PYTHONPATH:$root_dir:$root_dir/locators:$root_dir/tests:/$root_dir/page_objects:$root_dir/reports:$root_dir/utilities:$root_dir/res_files

python -m robot.run   --outputdir=$root_dir/reports  --listener=$root_dir/utilities/CustomListener.py    \
$root_dir/tests/test_nba_leaders.robot  \
$root_dir/tests/test_nba_players.robot   \
$root_dir/tests/test_nba_standings.robot  \