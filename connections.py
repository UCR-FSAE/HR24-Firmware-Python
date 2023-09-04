import can
#import CANBUS
from CAN_DEVICES.CANBUS import CANBUS

class connections:
    @classmethod
    def checkCANBUS(cls):
        canbusCheck = CANBUS()
        canbusCheck.first_bus.send(can.Message(arbitration_id=123, is_extended_id=True, data=[0x11, 0x22, 0x33]))
        #canbusCheck.first_bus.recv(timeout=3)
        #canbusCheck.first_bus.shutdown()
        print("connection checked")
        

connections.checkCANBUS()

