import can
from can.message import Message
from CAN_DEVICES.CANBUS import CANBUS
from CAN_DEVICES.can_mailbox import mailbox

class test_listener(can.BufferedReader):
    def on_message_received(self, msg: Message):
        print({msg.arbitration_id})
        #return super().on_message_received(msg)

class connections:
    @classmethod
    def checkCANBUS(cls):
        temp_listener = test_listener()
        temp_listener_list = [temp_listener]
        canbus_system = CANBUS(temp_listener_list)
        canbus_system.send_message(can.Message(arbitration_id=110, is_extended_id=False, data=[11,22,33,44,55]))
        canbus_system.send_message(can.Message(arbitration_id=111, is_extended_id=False, data=[11,22,33,44,55]))
        canbus_system.send_message(can.Message(arbitration_id=112, is_extended_id=False, data=[11,22,33,44,55]))
        #canbus_system.print_message()
        canbus_system.shutdown()
        #mailbox_listner = testListner()
        #mailbox = can.Notifier(canbus_system.first_bus,[mailbox_listner], timeout=1)
        #check_mailbox = mailbox(canbus_system.first_bus)
        #canbus_system.first_bus.recv(timeout=5)
        #canbus_system.first_bus.send(can.Message(arbitration_id=110, is_extended_id=False, data=[11,22,33,44,55]))
        #canbus_system.first_bus.send(can.Message(arbitration_id=120, is_extended_id=False, data=[11,22,33,44,55]))
        #canbus_system.first_bus.send(can.Message(arbitration_id=130, is_extended_id=False, data=[11,22,33,44,55]))
        #canbus_system.first_bus.recv(timeout=3)
        #msg = check_mailbox.mailbox_listner.get_message()
        #msg = mailbox_listner.get_message()
        #print(msg)
        #check_mailbox.ShutDownBox()
        #mailbox_listner.stop()
        #mailbox.stop()
        #canbus_system.first_bus.shutdown()
        print("connection checked")

        #possbily use on recive to check if message is a fault
        #code and if it is return false for tick functionality
        


        
connections.checkCANBUS()

