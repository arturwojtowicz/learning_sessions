# Imagine, that building has a 1 000 000 floors and You have only 6 balls.
# If You throw a ball from too high, the ball would break, then You have only 5 balls.
# If You throw a ball from a too low floor, the ball wont break, You can throw this ball again.
# Find a "Breaking Point" of the ball, so the highest floor, where ball will NOT crash.
# Try to find it in as less tries as possible

import random

def building(floor: int) -> int: ...


building(random.choice(range(1000001)))
