from event_dispatcher import EventDispatcher
from agents.customer import Customer
from agents.restaurant import Restaurant
from agents.courier import Courier
from agents.payment import PaymentSystem


dispatcher = EventDispatcher()

customer = Customer("Alperen", dispatcher)
restaurant = Restaurant("Degisik Doner", dispatcher)
courier = Courier("Mehmet Kurye", dispatcher)
payment_system = PaymentSystem(dispatcher)

customer.place_order(order_id="1001", items=["Doner", "Ayran"])