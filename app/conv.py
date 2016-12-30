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

    speeds, ts = analyse.readdata()
    speed_len = len(speeds)

    day_data = {}
    for i in range(speed_len):
        speed = speeds[i]
        t = ts[i]
        day_string = datetime.strftime(t, "%Y-%m-%d")
        if day_string not in day_data.keys():
            day_data[day_string] = {}
            day_data[day_string]["speeds"] = []
            day_data[day_string]["ts"] = []

        day_data[day_string]["speeds"].append(speed)
        day_data[day_string]["ts"].append(datetime.strftime(t, "%Y-%m-%d %H:%M:%S"))

    days = []
    for day_string in sorted(day_data.keys()):
        day = day_data[day_string]
        speeds = day["speeds"]

        templateVars = {
            "ts" : day["ts"],
            "speeds" : speeds,
            "title" : day_string
        }

        with open(os.path.join(output_directory, day_string + ".htm"), 'w') as f:
            f.write(render_template("day.html", templateVars))

        days.append({
            "day" : day_string,
            "speed" : sum(speeds) / len(speeds)
        })

    with open(os.path.join(output_directory, "index.htm"), 'w') as f:
        f.write(render_template("index.html", variables={
            "days" : reversed(days),
            "title" : config.title
            }))
