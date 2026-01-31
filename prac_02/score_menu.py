MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

def main():
    """Run the score menu program"""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_score_result(score)
            print(result)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell!")

def get_valid_score():
    """Get a valid score from the user"""
    score = float(input("Enter score (0-100): "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("Invalid score")
        score = float(input("Enter score (0-100): "))
    return score

def determine_score_result(score):
    """Determine the result string for a given score"""
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    if score >= EXCELLENT_SCORE:
        return "Excellent"
    if score >= PASSABLE_SCORE:
        return "Passable"
    return "Bad"

def print_stars(score):
    """Print stars matching the score"""
    print("*" * int(score))

main()