class EventDispatcher:
    """Central dispatcher managing events."""
    def __init__(self):
        self.listeners = {}

    def register_listener(self, event_name, callback):
        """Adds a listener (callback) for a specific event."""
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(callback)

    def dispatch(self, event):
        """Sends the event to the corresponding listeners."""
        event_name = event.event_name
        if event_name in self.listeners:
            for callback in self.listeners[event_name]:
                callback(event.payload)