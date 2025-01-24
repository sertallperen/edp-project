from events.order_events import OrderPlacedEvent
from event_dispatcher import EventDispatcher

class Customer:
    """The customer places an order and tracks its status."""
    
    def __init__(self, name, dispatcher: EventDispatcher):
        self.name = name
        self.dispatcher = dispatcher
        self.dispatcher.register_listener("order_delivered", self.order_received)

    def place_order(self, order_id, items):
        """The customer places an order."""
        print(f"{self.name} placed an order: {items}")
        event = OrderPlacedEvent(order_id, self.name, items)
        self.dispatcher.dispatch(event)

    def order_received(self, payload):
        """Called when the order is delivered to the customer."""
        print(f"{self.name} has received the order! (Order ID: {payload['order_id']})")