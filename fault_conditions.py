import bloom_filter
import config

class fault_conditions():
    def __init__(self):
        #initialize the fault code parsing
        #initialize table
        print("fault code check initialized")
    def check(self, code):
        #check code against table
        #likely needs optimization, maybe a preliminary bloom filter, maybe a hash table
            #bloom filter would run quick search for code NOT being fault code
            #false return would trigger long search and if found, return interrupt

        #leaving dictionary implementation as default
        if code in config.FaultCodes.keys():
            return True
        else:
            return False

