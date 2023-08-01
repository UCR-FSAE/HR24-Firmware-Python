'''
Configuration file for CANBUS

Different operating modes, etc

'''

# settings for accessing different can objects, etc
ports = dict(
    virtual = 'vcan0',
    usb = 'can0',
    pin = 'can1'
)

interface = dict(
    socketcan = 'socketcan',
)