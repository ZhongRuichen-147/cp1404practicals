def main():
    """Display income report for incomes over a given number of months."""
    numbers_of_months = int(input("How many mothes? "))
    incomes = get_incomes(numbers_of_months)
    display_income_report(incomes)

def get_incomes(number_of_months):
    """Get income amounts for each month."""
    incomes = []

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    return incomes

def display_income_report(incomes):
    """Display income report with cumulative totals."""
    print("\nIncome Report\n-------------")

    total = 0

    for month_number in range(1, len(incomes) + 1):
        income = incomes[month_number - 1]
        total += income
        print(f"Month {month_number:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()