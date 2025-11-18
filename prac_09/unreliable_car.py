from car import Car
import random


class UnreliableCar(Car):
    """Represent an unreliable car object."""

    def __init__(self, name, fuel, reliability):
        """Initialise an unreliable car instance"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance.
        Drive given distance if car reliability is more than
        random chance"""

        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
