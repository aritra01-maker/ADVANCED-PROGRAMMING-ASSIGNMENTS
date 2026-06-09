# Assignment 15 - Multithreading & Race Conditions in C (Mutex)

## Question
Write a multithreaded C program using POSIX threads (pthread) where multiple threads increment a shared global counter.

### Part 1 â€” Without Synchronization:
- Show incorrect output caused by race condition

### Part 2 â€” With Mutex:
- Use pthread_mutex_t to protect the critical section
- Produce correct final counter value

### Must Demonstrate:
- Thread creation using pthread_create()
- Synchronization using pthread_mutex_lock() and pthread_mutex_unlock()
- Thread completion using pthread_join()
- Explanation of why race condition occurs and how mutex solves it

## Language
C (POSIX Threads)

## Files
- \ace_condition.c\
- \mutex_solution.c\
