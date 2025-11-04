"""
Project class for Project Management Program
Estimate: 60 mins
Actual:
"""

from datetime import datetime
from project import Project


def load_projects(filename):
    """Load projects from file into list"""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()  # Read header/ skip
        for line in in_file:
            details = line.strip().split("\t")
            name = details[0]
            start_date = datetime.strptime(details[1], "%d/%m/%Y").date()
            priority = int(details[2])
            cost_estimate = float(details[3])
            completion_percentage = int(details[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


def main():
    """Load projects and display menu"""
    filename = "projects.txt"
    projects = load_projects(filename)

    for project in projects:
        print(project)


main()
