def main():
    """Get emails and names from the user, then display them."""
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        expected_name = extract_name(email)
        confirmation = input(f"Is your name {expected_name}? (Y/n) ").strip().lower()

        # If user presses Enter (blank) or enters "y", keep the expected_name
        if confirmation != "" and confirmation != "y":
            expected_name = input("Name: ")

        email_to_name[email] = expected_name
        email = input("Email: ")

    # Print the formatted list of names and emails
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name(email):
    """Extract an expected name from an email address."""
    # Split the email at "@" and take the first part (the username)
    prefix = email.split("@")[0]
    # Split the username at "." if it exists
    parts = prefix.split(".")
    # Join the parts with a space and convert to title case
    name = " ".join(parts).title()
    return name

if __name__ == '__main__':
    main()