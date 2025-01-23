from events.order_events import OrderDeliveredEvent
from event_dispatcher import EventDispatcher

class Courier:
    """Kurye, siparişi restorandan alıp müşteriye teslim eder."""
    
    def __init__(self, name, dispatcher: EventDispatcher):
        self.name = name
        self.dispatcher = dispatcher
        self.dispatcher.register_listener("order_prepared", self.pick_up_order)

    def pick_up_order(self, payload):
        """Siparişi teslim almak için çağrılır."""
        order_id = payload["order_id"]
        print(f"{self.name} kuryesi siparişi aldı. Yolda! (Sipariş ID: {order_id})")
        event = OrderDeliveredEvent(order_id)
        self.dispatcher.dispatch(event)