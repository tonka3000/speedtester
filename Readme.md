# Speedtester

This speedtester use the awesome speedtest-cli. It measure the speed and create simple html pages to make it visible via a webserver.  
This project is build for the raspberry pi, but could be used in any python environment.

This app required python 3.4 or higher

# config file
First you have to create a `config.py` file next to the toplevel `speed.py`. You can copy the `config_example.py`, which are good default settings for the raspberry pi.

# virtual environment
It's highly recommended to use an virtual environment. You could use the `virtualenv` module from `pip` or you could use the buildin virtual environment (`python -m venv venv`).

# install dependencies
`pip install -r requirements.txt`

# schedule speedtests
speedtester does not schedule the speedtests, so you have to use your own scheduler. On unix systems cron-jobs works great.  

example for the raspberry pi (speedtest every 10 minutes):
```
crontab -e
```
enter following into your crontab and save + close the file (`:wq` for vim)
```
SHELL=/bin/bash
*/10 * * * * cd /home/pi/speedtester/ && source venv/bin/activate && python speed.py > /var/www/html/speedtester_log.txt && deactivate
```