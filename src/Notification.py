from collections import OrderedDict

class Notification:
    def __init__(self,message):
        self.__message = message
        self.__routeLabelMap = OrderedDict()

    def addButton(self, routeName, buttonLabel):
        self.__routeLabelMap[routeName] = buttonLabel
    def getMessage(self):
        return self.__message
    def getRouteLabelMap(self):
        return self.__routeLabelMap

class DeletableNotification(Notification):
    def __init__(self,message):
        super().__init__(message)
        super().addButton("delete_notification","X")

class AcceptRejectNotification(Notification):
    def __init__(self,message,eventId):
        super().__init__(message)
        super().addButton("accept_notification", "Accept")
        super().addButton("reject_notification", "Reject")
        self.__eventId = eventId
    def getEventId(self):
        return self.__eventId