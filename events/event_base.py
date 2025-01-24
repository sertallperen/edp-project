class Event:
    """Base class for all events."""
    def __init__(self, payload=None):
        self.payload = payload if payload else {}

    @property
    def event_name(self):
        """Subclasses must specify the event_name property."""
        raise NotImplementedError("Subclasses must define event_name!")