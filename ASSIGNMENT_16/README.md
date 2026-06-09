# Assignment 16 - Thread Synchronization with Semaphores/Condition Variables in C

## Question
Develop a multithreaded C program using POSIX threads where multiple threads coordinate access to a shared resource using semaphores or condition variables.

### Possible Implementations:
- Producer-Consumer system
- Limited resource access system
- Thread scheduling simulation

### Must Demonstrate:
- Threads wait correctly when resource is unavailable
- Threads continue only when signaled
- Proper synchronization and safe shared-memory access
- Thread communication using:
  - sem_wait(), sem_post()
  - pthread_cond_wait(), pthread_cond_signal()
- Print messages showing thread execution order
- Explain how synchronization prevents inconsistent behavior

## Language
C (POSIX Threads)

## Files
- \producer_consumer.c\ or \	hread_sync.c\
