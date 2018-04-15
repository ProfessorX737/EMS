from Period import Period

class Session(Period):
    def __init__(self,presenter,period):
        self._presenter = presenter
        self._period = period
    
    def getPresenter(self):
        return self._presenter
    def getPeriod(self):
        return self._period
    
    def setPresenter(self,presenter):
        self._presenter = presenter
    def setPeriod(self,period):
        self._period = period
    
    