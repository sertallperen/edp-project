from event_base import Event

class OrderPlacedEvent(Event):
    """Müşteri sipariş verdiğinde tetiklenir."""
    event_name = "order_placed"

    def __init__(self, order_id, customer_name, items):
        payload = {
            "order_id": order_id,
            "customer_name": customer_name,
            "items": items
        }
        super().__init__(payload)

class OrderPreparedEvent(Event):
    """Restoran siparişi hazırladığında tetiklenir."""
    event_name = "order_prepared"

    def __init__(self, order_id):
        payload = {"order_id": order_id}
        super().__init__(payload)

class OrderDeliveredEvent(Event):
    """Sipariş müşteriye teslim edildiğinde tetiklenir."""
    event_name = "order_delivered"

    def __init__(self, order_id):
        payload = {"order_id": order_id}
        super().__init__(payload)