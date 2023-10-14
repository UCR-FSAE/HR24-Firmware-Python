'''
Configuration file for CANBUS

Different operating modes, etc

'''

from configparser import ConfigParser

config = ConfigParser()

# settings for accessing different can objects, etc
config["Ports"] = {
    "virtual": 'vcan0',
    "usb": 'can0',
    "pin": 'can1',
}

config["Inferfaces"] = {
    "SocketCan" : 'socketcan'
}

with open("canbus_config.ini", "w") as file:
    config.write(file)