from Period import Period

class Session(Period):
    def __init__(self,period,presenter):
        super().copy(period)                  # period
        self._presenter = presenter           # Person
    
    def getPresenter(self):
        return self._presenter

    def setPresenter(self,presenter):
        self._presenter = presenter
    
    