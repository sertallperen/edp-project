from events.event_base import Event

class PaymentProcessedEvent(Event):
    """Triggered when the payment is successful."""
    event_name = "payment_processed"

    def __init__(self, order_id, amount):
        payload = {
            "order_id": order_id,
            "amount": amount
        }
        super().__init__(payload)

class PaymentFailedEvent(Event):
    """Triggered when the payment fails."""
    event_name = "payment_failed"

    def __init__(self, order_id, reason):
        payload = {
            "order_id": order_id,
            "reason": reason
        }
        super().__init__(payload)