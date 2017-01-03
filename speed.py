#!/usr/bin/env python
import os
from app.speed import getDownloadSpeed
from app.conv import convertToHtml
from datetime import datetime
import config

# pylint: disable=C0103

__dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    data_directory = os.path.abspath(config.data_directory)
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)

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

    print("convert log to html")
    convertToHtml()
