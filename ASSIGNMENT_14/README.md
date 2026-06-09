# Assignment 14 - Garbage Collection & Cyclic References in Python

## Question
Create a scenario where objects are "dead" but still have a reference count higher than zero, then force the Garbage Collector to clean them up.

### Implementation Steps:

1. Create a \Node\ class with \
ame\ and \link\ attributes
2. Create a cycle: Node A and Node B, set \A.link = B\ and \B.link = A\
3. Use \sys.getrefcount()\ to show both objects have multiple references
4. Use \del A\ and \del B\
5. Use the \gc\ module to show objects still exist in memory due to the cycle
6. Call \gc.collect()\ and print the number of unreachable objects collected

## Language
Python

## Files
- \garbage_collection.py\
