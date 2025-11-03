from prac_07.guitar import Guitar


def load_guitars(filename):
    """Read guitars from file and return list"""
    guitars = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            details = line.strip().split(",")
            name = details[0]
            year = int(details[1])
            cost = float(details[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


def main():
    """Read guitars from CSV file and sort"""
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    guitars.sort()

    print("Guitars Sorted by Age:")
    for guitar in guitars:
        print(guitar)


main()
