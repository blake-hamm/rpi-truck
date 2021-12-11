# rpi-truck
Project to track odb2 data from vehicle, stream with faust fork into postgresql db and vizualize in plotly/flask app in web browser.

Using this framework in order to read odb2 data: https://github.com/brendan-w/python-OBD .

Goals:
1) Stream faster by using faust (real time to rpi display)
2) Use web application instead of built in gui
    a) Raspbian lite installed with script to automatically open chromium web browser with application address
    b) Idea is to have other applications running in browser that you can switch between (version of open auto in web app?)
4) Build postgresql db on raspberry pi and maintain public copy for analytics/machine learning (kaggle?)
5) Use Apache Airflow to monitor faust ETL and load to public cloud (might be overkill - could host different server on local network for this)

Requirements:
 - Apche kafka (https://kafka.apache.org/quickstart)
 - Faust Fork (https://github.com/faust-streaming/faust)

Other useful resource:
 - https://www.scangauge.com/x-gauge-commands/7-3l-diesel/
 - https://www.focusrs.org/threads/torque-pro-pid-list.122101/
 - https://drive.google.com/file/d/1-reGLDtccUiqTIXefZa0n9J5rOWT53kU/view
 - https://www.ford-trucks.com/forums/1523900-2018-powerstroke-pids.html#post17722775
 - https://www.ford-trucks.com/forums/1322804-torque-pro-ford-6-7l-extended-pids.html