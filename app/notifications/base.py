class BaseNotifier:
    def notify(self, event, data):
        raise NotImplementedError("You must implement the 'notify' method.")
