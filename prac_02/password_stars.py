password = input("Password: ")

while len(password) < 10:
    print("Password is too short.")
    password = input("Password: ")
else:
    print(len(password) * "*")
