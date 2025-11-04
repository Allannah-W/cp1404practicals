"""
Project class for Project Management Program
Estimate: 60 mins
Actual:
"""

from datetime import datetime


class Project:

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """String representation of Project"""
        return (f"{self.name}, Start: {self.start_date.strftime('%d/%m/%Y')}, Priority: {self.priority}, "
                f"Cost Estimate: ${self.cost_estimate:.2f}, Completion Percentage: {self.completion_percentage}%")

    def __lt__(self, other):
        """Enable sorting by priority"""
        return self.priority < other.priority

    def is_complete(self):
        """Return true if project complete"""
        return self.completion_percentage == 100
