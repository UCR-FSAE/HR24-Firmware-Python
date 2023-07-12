import application

def __main__():
    app = application()
    while(app.noFault):
        try:
            app.tickfunctionality()
        except:
            print("an error has occurred")
            #potentially not required, as app.tickfunctionality should trigger app.noFault, but interrupt may stop it before it does
            app.noFault = False
            #grab error from app class
            #app.errorcode or something like that