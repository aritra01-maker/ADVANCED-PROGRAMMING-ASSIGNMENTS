# Assignment 09 - Banking System in Java

## Question
Design a banking system in Java.

### Base Class: Account
- Private fields: accountNumber, ownerName, balance
- Getters/setters and at least two constructors (with constructor chaining)
- Methods: deposit(), withdraw() with validation, display()

### Subclasses:
- **SavingsAccount**: add interestRate, override display() showing interest
- **CurrentAccount**: add overdraftLimit, restrict withdrawals accordingly

### Must Demonstrate:
1. Proper encapsulation (no direct field access)
2. Constructor overloading and chaining using this(...)
3. Inheritance and method overriding (@Override and super)
4. Polymorphism â€” store objects in an Account reference list and call display()
5. Basic validation (assert or exception for invalid operations)

## Language
Java

## Files
- \Account.java\
- \SavingsAccount.java\
- \CurrentAccount.java\
- \Main.java\
