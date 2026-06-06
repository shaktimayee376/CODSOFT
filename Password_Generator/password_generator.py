import random
import string

print("Password Creator")

while True:
    choice = input("\nEnter password length (or 0 to exit): ")

    try:
        size = int(choice)

        if size == 0:
            print("Program Closed")
            break

        if size < 8:
            print("Choose at least 8 characters.")
            continue

        chars = (
            string.ascii_letters +
            string.digits +
            "!@#$%^&*?"
        )

        password_list = []

        password_list.append(random.choice(string.ascii_lowercase))
        password_list.append(random.choice(string.ascii_uppercase))
        password_list.append(random.choice(string.digits))
        password_list.append(random.choice("!@#$%^&*?"))

        for _ in range(size - 4):
            password_list.append(random.choice(chars))

        random.shuffle(password_list)

        final_password = "".join(password_list)

        print("Your Password:", final_password)

    except ValueError:
        print("Please enter a valid number.")