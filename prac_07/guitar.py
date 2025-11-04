"""
Guitar Exercise
Estimate: 30mins
Actual: 40mins
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Represent guitar object"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string of guitar information"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Compare ages of guitars"""
        return self.year < other.year

    def get_age(self):
        """Return age of guitar"""
        current_year = 2025
        return current_year - self.year

    def is_vintage(self):
        """Return true if guitar is over 50 years old"""
        return self.get_age() >= 50
