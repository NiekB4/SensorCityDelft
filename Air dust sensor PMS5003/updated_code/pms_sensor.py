from machine import Pin, UART
import main
import time
import array
from struct import unpack

"""
Code for the PMS5003 Air Dust Sensor
Created by Niek Bebelaar

Connections:
- purple on PMS     to      Vin (5.5V) on LoPy
- orange on PMS     to      GND on LoPy
- white on PMS      to      G22 (P11) on LoPy
- green on PMS      to      G17 (P10) on LoPy
- blue on PMS       to      G16 (P9) on LoPy
- yellow on PMS     to      G15 (P8) on LoPy
no capacitors or resistors needed (P11 and P8 have 3.3 Volt logic)

After connecting the cables, call the read_data() function to read the data.

Sources:
https://github.com/rbraggaar/sensor-city-delft/blob/master/airqual_pms5003/main.py
https://gist.github.com/sorz/516f6fb8b81fcb99225a
"""
# Ports
SET_PORT = 'P11'    # LoPy SET port, communicates with the PMS SET port (P3)
TXD_PORT = 'P3'     # LoPy TXD port, communicates with PMS RXD port (P4)            # DOES NOT MATTER: is by default port 9 or 10
RXD_PORT = 'P4'    # LoPy RXD port, communicates with the PMS TXD port (P5)         # DOES NOT MATTER: is by default port 9 or 10
RESET_PORT = 'P8'   # LoPy RESET port, communicates with the PMS RESET port(P6)

STARTUP_TIME = 30    # 30 seconds of startup time (needed for ventilator). 5 is better for debugging.

set_pin = Pin(SET_PORT, mode=Pin.OUT)
reset_pin = Pin(RESET_PORT, mode=Pin.OUT)
#data_uart = UART(1, 9600, parity=None, stop=1, pins=('RXD_PORT', TXD_PORT))
data_uart2 = UART(1, baudrate=9600, parity=None, stop=1, pins=('P9', 'P10'))


def fan_on():
    print('Turning the PMS5003 fan on')  # the fan is ON by default.
    set_pin.value(1)


def fan_off():
    print('Turning the PMS5003 fan off')
    set_pin.value(0)


def reset():
    print('Resetting the PMS5003 sensor')
    reset_pin.value(1)


def set_sensor():
    print('Preparing the fan...')
    fan_on()
    print('Wait 30 seconds...')
    time.sleep(STARTUP_TIME)           # wait 30 seconds
    print('Sensor is set')


def read_data():
    set_sensor()
    print('Reading data')
    d = data_uart2
    #print('d: ', d)
    raw = d.read()
    #print('raw data: ', raw)
#    data = []
#    data += raw
#    print(type(data))
#    print(raw)
    unpacking = unpack('>16H', raw)
    #print('all unpacked data: ', type(unpacking), unpacking)
    print('')
    print('big starting number:   ', unpacking[0])
    print('frame length (2*13+2): ', unpacking[1])
    print('PM1.0 concentration, standard particle: ', unpacking[2])
    print('PM2.5 concentration, standard particle: ', unpacking[3])
    print('PM10  concentration, standard particle: ', unpacking[4])
    print('PM1.0 concentration, atmospheric env:   ', unpacking[5])
    print('PM2.5 concentration, atmospheric env:   ', unpacking[6])
    print('PM10  concentration, atmospheric env:   ', unpacking[7])
    print('Data 7:  ', unpacking[8])
    print('Data 8:  ', unpacking[9])
    print('Data 9:  ', unpacking[10])
    print('Data 10: ', unpacking[11])
    print('Data 11: ', unpacking[12])
    print('Data 12: ', unpacking[13])
    print('Data 13 (reserved):', unpacking[14])
    print('Check code:        ', unpacking[15])
    print('')
    fan_off()
    print('Finished!')



#    n = 1
#    for d in data:
#        print(n, ': ', d)
#        n += 1
#    if(len(data)) == 255:
#        print('kaas')
#    else:
#        print('Raarr')
#        read_data()
#    raw2 = d.read(32)
#    data_bytearray = bytearray(32)
#    data_bytearray += d.read(32)
#    print(data_bytearray)
    #buf = array.array()
    #data_bytearray = bytearray(())

#    buf = array.array('H')
#    for i in range(0, 31):
#        buf.append(0)
    #buf = array.array(buf)
#    print(buf)
#    d.read(buf)

#    a = bytearray(b'\xc7\x14')
#    unpack


    #data = bytearray()
    #print(type(data))
    #print('data before: ', data)
    #data += d.read(32)
    #print('data after: ', data)
    #buf = array.array('0x42')
    #print(type(buf), buf)
