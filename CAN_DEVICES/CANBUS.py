'''
General implementation of socketCAN instance

Use conflict-safe instance of method:
https://python-can.readthedocs.io/en/master/bus.html#thread-safe-bus

'''
import can
import canbusconfig

class CANBUS(canbusconfig):
    def __init__(self):
        try:
            first_bus = can.ThreadSafeBus(interface=canbusconfig.interface['socketcan'], channel=canbusconfig.ports['virtual'])
            first_bus.recv(timeout=3) #if it spends more than
        except:
            e = "error setting up the threadsafebus, please ensure that your interface"
            return
