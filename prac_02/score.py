"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50

def main():
    """Run the score status program"""
    user_score = float(input("Enter Score: "))
    user_result = determine_score_result(user_score)
    print(f"User score {user_score:.1f} is {user_result}")
    if user_result == "Excellent":
        print("You get a prize!")

    random_score = random.randint(MIN_SCORE, MAX_SCORE)
    random_result = determine_score_result(random_score)
    print(f"Random: {random_score} = {random_result}")

def determine_score_result(score):
    """Determine the result string for a given score"""
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    if score >= EXCELLENT_SCORE:
        return "Excellent"
    if score >= PASSABLE_SCORE:
        return "Passable"
    return "Bad"

main()