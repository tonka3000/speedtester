#!/usr/bin/env python
import os, argparse
from app.speed import getDownloadSpeed
from app.conv import convertToHtml
from app.configuration import getConfigValue
from datetime import datetime

# pylint: disable=C0103

__dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='speedtester')
    parser.add_argument('--no-speedtest', help='skip the speedtest', action='store_true')
    parser.add_argument('--no-html', help='skip the html generation', action='store_true')
    args = parser.parse_args()

    data_directory = os.path.abspath(getConfigValue("data_directory"))
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)

    if not args.no_speedtest:
        print("measure speed")
        logfile = os.path.join(data_directory, "log.txt")

        now = datetime.now()
        ts = now.strftime("%Y-%m-%d_%H-%M-%S")

        ts = str(now)
        download_speed, upload_speed = getDownloadSpeed()
        end = datetime.now()
        duration = end - now
        print("download speed: " + str(download_speed))
        print("upload speed: " + str(upload_speed))

        with open(logfile, "a") as f:
            f.write(download_speed + ":" + upload_speed + "\t" + ts + "\t" + str(duration) + "\n")

    if not args.no_html:
        print("convert log to html")
        convertToHtml()
