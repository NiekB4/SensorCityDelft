import time
from machine import Pin
from dth import DTH

# data pin connected to P11
# 1 for AM2302
th = DTH(Pin('P3', mode=Pin.OPEN_DRAIN), 1)
time.sleep(5)

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
    if len(humidities) == 10:
        sum_hum = sum(humidities)
        avg_hum = sum_hum / 10.0
        print(" ")
        print('The average humidity was: {:3.2f}'.format(avg_hum))
        print('The maximum humidity was: {:3.2f}'.format(max(humidities)))
        print('The minumum humidity was: {:3.2f}'.format(min(humidities)))
        humidities = []
    time.sleep(5)
