FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2

def main():
    """Read data file and print details about Wimbledon champions and countries."""
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def get_records(filename):
    """Get records from file in list of lists form."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove the header row
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    """Create dictionary of champions and set of countries from records."""
    champion_to_count = {}
    countries = set()
    for record in records:
        country = record[INDEX_COUNTRY]
        champion = record[INDEX_CHAMPION]

        countries.add(country)   # Add country to the set (sets automatically ignore duplicates)

        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1

    return champion_to_count, countries   # Count the champions using dictionary get() method


def display_results(champion_to_count, countries):
    """Display champions and winning countries neatly."""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(f"{name} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    # Sort the set of countries into an alphabetical list, then join with comma
    print(", ".join(sorted(countries)))


if __name__ == '__main__':
    main()