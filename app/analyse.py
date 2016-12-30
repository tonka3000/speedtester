import os, sys
from datetime import date,datetime
import config

# pylint: disable=C0103

infile = os.path.join(config.data_directory, "log.txt")

def readdata():
    '''
    parse log.txt file and return speed and timestamp list
    '''
    speed = []
    ts = []
    with open(infile, 'r') as f:
        for line in f:
            l = line.strip()
            splits = l.split("\t")

            speedtext = splits[0].lower()
            if "mbit/s" in speedtext:
                speedtext = speedtext.replace("mbit/s", "").strip()
                s = float(speedtext)
                speed.append(s)

                date_string = splits[1]
                date_format = "%Y-%m-%d %H:%M:%S.%f"
                t = datetime.strptime(date_string, date_format)
                ts.append(t)
            else:
                continue
    return speed, ts
