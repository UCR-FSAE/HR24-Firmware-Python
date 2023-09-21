'''
General implementation of socketCAN instance

Use conflict-safe instance of method:
https://python-can.readthedocs.io/en/master/bus.html#thread-safe-bus

'''
import can
from .can_mailbox import mailbox


from configparser import ConfigParser

config = ConfigParser()
config.read('canbus_config.ini')

class CANBUS():
    def __init__(self, listener_list:list):
        try:
            print("setup virtal CANBUS")
            #self.first_bus = can.ThreadSafeBus(interface=canbusconfig.interface['socketcan'], channel=canbusconfig.ports['virtual'])
            #self.first_bus.recv(timeout=3) #if it spends more than
            self.first_bus = can.ThreadSafeBus(interface=config['Inferfaces']['SocketCan'], channel=config['Ports']['virtual'], receive_own_messages=True)
            self.temp_listner = can.BufferedReader()
            listener_list.append(self.temp_listner)
            self.mail_box = can.Notifier(self.first_bus, listener_list)
        except:
            e = "error setting up the threadsafebus, please ensure that your interface"
            print(e)
            return
        
    def send_message(self, msg: can.Message):
        try:
            self.first_bus.send(msg)
            #print("message sent")
        except:
            print("error, message not sent")
    
    def print_message(self):
        print(self.temp_listner.get_message())
    
    def shutdown(self):
        self.temp_listner.stop()
        self.mail_box.stop()
        self.first_bus.shutdown()



#can_bus_test = CANBUS()