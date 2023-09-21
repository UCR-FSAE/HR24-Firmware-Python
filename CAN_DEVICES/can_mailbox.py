import can

class mailbox:
    def __init__(self, bus):
        try:
            self.mailbox_listner = can.BufferedReader()
            self.mailbox_notifier = can.Notifier(bus,[self.mailbox_listner], timeout=1.5)

            #self.mailbox_listner.stop()
            print("mailbox set up")
        except:
            e = "error setting up mailbox"
            print(e)
    
    def ShutDownBox(self):
        self.mailbox_notifier.stop()
        self.mailbox_listner.stop()
        print("mailbox shut off")