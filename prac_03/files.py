# 1
name = input("Name:")
name_file = open("name.txt", 'w')
print(name, file=name_file)
name_file.close()

# 2
name_file = open("name.txt", 'r')
content = name_file.read().strip()
print(f"Hi {content}!")
name_file.close()

# 3
with open("numbers.txt", "r") as numbers_file:
    first_number = int(numbers_file.readline())
    second_number = int(numbers_file.readline())

    result = first_number + second_number
    print(result)

# 4
total = 0
with open("numbers.txt","r") as numbers_file:
    for line in numbers_file:
        number = int(line)
        total = total + number
    print(total)
