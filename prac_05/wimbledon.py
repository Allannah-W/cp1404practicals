"""
Wimbledon
Estimated: 35min
Actual: 40mins
"""


def main():
    filename = "wimbledon.csv"
    data = read_file(filename)
    countries, champion_to_wins = process_data(data)
    display_results(countries, champion_to_wins)


def read_file(filename):
    """Read file and return rows of data in a list of lists"""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            row = line.strip().split(",")
            data.append(row)
    return data


def process_data(data):
    """Return set of countries and champion-wins dictionary"""
    countries = set()
    champion_to_wins = {}

    for line in data:
        champion = line[2]
        country = line[1]

        countries.add(country)

        if champion in champion_to_wins:
            champion_to_wins[champion] += 1
        else:
            champion_to_wins[champion] = 1

    return countries, champion_to_wins


def display_results(countries, champion_to_wins):
    """Display champions wins and countries"""
    print("Wimbledon Champions")
    for champion in champion_to_wins:
        print(f"{champion}: {champion_to_wins[champion]}")

    print(f"These {len(countries)} countries have won Wimbledon:")
    countries = ", ".join(sorted(countries))
    print(countries)


main()
