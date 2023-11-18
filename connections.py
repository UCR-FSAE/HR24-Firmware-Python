import can
from can.message import Message
from CAN_DEVICES.CANBUS import CANBUS
import time
import random
import datetime

test_bus = can.ThreadSafeBus('test', bustype='virtual')

id_list = random.sample(range(1000), 10)

#simply listener class to test connection of canbus
class test_listener(can.BufferedReader):
    def on_message_received(self, msg: Message):
        print({msg.arbitration_id})
        handshake_dict[msg.arbitration_id] = msg.data

class connections:
    @classmethod
    def checkCANBUS(cls):
        temp_listener = test_listener()
        temp_listener_list = [temp_listener]
        canbus_system = CANBUS(temp_listener_list)
        # canbus_system.send_message(can.Message(arbitration_id=110, is_extended_id=False, data=[11,22,33,44,55]))
        # canbus_system.send_message(can.Message(arbitration_id=111, is_extended_id=False, data=[11,22,33,44,55]))
        # canbus_system.send_message(can.Message(arbitration_id=112, is_extended_id=False, data=[11,22,33,44,55]))
        
        msg = can.Message(arbitration_id=110, is_extended_id=False, data=[11,22,33,44,55])
        canbus_system.send_message(msg)

        #buffer to allow time for messages to be received and printed
        time.sleep(1)
        #possbily use on recive to check if message is a fault
        #code and if it is return false for tick functionality

        # CHECK IF CONNECTED
        print("checking connection")
        # new_msg = canbus_system.recv(timeout=5)
        # print(new_msg.arbitration_id)
        print("connection checked")

        # COLLECT DATA
        x = time.time()
        timeout = x + 20
        i = 0
        while True:
            if time.time() > timeout:
                break
            if i < 10:
                canbus_system.send_message(can.Message(arbitration_id=id_list[i], 
                                                        is_extended_id=False, 
                                                        data=[11,22,33,44,55]))
                i+=1
                # received_msg = canbus_system.recv(timeout=5)  


        canbus_system.shutdown()

        
        


handshake_dict = {}
        
connections.checkCANBUS()
test_bus.shutdown()

# print(handshake_dict)

# CHECK IF ID IS IN DICT
id_1 = id_list[0]
id_2 = id_list[1]
if id_1 in handshake_dict:
    print("id " + str(id_1) + " found in dict")
else:
    print('id: ' + str(id_1) + ' not found')
if id_2 in handshake_dict:
    print("id " + str(id_2) + " found in dict")
else:
    print('id: ' + str(id_2) + ' not found')
