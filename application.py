class application:
    def __init__(self):
        try:
            self.initializeHW(self)
            self.initializeConnections(self)
            self.initializeVariables(self)
            self.setStatus(self)
        except:
            self.noFault = False
            print("initialization failed")
    def initializeHW(self):
        #this is where you initialize hardware
        print("hardware initialized")
    def initializeConnections(self):
        #this is where we initialize I/O
        print("connection initialized")
    def initializeVariables(self):
        #this is where we initialize variables,
        #i.e. self.someVariable = defaultValue
        print("variables initialized")
    def setStatus(self):
        self.status = True
        print("status changed")
    def tickfunctionality(self):
        #what it does each tick
            #write to buffer
            #update local values
            #check values for fault codes
            #set flag to run tick again
    ##member variables
    status = False ##status as to whether variables have been initialized
    noFault = True ##status as to whether any faults have been detected (True means no faults, false means fault detected)