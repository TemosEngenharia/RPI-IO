# -*- coding: utf-8 -*-
import rrdtool
import os.path
from smbus2 import SMBusWrapper

def main():
    if check_rrd():
        temp_update()
    else:
        rrd_create()
        temp_update()

def check_rrd():
    return os.path.isfile("/var/ramdisk/var/temperature.rrd")

def rrd_create():
    ret = rrdtool.create("/var/ramdisk/var/temperature.rrd", 
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
    with SMBusWrapper(1) as bus:
        # Read a block of 16 bytes from address 80, offset 0
        block = bus.read_i2c_block_data(0x48, 0x00, 16)
        # Returned value is a list of 16 bytes
        TEMP=str(block[0] + block[1]/100.0)
    ret = rrdtool.update('/var/ramdisk/var/temperature.rrd','N:'+TEMP)
    if ret:
        print rrdtool.error()

if __name__ == '__main__':
    main()
