"""
Micropython library for PMS5003
by Rob Braggaar
"""
import time
import struct
from machine import UART, Pin


class PMS5003():
    def __init__(self, sleep='P11', reset='P8'):
        """
            Lopy     :: PMS
            TXD: P9  :: RXD: P4
            RXD: P10 :: TXD: P5
            SET: P11 :: SET: P3
            RESET: P12 :: RESET: P6                          # should be P8
        """
        self.STARTUP_TIME = 30  # startup time                                      # DONE
        self.port = UART(1, baudrate=9600, parity=None, stop=1, pins=('P3', 'P4'))
        self.set_pin = Pin(sleep, mode=Pin.OUT)                                     # DONE
        self.reset_pin = Pin(reset, mode=Pin.OUT)                                   # DONE

        self.set_pin.value(0)  # start powered off
        self.reset_pin.value(1)  # pull low and high for reset

    def set_pms(self):                                                              # DONE
        print("PMS: set")                                                           # DONE
        self.set_pin.value(0)                                                       # DONE
        time.sleep(self.STARTUP_TIME)                                               # DONE

    def reset_pms(self):                                                            # DONE
        print("PMS: reset")                                                         # DONE
        self.reset_pin.value(0)                                                     # DONE
        time.sleep_ms(50)                                                           # DONE
        self.reset_pin.value(1)                                                     # DONE

    def sleep(self):                                                                # DONE
        print("PMS: sleep")                                                         # DONE
        self.set_pin.value(0)                                                       # DONE

##########################################################################################

    def packet_from_data(self, data):
        numbers = struct.unpack('>16H', data)
        csum = sum(data[:-2])
        if csum != numbers[-1]:
            print("Bad packet data: %s / %s", data, csum)
            return None
        return numbers[2:-2]

    def read_pms(self):
        c = self.port.read(1)
        print('Result of read_pms: ', c)
    #    if c != '\x42':
    #        self.read_pms()

        c = self.port.read(1)
        print(c)
    #    if c != '\x4d':
    #        self.read_pms()

        data = bytearray((0x42, 0x4d))
        print('data:', len(data), '\n', data)

        data += self.port.read(30)
        print('data:', len(data), '\n', data)

    #    if len(data) != 32:
    #        self.read_pms()

        measurements = self.packet_from_data(data)
        if measurements == None:
            print("PMS: read failed")
        else:
            return measurements

def start():
    pms = PMS5003()
    pms.set_pms()
    print(pms.read_pms())
