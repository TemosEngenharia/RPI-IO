# -*- coding: utf-8 -*-
import rrdtool
import os.path


pingAddress = '8.8.8.8'
def main():
    if check_rrd():
        temp_update()
    else:
        rrd_create()
        temp_update()

def check_rrd():
    return os.path.isfile("/var/ramdisk/var/net.rrd")

def rrd_create():
    ret = rrdtool.create("/var/ramdisk/var/net.rrd", 
                         "--step", "60", "--start", '0',
                         "DS:temp:GAUGE:120:-15:120",
                         "RRA:AVERAGE:0.5:1:60",
                         "RRA:AVERAGE:0.5:5:288",
                         "RRA:AVERAGE:0.5:10:1008",
                         "RRA:AVERAGE:0.5:30:1440",
                         "RRA:AVERAGE:0.5:60:8784")
    if ret:
        print rrdtool.error()

def temp_update():
    # Perform the ping using the system ping command (one ping only)
    rawPingFile = os.popen('ping -c 1 %s' % (pingAddress))
    rawPingData = rawPingFile.readlines()
    rawPingFile.close()
    # Extract the ping time
    if len(rawPingData) < 2:
        # Failed to find a DNS resolution or route
        failed = True
        latency = 0
    else:
        index = rawPingData[1].find('time=')
        if index == -1:
            # Ping failed or timed-out
            failed = True
            latency = 0
        else:
            # We have a ping time, isolate it and convert to a number
            failed = False
            latency = rawPingData[1][index + 5:]
            latency = latency[:latency.find(' ')]
    ret = rrdtool.update('/var/ramdisk/var/net.rrd','N:'+str(latency))
    if ret:
        print rrdtool.error()

if __name__ == '__main__':
    main()
