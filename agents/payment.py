from events.payment_events import PaymentProcessedEvent, PaymentFailedEvent
from event_dispatcher import EventDispatcher

class PaymentSystem:
    """Ödeme sistemini simüle eder."""
    
    def __init__(self, dispatcher: EventDispatcher):
        self.dispatcher = dispatcher
        self.dispatcher.register_listener("order_placed", self.process_payment)

    def process_payment(self, payload):
        """Ödemeyi işler."""
        order_id = payload["order_id"]
        amount = len(payload["items"]) * 10  # Örnek ücretlendirme
        print(f"Ödeme işleniyor: {amount} TL (Sipariş ID: {order_id})")

        if amount > 0:
            event = PaymentProcessedEvent(order_id, amount)
            print(f"Ödeme başarılı! (Sipariş ID: {order_id})")
        else:
            event = PaymentFailedEvent(order_id, "Geçersiz tutar")
            print(f"Ödeme başarısız! (Sipariş ID: {order_id})")

        self.dispatcher.dispatch(event)