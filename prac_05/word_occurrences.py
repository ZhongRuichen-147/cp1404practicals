def main():
    """Count occurrences of words in a user-entered and display them aligned."""
    text = input("Text: ")
    words = text.split()

    # Count the words using a dictionary
    word_to_count = {}
    for word in words:
        # dict.get(key, default) is a great way to handle missing keys
        word_to_count[word] = word_to_count.get(word, 0) + 1

    # Get a sorted list of the unique words (keys)
    sorted_words = sorted(word_to_count.keys())

    # Find the maximum word length to align the output neatly
    if sorted_words:
        max_length = max(len(word) for word in sorted_words)

        for word in sorted_words:
            print(f"{word:{max_length}} ; {word_to_count[word]}")


if __name__ == '__main__':
    main()