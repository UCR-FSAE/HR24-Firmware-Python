import can



class device(can.BufferedReader):
    def __init__(self):
        try:
            # generate all the variables your specific class will use
            #CANBUS messages
            self.FIRMWARE_VERSION = None
            self.CELL_DO_SOMETHING_COMMAND = None
            self.CELL_1_4_TEMPERATURE = None
            self.CELL_1_4_VOLTAGE = None
            self.DEVICE_STATUS = None
            #FAULT CODE messages
            self.faultList = None
            #call the functions needed for variables and first instance
            self.messageType()
            self.faultInitializer()
            print("device initialized")
        except:
            e = "error setting up device"
            print(e)
            return
    '''
    The following functions are barebones templates for:
    using setter/getter functions, a buffer, and processing functions
    '''
    def __dummyBuffer__(self):
        # dummy buffer, can fill out as needed
        self.dummyvalue = "value would go here"
        self.sedonddummyvalue = "this is another dummy value"
    def getterTemplate(self):
        # big idea is: get a value from buffer, do something with it or send to where it needs to go by calling another method
        # gets value from buffer (i.e. self.dummyvalue)
        tempvalue = self.dummyvalue
        # does something with the temporary value
        tempvalue += 1
        # stores changed value somewhere
        self.sedonddummyvalue = tempvalue
    def dummyprocessingfunction(arg):
        # does something
        temp = arg + 1
        arg = temp
        return arg
    def setterTemplate(self):
        # setter function, sets value in class based on condition, etc
        temp = self.sedonddummyvalue
        '''
        #can do something like the following:
        if temp==condition:
            self.seconddummyvalue = self.callfunction(temp)
        '''
        # alternatively, for simpler functions just set the value to something like output with it called inline
        self.seconddummyvalue = self.dummyprocessingfunction(temp)
        
    '''
    The following functions are for processing CANBUS messages
    '''
    def messageType(self):
        # example message types
        # contains address and name
        '''
        #Removed tuple
        self.DEVICE_STATUS = 0x10,
        self.CELL_1_4_VOLTAGE = 0x20,
        self.CELL_1_4_TEMPERATURE = 0x30,
        self.CELL_DO_SOMETHING_COMMAND = 0x40,
        self.FIRMWARE_VERSION = 0xA0
        '''
        self.DEVICE_STATUS = 0x10
        self.CELL_1_4_VOLTAGE = 0x20
        self.CELL_1_4_TEMPERATURE = 0x30
        self.CELL_DO_SOMETHING_COMMAND = 0x40
        self.FIRMWARE_VERSION = 0xA0

    def receiveMessage(self, msg):
        # parses through "mailbox" of recent messages and grabs it, stores to local buffer if it's relevant
        # elementary implementation would look like this:
        #Removed msg.code



        if any(msg == fault for fault in self.faultList):
            # do something with the fault
            # perhaps initiate shutdown sequence
            print("fault detected: ", msg)
        else:
            match msg:
                case self.DEVICE_STATUS:
                    print("device status", msg)

                case self.CELL_1_4_VOLTAGE:
                    print("cell voltage", msg)
                
                case self.CELL_1_4_TEMPERATURE:
                    print("cell temperature", msg)
                
                case self.CELL_DO_SOMETHING_COMMAND:
                    print("do something command", msg)

                case self.FIRMWARE_VERSION:
                    print("firmware version", msg)
                case _:
                    print("non related message, store in buffer")
                

    def faultInitializer(self):
        # a function called in init,
        # you can fill out the faultList with the actual fault codes for the specific device
        self.faultList = (0x0AC, 0x0AB)


#device_test = device()

#device_test.receiveMessage(0x10)