'''
General implementation of socketCAN instance

Use conflict-safe instance of method:
https://python-can.readthedocs.io/en/master/bus.html#thread-safe-bus

'''
import can

from configparser import ConfigParser

config = ConfigParser()
config.read('canbus_config.ini')

class CANBUS():
    def __init__(self, listener_list:list):
        try:
            # self.first_bus = can.ThreadSafeBus(interface=config['Inferfaces']['SocketCan'], channel=config['Ports']['virtual'], receive_own_messages=True)
            self.first_bus = can.ThreadSafeBus('test', bustype='virtual', receive_own_messages=True)
            self.can_notifer = can.Notifier(self.first_bus, listener_list)
            print("virtual bus set")
        except:
            e = "error setting up the threadsafebus, please ensure that your interface"
            print(e)
            return
        
    #function for sending messages to the canbus
    def send_message(self, msg: can.Message):
        try:
            self.first_bus.send(msg)
        except:
            print("error, message not sent")

    
    #function to shutdown canbus system
    def shutdown(self):
        print("shutting down")
        # self.temp_listner.stop()
        # self.mail_box.stop()
        self.can_notifer.stop()
        self.first_bus.shutdown()



#can_bus_test = CANBUS()