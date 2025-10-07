usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
             'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
             'ExecState', 'InteractiveConsole', 'InterpreterInterface',
             'StartServer', 'bob']


def main():
    numbers = get_numbers()
    print_numbers_information(numbers)

    username = get_username()
    check_for_authorised_user(username)


def get_numbers():
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers


def print_numbers_information(numbers):
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


def get_username():
    username = input("Username: ")
    return username


def check_for_authorised_user(username):
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
