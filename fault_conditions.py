import bloom-filter
import config

class fault_conditions():
    def __init__(self):
        #initialize the fault code parsing
        #initialize table
        print("fault code check initialized")
    def check(self, code):
        #check code against table
        #likely needs optimization, maybe a bloom filter, maybe a hash table
        #leaving dictionary implementation as default

