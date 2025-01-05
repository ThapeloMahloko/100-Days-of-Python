"""
Heads or tails Program
"""
# Import random module
import random

# Random number 
random_head_or_tail = random.randint(0, 1)

# Head or Tails Selector
if random_head_or_tail == 0:
    print("Head")
else:
    print("Tail")