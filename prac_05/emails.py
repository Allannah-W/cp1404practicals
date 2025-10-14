"""
Emails
Estimate: 35mins
Actual:   32mins
"""

email_to_name = {}

email = input("Email: ")
while email != "":
    name = " ".join(email.split("@")[0].replace(".", " ").split()).title()

    name_check = input(f"Is your name {name}? (y/n)").lower()

    if name_check not in ('', 'y'):
        name = input("Name: ").title()

    email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
