while True:
    print("\nCalculator Menu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Result =", a + b)
    elif choice == 2:
        print("Result =", a - b)
    elif choice == 3:
        print("Result =", a * b)
    elif choice == 4:
        if b == 0:
            print("Error: Division by zero")
        else:
            print("Result =", a / b)
    else:
        print("Invalid choice")