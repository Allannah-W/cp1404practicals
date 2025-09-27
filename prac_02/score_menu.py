def main():
    score = get_valid_score()

    menu = """(G)et a valid score
    (P)rint result
    (S)how stars
    (Q)uit"""
    print(menu)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_result(score))
        elif choice == "S":
            print(show_stars(score))
        else:
            print("Invalid choice")
        print(menu)
        choice = input(">>> ").upper()
    print("Farewell.")


def get_valid_score():
    """Get and Validate Score"""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = int(input("Score: "))
    return score


def determine_result(score):
    """Determine associated result of score"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


def show_stars(score):
    """Convert score into str of *"""
    return score * "*"


main()
