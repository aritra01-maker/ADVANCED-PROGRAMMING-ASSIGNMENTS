"""
=========================================================
        USER ONBOARDING VALIDATION MODULE
=========================================================

This module validates:
1. User Email
2. User Age

Author : Student Assignment
Language : Python
=========================================================
"""

# Importing regular expression module
import re


# =========================================================
# CUSTOM EXCEPTION CLASSES
# =========================================================

class InvalidEmailError(ValueError):
    """
    Raised when the email is invalid.
    Inherits from ValueError because
    the input value is incorrect.
    """

    def __init__(self, email):
        message = (
            f"\n[EMAIL VALIDATION FAILED]\n"
            f"Provided email '{email}' is invalid.\n"
            f"Please enter a valid email address.\n"
        )
        super().__init__(message)


class UnderageError(Exception):
    """
    Raised when the user's age is below 18.
    """

    def __init__(self, age):
        message = (
            f"\n[AGE VALIDATION FAILED]\n"
            f"Registration denied.\n"
            f"Provided age: {age}\n"
            f"Minimum required age: 18\n"
        )
        super().__init__(message)


# =========================================================
# REGISTRATION SERVICE CLASS
# =========================================================

class RegistrationService:

    def __init__(self):
        """
        Constructor initializes regex pattern.
        """

        # Regular expression for email validation
        self.email_pattern = (
            r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        )

    # -----------------------------------------------------
    # METHOD : register_user
    # -----------------------------------------------------

    def register_user(self, email: str, age: int) -> bool:
        """
        Validates user registration details.

        Parameters:
            email (str): User email address
            age (int): User age

        Returns:
            bool: True if registration succeeds

        Raises:
            InvalidEmailError
            UnderageError
        """

        # =================================================
        # ASSERTION CHECKS (Internal Invariant Checks)
        # =================================================

        # Age should never be negative
        assert age >= 0, "System Error: Age cannot be negative."

        # Email object should not be None
        assert email is not None, "System Error: Email is None."

        # =================================================
        # EMAIL VALIDATION
        # =================================================

        # Remove leading/trailing spaces
        email = email.strip()

        # Check if email is empty
        if email == "":
            raise InvalidEmailError(email)

        # Regex validation
        if not re.match(self.email_pattern, email):
            raise InvalidEmailError(email)

        # =================================================
        # AGE VALIDATION
        # =================================================

        if age < 18:
            raise UnderageError(age)

        # =================================================
        # SUCCESSFUL REGISTRATION
        # =================================================

        print("\n=================================================")
        print("        REGISTRATION SUCCESSFUL")
        print("=================================================")
        print(f"Registered Email : {email}")
        print(f"Registered Age   : {age}")
        print("Account Status   : ACTIVE")
        print("=================================================\n")

        return True


# =========================================================
# DRIVER CODE
# =========================================================

if __name__ == "__main__":

    service = RegistrationService()

    print("\n==============================================")
    print("      USER REGISTRATION VALIDATION SYSTEM")
    print("==============================================")

    try:

        email = input("\nEnter Email : ")
        age = int(input("Enter Age   : "))

        service.register_user(email, age)

    except InvalidEmailError as e:
        print(e)

    except UnderageError as e:
        print(e)

    except AssertionError as e:
        print(f"\n[ASSERTION ERROR]\n{e}")

    except ValueError:
        print("\nInvalid input. Age must be numeric.")

    finally:
        print("\nProgram execution completed.\n")