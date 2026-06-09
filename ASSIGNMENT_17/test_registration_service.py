"""
=========================================================
            PYTEST UNIT TEST SUITE
=========================================================
"""

import pytest

from registration_service import (
    RegistrationService,
    InvalidEmailError,
    UnderageError
)


# =========================================================
# SHARED FIXTURE
# =========================================================

@pytest.fixture
def service():
    """
    Creates a shared RegistrationService object
    before every test.
    """

    return RegistrationService()


# =========================================================
# TEST : SUCCESSFUL REGISTRATION
# =========================================================

def test_valid_registration(service):

    result = service.register_user(
        "student123@gmail.com",
        20
    )

    assert result is True


# =========================================================
# TEST : EMPTY EMAIL
# =========================================================

def test_empty_email(service):

    with pytest.raises(InvalidEmailError):

        service.register_user("", 20)


# =========================================================
# TEST : INVALID EMAIL FORMAT
# =========================================================

def test_invalid_email(service):

    with pytest.raises(InvalidEmailError):

        service.register_user("invalid-email", 20)


# =========================================================
# TEST : UNDERAGE USER
# =========================================================

def test_underage_user(service):

    with pytest.raises(UnderageError):

        service.register_user("abc@gmail.com", 15)


# =========================================================
# TEST : NEGATIVE AGE ASSERTION
# =========================================================

def test_negative_age_assertion(service):

    with pytest.raises(AssertionError):

        service.register_user("abc@gmail.com", -5)