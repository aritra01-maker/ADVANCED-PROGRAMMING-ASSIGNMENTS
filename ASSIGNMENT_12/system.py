# ============================================================
#   E-COMMERCE ORDER PROCESSING SYSTEM
#   Designed with SOLID Principles in Python
# ============================================================

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
import json, uuid


# ─────────────────────────────────────────────
# DATA MODEL  (Single responsibility: just hold data)
# ─────────────────────────────────────────────
@dataclass
class Order:
    customer_name: str
    items: list
    total_amount: float
    order_type: str = "Regular"
    order_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    status: str = "Pending"


# ─────────────────────────────────────────────
# PAYMENT INTERFACE  (ISP: small, focused interface)
# ─────────────────────────────────────────────
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Returns True if payment succeeds."""


# Concrete payment methods — OCP: add new ones without touching existing code
class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"  [Credit Card] Charged ₹{amount:.2f} — Approved ✓")
        return True

class UPIPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"  [UPI] Payment of ₹{amount:.2f} via UPI — Success ✓")
        return True

class WalletPayment(PaymentProcessor):
    def __init__(self, balance: float):
        self.balance = balance

    def process_payment(self, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            print(f"  [Wallet] Debited ₹{amount:.2f} | Remaining: ₹{self.balance:.2f} ✓")
            return True
        print(f"  [Wallet] Insufficient balance ✗")
        return False


# ─────────────────────────────────────────────
# NOTIFICATION INTERFACE  (ISP: separate from payment)
# ─────────────────────────────────────────────
class NotificationSender(ABC):
    #PARENT CLASS FOR ALL NOTIFICATION TYPES
    @abstractmethod
    def send(self, order: Order) -> None:
        """Send a notification for the given order."""


# OCP: new channel = new class, zero changes elsewhere
#LSP is also maintained since all notifications can be used interchangeably in OrderService
class EmailNotification(NotificationSender):
    def send(self, order: Order) -> None:
        print(f"  [Email] Order #{order.order_id} confirmed for {order.customer_name}")

class SMSNotification(NotificationSender):
    def send(self, order: Order) -> None:
        print(f"  [SMS] Hi {order.customer_name}! Your order #{order.order_id} is placed.")

class PushNotification(NotificationSender):
    def send(self, order: Order) -> None:
        print(f"  [Push] 🔔 Order #{order.order_id} placed successfully!")


# ─────────────────────────────────────────────
# STORAGE INTERFACE  (ISP + DIP)
# ─────────────────────────────────────────────
class OrderStorage(ABC):
    #PARENT CLASS FOR ALL STORAGE TYPES
    @abstractmethod
    def save(self, order: Order) -> None:
        """Persist the order."""


class DatabaseStorage(OrderStorage):
    """Simulates a DB insert."""
    def save(self, order: Order) -> None:
        print(f"  [DB] INSERT order #{order.order_id} → orders table ✓")

class FileStorage(OrderStorage):
    """Appends order as JSON to a local file."""
    def __init__(self, filepath: str = "orders.json"):
        self.filepath = filepath

    def save(self, order: Order) -> None:
        record = {
            "order_id": order.order_id,
            "customer": order.customer_name,
            "items": order.items,
            "total": order.total_amount,
            "type": order.order_type,
            "status": order.status,
            "created_at": order.created_at,
        }
        with open(self.filepath, "a") as f:
            f.write(json.dumps(record) + "\n")
        print(f"  [File] Order #{order.order_id} saved to '{self.filepath}' ✓")


# ─────────────────────────────────────────────
# ORDER PRICING STRATEGY  (LSP + OCP)
# Different order types override only what they need.
# ─────────────────────────────────────────────
class OrderPricing(ABC):
    #PARENT CLASS FOR ALL PRICING STRATEGIES
    @abstractmethod
    def final_amount(self, order: Order) -> float:
        """Return the payable amount."""

class RegularOrderPricing(OrderPricing):
    def final_amount(self, order: Order) -> float:
        return order.total_amount          # No change

class DiscountedOrderPricing(OrderPricing):
    def __init__(self, discount_pct: float = 10):
        self.discount_pct = discount_pct

    def final_amount(self, order: Order) -> float:
        discount = order.total_amount * self.discount_pct / 100
        print(f"  [Discount] {self.discount_pct}% off → saving ₹{discount:.2f}")
        return order.total_amount - discount

class PriorityOrderPricing(OrderPricing):
    SURCHARGE = 50  # flat priority fee

    def final_amount(self, order: Order) -> float:
        print(f"  [Priority] ₹{self.SURCHARGE} surcharge added for express delivery")
        return order.total_amount + self.SURCHARGE


# ─────────────────────────────────────────────
# ORDER SERVICE — High-level orchestrator
# DIP: depends only on abstractions injected at runtime
# SRP: only responsibility is to coordinate the flow
# ─────────────────────────────────────────────
class OrderService:

    #CLASS IN WHICH DEPENDENCIES ARE INJECTED OR IMPOSED EXTERNALLY, NOT CREATED INSIDE
    def __init__(
        self,
        payment: PaymentProcessor,       # abstraction, not CreditCardPayment
        notifications: list[NotificationSender],
        storage: OrderStorage,
        pricing: OrderPricing,
    ):
        self._payment = payment
        self._notifications = notifications
        self._storage = storage
        self._pricing = pricing

    def place_order(self, order: Order) -> None:
        print(f"\n{'═'*50}")
        print(f"  ORDER #{order.order_id} | {order.order_type} | {order.customer_name}")
        print(f"  Items : {', '.join(order.items)}")
        print(f"{'─'*50}")

        # 1. Calculate final amount
        amount = self._pricing.final_amount(order)

        # 2. Process payment
        success = self._payment.process_payment(amount)
        if not success:
            print("  ✗ Payment failed. Order cancelled.")
            return

        # 3. Update status & save
        order.status = "Confirmed"
        self._storage.save(order)

        # 4. Notify via all configured channels
        for notifier in self._notifications:
            notifier.send(order)

        print(f"  ✅ Order #{order.order_id} completed!\n")


# ─────────────────────────────────────────────
# DEMO — Wiring everything together
# ─────────────────────────────────────────────
if __name__ == "__main__":

    # --- Order 1: Regular order, Credit Card, Email + SMS ---
    o1 = Order(customer_name="Arjun Sharma", items=["Laptop", "Mouse"], total_amount=75000, order_type="Regular")
    svc1 = OrderService(
        payment=CreditCardPayment(),
        notifications=[EmailNotification(), SMSNotification()],
        storage=DatabaseStorage(),
        pricing=RegularOrderPricing(),
    )
    svc1.place_order(o1)

    # --- Order 2: Discounted order, UPI, Push notification ---
    o2 = Order(customer_name="Priya Nair", items=["Headphones"], total_amount=3000, order_type="Discounted")
    svc2 = OrderService(
        payment=UPIPayment(),
        notifications=[PushNotification()],
        storage=FileStorage("orders.json"),
        pricing=DiscountedOrderPricing(discount_pct=15),
    )
    svc2.place_order(o2)

    # --- Order 3: Priority order, Wallet (sufficient funds) ---
    o3 = Order(customer_name="Ravi Kumar", items=["Keyboard", "Monitor"], total_amount=15000, order_type="Priority")
    svc3 = OrderService(
        payment=WalletPayment(balance=20000),
        notifications=[EmailNotification(), PushNotification()],
        storage=DatabaseStorage(),
        pricing=PriorityOrderPricing(),
    )
    svc3.place_order(o3)

    # --- Order 4: Wallet with INSUFFICIENT funds ---
    o4 = Order(customer_name="Neha Singh", items=["Smartwatch"], total_amount=12000, order_type="Regular")
    svc4 = OrderService(
        payment=WalletPayment(balance=500),
        notifications=[SMSNotification()],
        storage=FileStorage("orders.json"),
        pricing=RegularOrderPricing(),
    )
    svc4.place_order(o4)