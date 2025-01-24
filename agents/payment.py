from events.payment_events import PaymentProcessedEvent, PaymentFailedEvent
from event_dispatcher import EventDispatcher

class PaymentSystem:
    """Simulates the payment system."""
    
    def __init__(self, dispatcher: EventDispatcher):
        self.dispatcher = dispatcher
        self.dispatcher.register_listener("order_placed", self.process_payment)

    def process_payment(self, payload):
        """Processes the payment."""
        order_id = payload["order_id"]
        amount = len(payload["items"]) * 10  # Example pricing
        print(f"Processing payment: {amount} TL (Order ID: {order_id})")

        if amount > 0:
            event = PaymentProcessedEvent(order_id, amount)
            print(f"Payment successful! (Order ID: {order_id})")
        else:
            event = PaymentFailedEvent(order_id, "Invalid amount")
            print(f"Payment failed! (Order ID: {order_id})")

        self.dispatcher.dispatch(event)