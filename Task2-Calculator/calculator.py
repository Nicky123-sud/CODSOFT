def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    try:
        # User inputs the operation choice
        choice = input("Enter the operation (+, -, *, /): ").strip()
        if choice not in ['+', '-', '*', '/']:
            print("Invalid choice. Please choose a valid operation.")
            return
        
        # User inputs two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Perform the selected operation and print the result
        if choice == '+':
            result = num1 + num2
            operation = "Addition"
        elif choice == '-':
            result = num1 - num2
            operation = "Subtraction"
        elif choice == '*':
            result = num1 * num2
            operation = "Multiplication"
        elif choice == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
            operation = "Division"
        
        # Display the result
        print(f"\n{operation} Result: {num1} {choice} {num2} = {result}")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the calculator
calculator()
