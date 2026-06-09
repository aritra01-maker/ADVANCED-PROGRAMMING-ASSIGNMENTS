# Assignment 12 - E-Commerce Order System (SOLID Principles)

## Question
Design a system in Java/Python for processing customer orders in an e-commerce platform.

### Supported Features:
- Multiple payment methods (Credit Card, UPI, Wallet, etc.)
- Multiple notification channels (Email, SMS, Push)
- Different order types (Regular, Discounted, Priority)
- Different storage mechanisms (Database, File, etc.)

### SOLID Principles Required:

1. **SRP** â€” Each class has one responsibility (order logic, payment, notification, storage are separate)
2. **OCP** â€” Add new payment methods or notification types without modifying existing classes
3. **LSP** â€” All subclasses work correctly through their base type
4. **ISP** â€” Small, role-specific interfaces; no class implements unused methods
5. **DIP** â€” High-level classes depend on abstractions; use dependency injection

### System Should:
- Create an order
- Process payment using a selected method
- Send notification after successful order
- Save order details using a storage mechanism

## Language
Java or Python

## Files
- Multiple class files as per design
