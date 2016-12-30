import os, sys, subprocess
import config

# pylint: disable=C0103

__dir = os.path.dirname(os.path.abspath(__file__))

speedtestcli_bin = 'speedtest-cli'
tmp = os.path.join(config.data_directory, "tmp.txt")

def getDownloadSpeed():
    '''
    calculate download speed and return it as a string
    '''
    with open(tmp, "w") as f:
        subprocess.call([speedtestcli_bin], stdout=f)
    with open(tmp, "r") as f:
        downloadtext = "Download:"
        for line in f:
            l = line.strip()
            if l.startswith(downloadtext):
                speedtext = l[len(downloadtext):].strip()
                return speedtext
    return "0 MBit/s"
