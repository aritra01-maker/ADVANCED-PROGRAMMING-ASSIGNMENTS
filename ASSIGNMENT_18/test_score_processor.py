# =========================================================
# File Name : test_score_processor.py
# Purpose   : Unit tests for ScoreProcessor
# =========================================================


# ---------------------------------------------------------
# Import pytest framework
# ---------------------------------------------------------
import pytest

# ---------------------------------------------------------
# Import ScoreProcessor class
# ---------------------------------------------------------
from score_processor import ScoreProcessor


# ---------------------------------------------------------
# Test Case 1
# Test successful score processing
# ---------------------------------------------------------
def test_valid_score_processing():

    # Create object
    processor = ScoreProcessor()

    # Call method using valid file
    result = processor.process_score_file("valid_score.txt")

    # Verify expected output
    # 4*10 = 40
    assert result == 40


# ---------------------------------------------------------
# Test Case 2
# Test missing file handling
# ---------------------------------------------------------
def test_missing_file():

    # Create object
    processor = ScoreProcessor()

    # Expect FileNotFoundError
    with pytest.raises(FileNotFoundError):

        processor.process_score_file("missing_file.txt")


# ---------------------------------------------------------
# Test Case 3
# Test invalid number format
# ---------------------------------------------------------
def test_invalid_data():

    # Create object
    processor = ScoreProcessor()

    # Expect ValueError
    with pytest.raises(ValueError):

        processor.process_score_file("invalid_score.txt")