import os, sys, subprocess
from app.configuration import getConfigValue

# pylint: disable=C0103

__dir = os.path.dirname(os.path.abspath(__file__))

speedtestcli_bin = 'speedtest-cli'
tmp = os.path.join(getConfigValue("data_directory", "./data"), "tmp.txt")

def getDownloadSpeed():
    '''
    calculate download speed and return it as a string
    '''
    with open(tmp, "w") as f:
        subprocess.call([speedtestcli_bin], stdout=f)

    download_speed = "0 MBit/s"
    upload_speed = "0 MBit/s"
    with open(tmp, "r") as f:
        downloadtext = "Download:"
        uploadtext = "Upload:"
        for line in f:
            l = line.strip()
            if l.startswith(downloadtext):
                download_speed = l[len(downloadtext):].strip()
            elif l.startswith(uploadtext):
                upload_speed = l[len(uploadtext):].strip()
    return download_speed, upload_speed
