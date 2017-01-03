import os, sys
from datetime import date,datetime
import config

# pylint: disable=C0103

infile = os.path.join(config.data_directory, "log.txt")

def readdata():
    '''
    parse log.txt file and return speed and timestamp list
    '''
    download_speed = []
    upload_speeds = []
    ts = []
    with open(infile, 'r') as f:
        for line in f:
            l = line.strip()
            splits = l.split("\t")

            speedtext = splits[0].lower()
            if "mbit/s" in speedtext:
                speedsplits = speedtext.split(":")
                speedvalues = []
                for e in speedsplits:
                    speedvalues.append(float(e.replace("mbit/s", "").strip()))
                download_speed.append(speedvalues[0])
                upload_speed = 0.
                if len(speedvalues) > 1:
                    upload_speed = speedvalues[1]
                upload_speeds.append(upload_speed)

                date_string = splits[1]
                date_format = "%Y-%m-%d %H:%M:%S.%f"
                t = datetime.strptime(date_string, date_format)
                ts.append(t)
            else:
                continue
    return download_speed, upload_speeds, ts
