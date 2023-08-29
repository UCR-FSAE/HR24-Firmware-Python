'''
General implementation of socketCAN instance

Use conflict-safe instance of method:
https://python-can.readthedocs.io/en/master/bus.html#thread-safe-bus

'''
import can
import canbusconfig
#import canbusconfig
#class CANBUS(canbusconfig) not working when having in
class CANBUS():
    def __init__(self):
        try:
            print("setup virtal CANBUS")
            self.first_bus = can.ThreadSafeBus(interface=canbusconfig.interface['socketcan'], channel=canbusconfig.ports['virtual'])
            #self.first_bus.recv(timeout=3) #if it spends more than

        except:
            e = "error setting up the threadsafebus, please ensure that your interface"
            return
    
