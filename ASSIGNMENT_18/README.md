# Assignment 18 - File Handling with Exception Management

## Question
Create a data utility class that reads an integer score from a text file, multiplies it by 10, and handles all errors gracefully.

### If Java:
- Class: ScoreProcessor
- Method:
  \\\java
  public int processScoreFile(String filePath)
  \\\
- Use try-catch-finally or try-with-resources
- Catch FileNotFoundException and NumberFormatException specifically
- finally block prints "File cleanup completed"
- JUnit 5 tests:
  - Successful calculation with valid file
  - assertThrows for missing file

### If Python:
- Class: ScoreProcessor
- Method:
  \\\python
  def process_score_file(self, file_path: str) -> int
  \\\
- Use try-except-else-finally
- Catch FileNotFoundError and ValueError
- else block prints "Data processed successfully"
- finally block prints "File cleanup completed"
- pytest suite:
  - Test successful calculation
  - pytest.raises for missing file

### Must Have:
1. Exception Handling & Structure (multi-catch, cleanup block always runs)
2. Core Logic & Input Validation (read file, parse integer, multiply by 10)
3. Unit Testing (happy path + error path)

## Language
Java or Python

## Files
- \ScoreProcessor.java\ / \score_processor.py\
- \ScoreProcessorTest.java\ / \	est_score_processor.py\
