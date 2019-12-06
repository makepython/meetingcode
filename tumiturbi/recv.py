import spidev
import time
import os

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

def read_channel(channel):
    adc = spi.xfer2([1, (8+channel)<<4, 0])
    print(adc)
    data = ((adc[1]&3)<<8) + adc[2]
    return data


def convert_to_volts(data, places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts, places)
    return volts


channel = 0

while True:
    light_level = read_channel(channel)
    light_volts = convert_to_volts(light_level, 2)

    print(light_level, light_volts)

    time.sleep(5)
