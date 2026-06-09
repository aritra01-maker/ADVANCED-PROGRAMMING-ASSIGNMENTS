# Assignment 17 - User Registration Validation with Custom Exceptions

## Question
Build a user onboarding validation module.

### Constraints:
- Email must not be null/empty and must match a valid email regex pattern
- User must be at least 18 years old

### If Java:
- Checked exception: InvalidEmailException
- Unchecked exception: UnderageException (extends RuntimeException)
- Class: RegistrationService with method:
  \\\java
  public boolean registerUser(String email, int age) throws InvalidEmailException
  \\\
- Include internal assert statement
- JUnit 5 test suite: RegistrationServiceTest
  - @BeforeEach setup
  - Validate successful registrations
  - assertThrows for both exceptions

### If Python:
- InvalidEmailError and UnderageError (inheriting from appropriate built-ins)
- Class: RegistrationService with method:
  \\\python
  def register_user(self, email: str, age: int) -> bool
  \\\
- Internal assert for invariants
- pytest suite with @pytest.fixture, pytest.raises

### Must Have:
1. Custom Exception Design (checked vs unchecked / proper base class)
2. Core Service Validation (regex, age check, assert, exceptions)
3. Unit Testing Suite (framework assertions, fixtures, exception testing)

## Language
Java or Python

## Files
- \RegistrationService.java\ / \egistration_service.py\
- \RegistrationServiceTest.java\ / \	est_registration.py\
