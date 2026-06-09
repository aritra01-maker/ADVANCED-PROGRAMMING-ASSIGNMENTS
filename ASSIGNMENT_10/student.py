# Address Class → Represents a student's address
class Address:
    def __init__(self, street, city, zip_code):
        # Initialize address attributes
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def display(self):
        # Returns formatted address string
        return f"{self.street}, {self.city} - {self.zip_code}"


# Student Class → Main class
class Student:
    def __init__(self, name, age, address, courses=None):
        self.name = name  # Public attribute

        # Protected attribute (_age) → should not be accessed directly
        self._age = None

        # Setter is used → ensures validation happens
        self.age = age

        # Composition → Student HAS-A Address object
        self.address = address

        # Mutable list handling
        # If no list is passed, create a new list (avoids shared reference issue)
        if courses is None:
            self.courses = []
        else:
            self.courses = courses

    # Getter for age
    @property
    def age(self):
        return self._age

    # Setter for age with validation
    @age.setter
    def age(self, value):
        # Validation logic
        if not isinstance(value, int) or value <= 0 or value > 120:
            raise ValueError("Age must be between 1 and 120")

        # Assign valid value
        self._age = value

    # Method to add course → modifies same list (mutable behavior)
    def add_course(self, course):
        self.courses.append(course)

    # Display student details
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

        # Calling Address class method → shows composition usage
        print(f"Address: {self.address.display()}")

        print("Courses:", ", ".join(self.courses))


# Derived Class → Inheritance
class ScholarshipStudent(Student):
    def __init__(self, name, age, address, courses, scholarship_amount):

        # Call parent constructor → avoids rewriting code
        super().__init__(name, age, address, courses)

        # New attribute specific to child class
        self.scholarship_amount = scholarship_amount

    # Method overriding
    def display(self):
        # Call parent display method first
        super().display()

        # Add extra detail
        print(f"Scholarship Amount: ₹{self.scholarship_amount}")


# -------------------------------
# Testing the system
# -------------------------------

# Create Address object
addr = Address("XYZ ROAD", "TEZPUR", "784001")
addr2 = Address("ABC STREET", "GUWAHATI", "781001")

# Create Student object
student1 = Student("Aritra", 20, addr)

# Add courses → modifies same list (mutable behavior)
student1.add_course("Data Structures")
student1.add_course("Algorithms")

print("=== Student Details ===")
student1.display()

# Add another course → persists 
student1.add_course("Operating Systems")

print("\nAfter adding another course:")
student1.display()

# Create Scholarship Student
scholar = ScholarshipStudent(
    "Priya", 21, addr2, ["DBMS", "OS"], 50000
)

print("\n=== Scholarship Student Details ===")
scholar.display()