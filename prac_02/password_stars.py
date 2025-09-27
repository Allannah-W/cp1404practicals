def main():
    password = get_password()
    convert_password(password)


def get_password():
    password = input("Password: ")
    while len(password) < 10:
        print("Password is too short.")
        password = get_password()
    return password


def convert_password(password):
    print(len(password) * "*")


main()
