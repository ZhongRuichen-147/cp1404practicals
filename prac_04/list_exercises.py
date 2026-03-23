def main():
    """Get numbers from user and display formatted statistics."""
    numbers = []
    for i in range(5):
        number = float(input("Number: "))
        numbers.append(number)

    display_statistics(numbers)


def display_statistics(numbers):
    """Calculate and print statistics from a list of numbers."""
    print(f"The first number is {numbers[0]:.0f}")
    print(f"The last number is {numbers[-1]:.0f}")
    print(f"The smallest number is {min(numbers):.0f}")
    print(f"The largest number is {max(numbers):.0f}")

    average = sum(numbers) / len(numbers)
    print(f"The average of the numbers is {average}")


main()