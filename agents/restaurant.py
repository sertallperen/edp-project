from events.order_events import OrderPreparedEvent
from event_dispatcher import EventDispatcher
#Restoran, siparişleri alır ve hazırlar.
class Restaurant:  
    def __init__(self, name, dispatcher: EventDispatcher):
        self.name = name
        self.dispatcher = dispatcher
        self.dispatcher.register_listener("order_placed", self.prepare_order)

    def prepare_order(self, payload):
        """Siparişi hazırlar ve event yayınlar."""
        order_id = payload["order_id"]
        print(f"{self.name} restoranı siparişi hazırlıyor... (Sipariş ID: {order_id})")
        event = OrderPreparedEvent(order_id)
        self.dispatcher.dispatch(event)