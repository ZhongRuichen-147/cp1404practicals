MIN_LENGTH = 8

def main():
    password = get_password(MIN_LENGTH)
    print_asterisks(password)

def get_password(min_length):
    password = input("Enter Password: ")
    while len(password) < min_length:
        print(f"Password must be at least {MIN_LENGTH} characters.")
        password = input("Enter Password: ")
    return password

def print_asterisks(password):
    print("*" * len(password))

main()