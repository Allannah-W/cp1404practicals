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


def add_new_guitar():
    """Add new guitars via prompt and add to list"""
    new_guitars = []
    name = input("Name: ").strip()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        new_guitars.append(guitar)
        print(f"{guitar.name} added")
        name = input("Name: ").strip()
    return new_guitars


def save_guitars(filename, guitars):
    """Update list of guitars in CSV file"""
    with open(filename, "w", encoding="utf-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def main():
    """Read guitars from CSV file and sort"""
    filename = "guitars.csv"
    guitars = load_guitars(filename)
    new_guitars = add_new_guitar()
    guitars.extend(new_guitars)

    guitars.sort()

    print("Guitars Sorted by Age:")
    for guitar in guitars:
        print(guitar)

    save_guitars(filename, guitars)


main()
