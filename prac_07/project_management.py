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


def display_menu():
    """Display the menu."""
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def save_projects(filename, projects):
    """Save projects to tab-delimited file"""
    with open(filename, "w", encoding="utf-8") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)  #print header
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                  f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def main():
    """Load projects and display menu"""
    filename = "projects.txt"
    projects = load_projects(filename)

    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} from {filename}")

    choice = ""
    while choice != "Q":
        display_menu()
        choice = input(">>>").upper()
        if choice == "L":
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} from {filename}")
        elif choice == "S":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "D":
            display_projects()
        elif choice == "F":
            filter_projects_by_date()
        elif choice == "A":
            add_new_project()
        elif choice == "U":
            update_project()
        elif choice == "Q":
            save = input("Would you like to save to the default file before quitting? (y/n): ").lower()
            if save == "y":
                save_projects()
        else:
            print("Invalid choice")
    print("Thank you for using custom-built project management software.")


main()
