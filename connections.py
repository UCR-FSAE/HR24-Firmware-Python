import can
from can.message import Message
from CAN_DEVICES.CANBUS import CANBUS
import time

#simply listener class to test connection of canbus
class test_listener(can.BufferedReader):
    def on_message_received(self, msg: Message):
        print({msg.arbitration_id})

class connections:
    @classmethod
    def checkCANBUS(cls):
        temp_listener = test_listener()
        temp_listener_list = [temp_listener]
        canbus_system = CANBUS(temp_listener_list)
        canbus_system.send_message(can.Message(arbitration_id=110, is_extended_id=False, data=[11,22,33,44,55]))
        canbus_system.send_message(can.Message(arbitration_id=111, is_extended_id=False, data=[11,22,33,44,55]))
        canbus_system.send_message(can.Message(arbitration_id=112, is_extended_id=False, data=[11,22,33,44,55]))

        #buffer to allow time for messages to be received and printed
        time.sleep(1)
        canbus_system.shutdown()
        print("connection checked")

        #possbily use on recive to check if message is a fault
        #code and if it is return false for tick functionality
        


        
connections.checkCANBUS()

