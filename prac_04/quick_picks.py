import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    number_of_picks = get_number_of_picks()
    for i in range(number_of_picks):
        quick_pick = make_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))


def get_number_of_picks():
    """Get user input for number of quick picks required"""
    number_of_picks = int(input("How many picks?: "))
    return number_of_picks


def make_quick_pick():
    """Make quick pick of random numbers between min and max numbers"""
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)

        if number not in quick_pick:
            quick_pick.append(number)

    quick_pick.sort()
    return quick_pick


main()
