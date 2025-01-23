class EventDispatcher:
    """Event'leri yöneten merkezî dispatcher."""
    def __init__(self):
        self.listeners = {}

    def register_listener(self, event_name, callback):
        """Belirli bir event için listener (callback) ekler."""
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(callback)

    def dispatch(self, event):
        """Event'i ilgili listener'lara iletir."""
        event_name = event.event_name
        if event_name in self.listeners:
            for callback in self.listeners[event_name]:
                callback(event.payload)