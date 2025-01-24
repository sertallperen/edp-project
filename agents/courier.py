from events.order_events import OrderDeliveredEvent
from event_dispatcher import EventDispatcher

class Courier:
    """The courier picks up the order from the restaurant and delivers it to the customer."""
    
    def __init__(self, name, dispatcher: EventDispatcher):
        self.name = name
        self.dispatcher = dispatcher
        self.dispatcher.register_listener("order_prepared", self.pick_up_order)

    def pick_up_order(self, payload):
        """Called to pick up the order."""
        order_id = payload["order_id"]
        print(f"Courier {self.name} has picked up the order. On the way! (Order ID: {order_id})")
        event = OrderDeliveredEvent(order_id)
        self.dispatcher.dispatch(event)