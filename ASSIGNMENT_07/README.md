# Assignment 07 - Activity Log Analyzer in Python

## Question
Develop an activity log analyzer in Python.

Each activity record:
\\\python
{
    "user": str,        # roll numbers of students
    "action": str,      # online activities (apps, websites visited)
    "duration": float   # screen time for each activity
}
\\\

### Required Functions:
\\\python
def total_time_per_user(logs: list[dict]) -> dict[str, float]
def most_active_users(logs: list[dict], k: int) -> list[str]
def unique_actions(logs: list[dict]) -> set[str]
\\\

### Must Use:
- dict, set, and list
- Comprehensions where appropriate
- sorted() with key
- Avoid explicit loops where possible
- Typing annotations
- defaultdict optionally
- reduce() to compute total activity time

### Complexity Analysis:
- Time complexity for computing top K users
- Space complexity of storing intermediate results

## Language
Python

## Files
- \ctivity_analyzer.py\
