MIN_LENGTH = 8


def main():
    """Run the password check program"""
    password = get_password(MIN_LENGTH)
    print_asterisks(password)

def get_password(min_length):
    """Get a valid password from the user"""
    password = input("Enter Password: ")
    while len(password) < min_length:
        print(f"Password must be at least {MIN_LENGTH} characters.")
        password = input("Enter Password: ")
    return password

def print_asterisks(password):
    """Print asterisks matching the length of the password"""
    print("*" * len(password))

main()