import sys
import gc

# ----------------------------------------
# Node Class
# ----------------------------------------

class Node:

    def __init__(self, name):
        self.name = name
        self.link = None

    def __del__(self):
        print(f"{self.name} is being garbage collected")


# ----------------------------------------
# Enable GC Debugging
# ----------------------------------------

gc.set_debug(gc.DEBUG_SAVEALL)

# ----------------------------------------
# Program Start
# ----------------------------------------

print("======================================")
print("   GARBAGE COLLECTION DEMONSTRATION")
print("======================================\n")

input("Press ENTER to create two nodes...")

# ----------------------------------------
# Create Nodes
# ----------------------------------------

A = Node("Node A")
B = Node("Node B")

print("\nTwo nodes created successfully.")

input("\nPress ENTER to create a circular reference...")

# Create Cycle
A.link = B
B.link = A

print("\nCircular reference created:")
print("Node A -> Node B")
print("Node B -> Node A")

# ----------------------------------------
# Reference Counts
# ----------------------------------------

input("\nPress ENTER to check reference counts...")

print("\nReference Counts:")
print(f"Reference count of A = {sys.getrefcount(A)}")
print(f"Reference count of B = {sys.getrefcount(B)}")

# ----------------------------------------
# Store Object IDs
# ----------------------------------------

a_id = id(A)
b_id = id(B)

# ----------------------------------------
# Delete References
# ----------------------------------------

input("\nPress ENTER to delete original references...")

del A
del B

print("\nVariables A and B deleted.")
print("But objects may still exist due to circular reference.")

# ----------------------------------------
# Investigation
# ----------------------------------------

input("\nPress ENTER to investigate memory...")

found_a = False
found_b = False

for obj in gc.get_objects():

    if id(obj) == a_id:
        found_a = True

    if id(obj) == b_id:
        found_b = True

print("\nInvestigation Result:")
print("Node A still exists in memory:", found_a)
print("Node B still exists in memory:", found_b)

# ----------------------------------------
# Garbage Collection
# ----------------------------------------

input("\nPress ENTER to force Garbage Collection...")

print("\nRunning gc.collect()...\n")

unreachable = gc.collect()

# ----------------------------------------
# Final Output
# ----------------------------------------

print("\nGarbage Collection Complete.")

print(f"\nUnreachable objects collected = {unreachable}")

print("\nProgram Finished Successfully.")