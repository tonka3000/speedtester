import os
from app import analyse
from app.template import render_template
from datetime import datetime
import config

# pylint: disable=C0103

__dir = os.path.dirname(os.path.abspath(__file__))

def convertToHtml():
    '''
    convert the log.txt file to html files
    '''
    output_directory = os.path.abspath(config.html_directory)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    speeds, upload_speeds, ts = analyse.readdata()
    speed_len = len(speeds)

    day_data = {}
    for i in range(speed_len):
        speed = speeds[i]
        upload_speed = upload_speeds[i]
        t = ts[i]
        day_string = datetime.strftime(t, "%Y-%m-%d")
        if day_string not in day_data.keys():
            day_data[day_string] = {}
            day_data[day_string]["speeds"] = []
            day_data[day_string]["ts"] = []
            day_data[day_string]["upload_speeds"] = []

        day_data[day_string]["speeds"].append(speed)
        day_data[day_string]["ts"].append(datetime.strftime(t, "%Y-%m-%d %H:%M:%S"))
        day_data[day_string]["upload_speeds"].append(upload_speed)

    days = []
    for day_string in sorted(day_data.keys()):
        day = day_data[day_string]
        speeds = day["speeds"]
        upload_speeds = day["upload_speeds"]

        templateVars = {
            "ts" : day["ts"],
            "download_speeds" : speeds,
            "upload_speeds" : upload_speeds,
            "title" : day_string
        }

        with open(os.path.join(output_directory, day_string + ".htm"), 'w') as f:
            f.write(render_template("day.html", templateVars))

        days.append({
            "day" : day_string,
            "download_speed" : sum(speeds) / len(speeds),
            "upload_speed" : sum(upload_speeds) / len(upload_speeds)
        })

    with open(os.path.join(output_directory, "index.htm"), 'w') as f:
        f.write(render_template("index.html", variables={
            "days" : reversed(days),
            "title" : config.title
            }))
