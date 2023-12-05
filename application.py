import connections
class application(connections):
    def __init__(self):
        try:
            self.initializeHW()
            self.initializeConnections()
            self.initializeVariables()
            self.setStatus()
        except:
            self.noFault = False
            print("initialization failed")
    
    def initializeHW(self):
        #this is where you initialize hardware
        print("hardware initialized")
        
    def initializeConnections(self):
        
        #we initialize IO and check connections using handshakes and checks
        #this is where we initialize I/O
        print("connection initialized")

    def initializeVariables(self):
        #this is where we initialize variables,
        #i.e. self.SsomeVariable = defaultValue
        print("variables initialized")

    def setStatus(self):
        self.status = True
        print("status changed")

    def tickfunctionality(self):
        print("tick")
        #Add part of the function for testing
        self.noFault = False
            #what it does each tick
            #write to buffer
            #update local values
            #check values for fault codes
            #set flag to run tick again
    ##member variables
    status = False ##status as to whether variables have been initialized
    noFault = True ##status as to whether any faults have been detected (True means no faults, false means fault detected)