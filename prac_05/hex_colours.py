# Constant dictionary placed at the module level
COLOUR_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine1": "#7fffd4",
    "azure1": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque1": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}


def main():
    """Get colour names from the user and display their hex codes."""
    colour_name = input("Enter a colour name: ").lower()
    while colour_name != "":
        # Convert user input to lowercase for case-insensitive matching
        if colour_name in COLOUR_CODES:
            print(f"{colour_name} is {COLOUR_CODES[colour_name]}")
        else:
            print("Invalid colour name")
        colour_name = input("Enter a colour name: ").lower()


if __name__ == '__main__':
    main()