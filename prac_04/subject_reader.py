"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_data = load_data(FILENAME)
    print(subject_data)
    convey_subject_details(subject_data)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    subject_data = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        subject_data.append(parts)
        # print("----------")
    input_file.close()
    return subject_data


def convey_subject_details(subject_data):
    """Print subject details clearly in sentences."""
    for subject, teacher, number_of_students in subject_data:
        print(f"{subject} is taught by {teacher:12} and has {number_of_students:4} students")

main()
