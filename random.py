#!/usr/bin/env python3
"""Random utilities module with demo functions."""

import random as rnd  # avoid import-self when your file is named random.py

class RandomUtils:
    """Provides various random-related utilities."""

    def __init__(self):
        """Initialize without a seed set."""
        self.seed = None

    def set_seed(self, seed_val):
        """Set the RNG seed for reproducibility."""
        prev = self.seed
        self.seed = seed_val
        rnd.seed(seed_val)
        return prev

    def roll_die(self, sides=6):
        """Simulate rolling an N-sided die."""
        return rnd.randint(1, sides)

    def random_float(self, lower=0.0, upper=1.0):
        """Return a floating-point number in [lower, upper]."""
        return rnd.uniform(lower, upper)

    def random_choice(self, items):
        """Pick one element at random from a non-empty sequence."""
        if not items:
            raise ValueError("Cannot choose from an empty sequence")
        return rnd.choice(items)

    def estimate_pi(self, iterations=10000):
        """Estimate π using the Monte Carlo method."""
        inside = 0
        for _ in range(iterations):
            x_val = rnd.random()
            y_val = rnd.random()
            if x_val * x_val + y_val * y_val <= 1:
                inside += 1
        return 4 * inside / iterations

def main():
    """Demo entry point."""
    utils = RandomUtils()
    utils.set_seed(42)
    print("10-sided die:", utils.roll_die(10))
    print("Float 5–10:", utils.random_float(5, 10))
    print("Choice:", utils.random_choice(["red", "green", "blue"]))
    print("Pi ≈", utils.estimate_pi(5000))

if __name__ == "__main__":
    main()
