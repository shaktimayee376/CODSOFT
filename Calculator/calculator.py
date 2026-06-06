print("Simple Calculator")

running = True

while running:
    print("\nOperations")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("q  Quit")

    operation = input("Select operation: ")

    if operation.lower() == "q":
        print("Calculator Closed")
        running = False
        continue

    try:
        first_number = float(input("Enter first value: "))
        second_number = float(input("Enter second value: "))
    except:
        print("Please enter valid numbers.")
        continue

    if operation == "+":
        result = first_number + second_number

    elif operation == "-":
        result = first_number - second_number

    elif operation == "*":
        result = first_number * second_number

    elif operation == "/":
        if second_number == 0:
            print("Cannot divide by zero")
            continue
        result = first_number / second_number

    else:
        print("Unknown operation")
        continue

    print(f"Answer = {result}")