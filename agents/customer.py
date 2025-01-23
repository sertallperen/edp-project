from events.order_events import OrderPlacedEvent
from event_dispatcher import EventDispatcher

class Customer:
    """Müşteri, sipariş verir ve sipariş durumunu takip eder."""
    
    def __init__(self, name, dispatcher: EventDispatcher):
        self.name = name
        self.dispatcher = dispatcher
        self.dispatcher.register_listener("order_delivered", self.order_received)

    def place_order(self, order_id, items):
        """Müşteri sipariş verir."""
        print(f"{self.name} sipariş verdi: {items}")
        event = OrderPlacedEvent(order_id, self.name, items)
        self.dispatcher.dispatch(event)

    def order_received(self, payload):
        """Sipariş müşteriye teslim edildiğinde çağrılır."""
        print(f"{self.name} siparişini teslim aldı! (Sipariş ID: {payload['order_id']})")