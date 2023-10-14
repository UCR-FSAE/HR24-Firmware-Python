import can
from can.message import Message
from configparser import ConfigParser

config = ConfigParser()
config.read('canbus_config.ini')



#table class to hold a objects hash table
class id_table():
    def __init__(self, hash_table:dict):
        self.hash_table = hash_table

#mailbox class to handle reciving and distrubting messages
class mailbox(can.BufferedReader):
    def __init__(self):
        try:
            #create device table with device ids
            self.device_ids = (dict(config['Devices']))
            self.current_mailbox = []
            print("mailbox set up")
        except:
            e = "error setting up mailbox"
            print(e)

    def on_message_received(self, msg: Message):
        match self.current_mailbox.len():
            #stuck here
            case 10:
                print("flush out mailbox")
            case _:
               self.current_mailbox.append(msg) 
    
    def distrube_messages(self):
        print("bloom filter")


    
            