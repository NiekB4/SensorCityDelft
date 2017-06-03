import time
from machine import Pin
from machine import Timer
from dth import DTH
from network import LoRa
from math import log
import socket
import binascii
import struct
import pycom
import config

"""
	SECTION LORA
"""
"""
	Setup KPN LoRa:
		Basic LoRa example based on ABP (authorization by personalization)
		Setup your KPN details in config.py
"""

# LoRa details keys obtained from KPN
dev_addr = struct.unpack(">l", binascii.unhexlify(config.DEV_ADDR))[0]
# manually converted hex to decimal for better readability
nwks_key = binascii.unhexlify(config.NWKS_KEY)
apps_key = binascii.unhexlify(config.APPS_KEY)
#print('This is the nwks_key:            ', config.NWKS_KEY)
#print('This is the nwks_key hex:        ', nwks_key)

# Setup LoRa KPN
lora = LoRa(mode=LoRa.LORAWAN, adr=True)
# join a network using ABP
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwks_key, apps_key), timeout=0)
# create a LoRa socket
lora_sock = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
# set the LoRaWAN data rate
lora_sock.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

def ack():
    """
    The blinking LED light when a LoRa message is successfully sent.
    """
    for i in range(3):
        pycom.rgbled(0x00ff00)
        time.sleep_ms(100)
        pycom.rgbled(0)
        time.sleep_ms(100)


def lora_tx(payload):
    """
    The function to use in the call when sending a LoRa message.
    """
    print('Sending uplink message')
    pycom.rgbled(0xff0000)
    lora_sock.send(payload)
    print('LoRa uplink complete')
    ack()



"""
Setup The Things Network:
"""
"""
print('Main start')
# The things network first part.
lora = LoRa(mode=LoRa.LORAWAN)
dev_eui = binascii.hexlify(lora.mac()).upper().decode('utf-8')
print('This is the dev_eui:             ', dev_eui)
"""








"""
SEND SCRIPTS (over KPN LoRa)
"""

def send(m):
	text = str(m)
	mess = binascii.unhexlify(text)
	lora_tx(mess)
	confirm = 'Message send!'
	return(confirm)
	#print(send_sensor_1())


def send_sensor_1():
    message_payload = sensor_1.temperature()   # calls sensor function from lib
    print(message_payload)
#   mess = binascii.unhexlify(message_payload) # makes hex of the message
    lora_tx(message_payload)                   # sends the message
    print(send_sensor_2())                     # calls next function


def send_sensor_2():
    message_payload = sensor_2.humidity()      # calls sensor function from lib
    print(message_payload)
#   mess = binascii.unhexlify(message_payload) # makes hex of the message
    lora_tx(message_payload)                   # sends the message
    print(send_sensor_3())                     # calls next function


def send_sensor_3():
    message_payload = sensor_3.sensor_3()      # calls sensor function from lib
    print(message_payload)
#   mess = binascii.unhexlify(message_payload) # makes hex of the message
    lora_tx(message_payload)                   # sends the message
    return('Finished the round.... print "send()" for another round!')
"""
def noise():
    playnoise = sensor_4.test()
    print(playnoise)
"""
def sendtemp(x):
    #   output = round(x,2)
    #   print(output)
    #   print(a)
    #    print(intpart)
    #    print(decpart)
    #    messageval = intpart, decpart
    #    output = ("{:1.2f}".format(x))
    #    print(output)
    #    "{0:0.1f}".format(45.34531)
    #   print('Humidity: {:3.2f}'.format(result.humidity / 1.0))
    #    print(len(output))
    #    print(type(output))
    #    output = float(output.replace(',',''))
    #    print(output)
    #    text = str(x+' ')
    #    mess = binascii.unhexlify(output)
    lora_tx(x)





"""
SENSORS SECTION::
"""

"""
	Temperature and Humidity sensor AM2302:
"""
# data pin connected to P11
# 1 for AM2302
th = DTH(Pin('P4', mode=Pin.OPEN_DRAIN), 1)
time.sleep(5)

def temp_hum():
	temperatures = []
	humidities = []
	while True:
		result = th.read()
		print(result, type(result))
		print(result.is_valid())
		# if result.is_valid():
		print("#", len(temperatures)+1)
		print('Temperature: {:3.2f}'.format(result.temperature / 1.0))
		print('Humidity: {:3.2f}'.format(result.humidity / 1.0))
		temperatures.append(result.temperature)
		humidities.append(result.humidity)
		if len(temperatures) == 10:
			sum_temp = sum(temperatures)
			avg_temp = sum_temp / 10.0
			print(" ")
			print("Summary about the last 20 seconds:")
			print(" ")
			print('The average temperature was: {:3.2f}'.format(avg_temp))
			print('The maximum temperature was: {:3.2f}'.format(max(temperatures)))
			print('The minumum temperature was: {:3.2f}'.format(min(temperatures)))
			temperatures = []
			#send(avg_temp)
			print('Message send!')
		if len(humidities) == 10:
			sum_hum = sum(humidities)
			avg_hum = sum_hum / 10.0
			print(" ")
			print('The average humidity was: {:3.2f}'.format(avg_hum))
			print('The maximum humidity was: {:3.2f}'.format(max(humidities)))
			print('The minumum humidity was: {:3.2f}'.format(min(humidities)))
			humidities = []
		time.sleep(5)


"""
	Noise sensor MAX9814:
"""

SAMPLE_WINDOW = 50  # Sample window width in ms (50 ms = 20Hz)
sample = 0

adc = machine.ADC(bits=10)             # create an ADC object
apin = adc.channel(pin='P16')   	   # create an analog pin on P16

def noise():
#	SAMPLE_WINDOW = 50  # Sample window width in ms (50 ms = 20Hz)
#	sample = 0

#	adc = machine.ADC(bits=10)             # create an ADC object
#	apin = adc.channel(pin='P16')   	   # create an analog pin on P16
	while True:
		#time.sleep(1)
		chrono = Timer.Chrono()
		chrono.start()
		start_time = chrono.read_ms()
		#print('Start time', start_time)

		peak_to_peak = 0  		# peak-to-peak level
		signal_max = 0  		# max signal				
		signal_min = 1024  		# min signal				
		#sample = apin()
		while (chrono.read_ms() - start_time) < SAMPLE_WINDOW:  # 50 ms
			sample = apin()  	# read an analog value
			if sample > signal_max:					
				signal_max = sample
			elif sample < signal_min:				
				signal_min = sample
		peak_to_peak = signal_max - signal_min
		volts = (peak_to_peak * 3.3) / 1024
		if (peak_to_peak > 0):
			dB= (20*(log((peak_to_peak/1024)+1, 10)))*5 #calculate sound level in decibel
			print(dB)		
		else:
			dB = 'test'
			#print(dB)
		
		
		
		
		
		
