def calculator():
    
    while True:
        try:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
        except ValueError:
            print("\nInvalid input! Please enter valid numeric values.\n")
            continue

        print("\nChoose an operation:")
        print("[1] Addition (+)")
        print("[2] Subtraction (-)")
        print("[3] Multiplication (*)")
        print("[4] Division (/)")
        print("[5] Exit Calculator")

        operation = input("\nEnter your choice between 1 to 5: ")

        if operation == "1":
            result = int(num1 + num2) if (num1 + num2).is_integer() else num1 + num2
            print(f"\nThe result of adding {num1} and {num2} is: {result}\n")
        elif operation == "2":
            result = int(num1 - num2) if (num1 - num2).is_integer() else num1 - num2
            print(f"\nThe result of subtracting {num2} from {num1} is: {result}\n")
        elif operation == "3":
            result = int(num1 * num2) if (num1 * num2).is_integer() else num1 * num2
            print(f"\nThe result of multiplying {num1} and {num2} is: {result}\n")
        elif operation == "4":
            if num2 != 0:
                result = int(num1 / num2) if (num1 / num2).is_integer() else num1 / num2
                print(f"\nThe result of dividing {num1} by {num2} is: {result}\n")
            else:
                print("\nError: Division by zero is not allowed.\n")
        elif operation == "5":
            print("\nThank you for using the Simple Calculator!\n")
            break
        else:
            print("\nInvalid operation choice! Please select a valid option between 1 to 5.\n")

calculator()
