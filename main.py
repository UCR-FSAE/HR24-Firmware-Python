import application

def __main__():
    app = application()
    while(app.noFault):
        try:
            app.tickfunctionality()
        except:
            print("an error has occurred")
            #grab error from app class
            #app.errorcode or something like that

