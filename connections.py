import can
import sys
sys.path.append('/home/mario/Desktop/HR24E_python/CAN_DEVICES')

#import CANBUS
from CAN_DEVICES.CANBUS import CANBUS

class connections:
    def checkCANBUS(self,CANBUS):
        canbusCheck = CANBUS()
        canbusCheck.first_bus.send(can.Message(arbitration_id=123, is_extended_id=True, data=[0x11, 0x22, 0x33]))
        canbusCheck.first_bus.recv(timeout=3)
        canbusCheck.first_bus.shutdown()
        print("connection checked")
        

connections.checkCANBUS(connections, CANBUS)
