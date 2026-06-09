from typing import List, Dict, Set
from collections import defaultdict
from functools import reduce
import random
import time


# --------------------------------------------------
# Function 1: Total Time Per User (Using reduce)
# --------------------------------------------------
def total_time_per_user(logs: List[Dict[str, object]]) -> Dict[str, float]:
    """
    Returns total screen time per user using reduce().
    """

    def reducer(acc: Dict[str, float], log: Dict[str, object]) -> Dict[str, float]:
        user = log["user"]
        duration = log["duration"]
        acc[user] = acc.get(user, 0.0) + float(duration)
        return acc

    return reduce(reducer, logs, {})


# --------------------------------------------------
# Function 2: Most Active Users (Top K)
# --------------------------------------------------
def most_active_users(logs: List[Dict[str, object]], k: int) -> List[str]:
    """
    Returns top k users based on total activity time.
    """

    totals = total_time_per_user(logs)

    # Sort dictionary keys by value descending
    sorted_users = sorted(
        totals,
        key=lambda user: totals[user],
        reverse=True
    )

    return sorted_users[:k]


# --------------------------------------------------
# Function 3: Unique Actions
# --------------------------------------------------
def unique_actions(logs: List[Dict[str, object]]) -> Set[str]:
    """
    Returns unique set of actions using set comprehension.
    """
    return {log["action"] for log in logs}


# --------------------------------------------------
# Generate Dummy Activity Logs
# --------------------------------------------------
def generate_logs(num_users: int, num_logs: int) -> List[Dict[str, object]]:

    users = [f"ROLL_{1000+i}" for i in range(num_users)]

    actions = [
        "Instagram",
        "YouTube",
        "WhatsApp",
        "Chrome",
        "Facebook",
        "Netflix",
        "VSCode",
        "Telegram"
    ]

    logs = [
        {
            "user": random.choice(users),
            "action": random.choice(actions),
            "duration": round(random.uniform(1, 120), 2)
        }
        for _ in range(num_logs)
    ]

    return logs


# --------------------------------------------------
# Pretty Printing Utilities
# --------------------------------------------------
def print_separator():
    print("=" * 60)


def print_totals(totals: Dict[str, float]):
    print_separator()
    print("📊 TOTAL SCREEN TIME PER USER")
    print_separator()

    for user, time_spent in sorted(
            totals.items(),
            key=lambda x: x[1],
            reverse=True):

        print(f"{user:<15} | {time_spent:>8.2f} minutes")

    print_separator()


def print_top_users(top_users: List[str], totals: Dict[str, float]):
    print("\n🏆 TOP ACTIVE USERS")
    print_separator()

    for rank, user in enumerate(top_users, start=1):
        print(f"{rank}. {user:<15} -> {totals[user]:.2f} minutes")

    print_separator()


def print_unique_actions(actions: Set[str]):
    print("\n🌐 UNIQUE ACTIONS PERFORMED")
    print_separator()

    for action in sorted(actions):
        print(f"- {action}")

    print_separator()


# --------------------------------------------------
# MAIN EXECUTION
# --------------------------------------------------
if __name__ == "__main__":

    print_separator()
    print("📱 ACTIVITY LOG ANALYZER")
    print_separator()

    num_users = int(input("Enter number of users: "))
    num_logs = int(input("Enter number of activity records: "))
    k = int(input("Enter value of K (Top K users): "))

    logs = generate_logs(num_users, num_logs)

    print("\n🔎 Sample Logs (First 5 Records)")
    print_separator()
    for log in logs[:5]:
        print(log)
    print_separator()

    # -----------------------------------
    # Total Time Per User
    # -----------------------------------
    start = time.time()
    totals = total_time_per_user(logs)
    end = time.time()

    print_totals(totals)
    print(f"⏱ Time taken: {(end - start):.6f} seconds")

    # -----------------------------------
    # Top K Users
    # -----------------------------------
    start = time.time()
    top_users = most_active_users(logs, k)
    end = time.time()

    print_top_users(top_users, totals)
    print(f"⏱ Time taken: {(end - start):.6f} seconds")

    # -----------------------------------
    # Unique Actions
    # -----------------------------------
    actions = unique_actions(logs)
    print_unique_actions(actions)