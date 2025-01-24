# Event-Driven Order System

This project demonstrates an event-driven architecture (EDA) for a simple order management system. Various components such as the Customer, Restaurant, Courier, and Payment System communicate through events to simulate a real-world order and delivery process.

## Features
	•	Event-Driven Communication: Components interact through events, allowing for decoupled communication.
	•	Modular Components: The system consists of independent modules representing different entities like the customer, restaurant, courier, and payment system.
	•	Event Handling: The system uses an event dispatcher to handle event registration and dispatching to relevant listeners.

## Architecture Overview
	1.	Event: The base class for all events in the system. Each event carries a payload and requires subclasses to define a unique event_name.
	2.	EventDispatcher: A central component responsible for managing event listeners and dispatching events to the corresponding handlers.
	3.	Customer: Represents a customer who places orders and waits for the order to be delivered. The customer listens for the order_delivered event.
	4.	Restaurant: A restaurant that prepares orders when they are placed. It listens for the order_placed event and dispatches the order_prepared event once the order is ready.
	5.	Courier: The courier picks up the prepared order and delivers it to the customer. It listens for the order_prepared event and dispatches the order_delivered event when the order is successfully delivered.
	6.	PaymentSystem: The payment system processes payments for the orders placed. It listens for the order_placed event, processes the payment, and dispatches either a payment_processed or payment_failed event based on the outcome.

## Event Flow
	1.	Customer Places an Order: The customer invokes the place_order method, which triggers the order_placed event.
	2.	Restaurant Prepares the Order: Upon receiving the order_placed event, the restaurant prepares the order and dispatches the order_prepared event.
	3.	Courier Delivers the Order: The courier listens for the order_prepared event, picks up the order, and dispatches the order_delivered event once the delivery is completed.
	4.	Payment Processing: The payment system listens for the order_placed event, processes the payment, and dispatches either a payment_processed or payment_failed event.