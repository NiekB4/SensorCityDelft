"""
KPN LORA
Change these for your own keys (see https://loradeveloper.mendixcloud.com/
"""

DEV_ADDR = '14204D69'
NWKS_KEY = 'cf30d6929805e8594b19882245e7198f'
APPS_KEY = '7e0ec0209b5553beda68d875c76f0864'



"""
THE THINGS NETWORK
Change these for your own keys (see https://www.thethingsnetwork.org)
Type has to be string
"""
"""
APP_EUI = '70B3D57EF0004D2A'
APP_KEY = '4D937816D0EBECBBCEA62B048C1165DE'

"""

"""
LoPy LoRaWAN Nano Gateway configuration details
"""

GATEWAY_ID = "70b3d54998b3b0d7"  # '11aa334455bb7788'

# SERVER = "ttn-router-eu"  # 'router.eu.thethings.network'
SERVER = 'router.eu.thethings.network'
PORT = 1700

NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600

WIFI_SSID = "niek"  # 'my-wifi'
WIFI_PASS = "geomatics"  # 'my-wifi-password'

LORA_FREQUENCY = 868100000
LORA_DR = "SF7BW125"   # DR_5
