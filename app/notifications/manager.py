class NotificationsManager:
    def __init__(self):
        self._observers = []

    def register(self, observer):
        self._observers.append(observer)

    def notify(self, event, data):
        for observer in self._observers:
            observer.notify(event, data)