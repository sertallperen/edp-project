from events.order_events import OrderPreparedEvent
from event_dispatcher import EventDispatcher

# The restaurant receives and prepares orders.
class Restaurant:  
    def __init__(self, name, dispatcher: EventDispatcher):
        self.name = name
        self.dispatcher = dispatcher
        self.dispatcher.register_listener("order_placed", self.prepare_order)

    def prepare_order(self, payload):
        """Prepares the order and dispatches an event."""
        order_id = payload["order_id"]
        print(f"{self.name} restaurant is preparing the order... (Order ID: {order_id})")
        event = OrderPreparedEvent(order_id)
        self.dispatcher.dispatch(event)