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
