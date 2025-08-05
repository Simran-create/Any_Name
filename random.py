#!/usr/bin/env python3
"""
Random utilities module
"""

import random
import math

class RandomUtils:
    """Provides various random-related utility functions."""

    def __init__(self):
        self.seed = None

    def set_seed(self, seed_val):
        """Set the seed for reproducibility."""
        self.seed = seed_val
        random.seed(seed_val)

    def roll_die(self, sides=6):
        """Simulate a die roll."""
        return random.randint(1, sides)

    def random_float(self, lower=0.0, upper=1.0):
        """Get a random float in range."""
        return random.uniform(lower, upper)

    def random_choice(self, items):
        """Pick a random item from a list."""
        return random.choice(items)

    def estimate_pi(self, iterations=10000):
        """Use Monte Carlo method to estimate Pi."""
        inside = 0
        for _ in range(iterations):
            x, y = random.random(), random.random()
            if x**2 + y**2 <= 1:
                inside += 1
        return 4 * inside / iterations


if __name__ == "__main__":
    utils = RandomUtils()
    utils.set_seed(42)
    print("Rolling a 10-sided die:", utils.roll_die(10))
    print("Random float between 5 and 10:", utils.random_float(5, 10))
    print("Random choice from list:", utils.random_choice(['apple', 'banana', 'cherry']))
    print("Estimated Pi:", utils.estimate_pi(5000))
