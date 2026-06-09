# Assignment 10 - Student System in Python (OOP)

## Question
Design a student system in Python.

### Classes:
- **Address**: street, city, zipCode
- **Student**: name, age (protected), Address, course list
  - Control age using @property
  - Methods: add_course(), display()
- **ScholarshipStudent**: extends Student, adds scholarshipAmount, overrides display()

### Must Demonstrate:
1. Composition â€” Student HAS-A Address
2. Data validation using @property (age must be valid)
3. Inheritance and overriding using super() in display()
4. Mutable behavior â€” course list updates persist

## Language
Python

## Files
- \student_system.py\
