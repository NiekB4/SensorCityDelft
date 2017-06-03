from machine import UART, Pin
import time

class PMS5003():
    def __init__(self, enable=None, reset=None):
        """ TXD: P9  4e poort
            RXD: P10  3e poort
        """
        self.port = UART(1, 9600, parity=None, stop=1, pins=('P9', 'P10'))

    def receive_one(self):
        set_pin = Pin('P4', mode=Pin.OUT)  # was P11
        print('...................  Start  ...................')
        time.sleep(1)
        print('Starting fan..... wait 20 seconds.....')
        set_pin.value(1)
        time.sleep(20)
        print('Reading value.....')
        d1 = self.port.read(1)
        d2 = self.port.read(2)
        d3 = self.port.read(3)
        d4 = self.port.read(4)
        d5 = self.port.read(5)
        d6 = self.port.read(6)
        d100 = self.port.read(134)
        d = self.port.read()
        time.sleep(2)
        print('Value d1: ', d1)
        time.sleep(1)
        print('Value d2: ', d2)
        time.sleep(1)
        print('Value d3: ', d3)
        time.sleep(1)
        print('Value d4: ', d4)
        time.sleep(1)
        print('Value d5: ', d5)
        time.sleep(1)
        print('Value d6: ', d6)
        time.sleep(1)
        print('Value d100: ', d100)
        time.sleep(1)
        print('The whole data output: ', d)
        time.sleep(1)
        L = []
        for y in d:
            L.append(y)
        #    print('Character in List: ', y)
        print('Number of bytes in the data output: ', len(L))
        time.sleep(1)
        set_pin.value(0)
        print('...................  Finished!  ...................')


pms = PMS5003()
pms.receive_one()
time.sleep(5)
#pms.receive_one()
#time.sleep(5)
#pms.receive_one()
#time.sleep(5)
#pms.receive_one()
#time.sleep(5)

#set_pin = Pin('P11', mode=Pin.OUT)
#set_pin.value(1)
#time.sleep(5)
#set_pin.value(0)
#time.sleep(5)
#set_pin.value(1)
#print('On')
#time.sleep(5)
#set_pin.value(0)
#print('Off')
