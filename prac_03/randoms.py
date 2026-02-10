import random


print(random.randint(5, 20))  # line 1
# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# Line 1: integer; smallest 5; largest 20

print(random.randrange(3, 10, 2))  # line 2
# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
# Line 2: integers from 3, 5, 7, 9; smallest 3; largest 9; cannot produce 4

print(random.uniform(2.5, 5.5))  # line 3
# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# Line 3: float; about 2.5 to 5.5

print(random.randint(1, 100))  # random number between 1 and 100 inclusive