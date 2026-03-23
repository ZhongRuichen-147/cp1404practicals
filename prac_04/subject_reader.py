"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    data = load_data(FILENAME)
    display_subjects(data)


def load_data(filename):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_data = []
    input_file = open(filename, "r")
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subject_data.append(parts)
    input_file.close()

    return subject_data


def display_subjects(subjects):
    """Display the subject data nicely formatted."""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:<12} and has {subject[2]:>3} students")


main()