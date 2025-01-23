class Event:
    """Tüm event'ler için temel sınıf."""
    def __init__(self, payload=None):
        self.payload = payload if payload else {}

    @property
    def event_name(self):
        """Alt sınıfların event_name özelliği olmalı."""
        raise NotImplementedError("Alt sınıflar event_name belirtmelidir!")