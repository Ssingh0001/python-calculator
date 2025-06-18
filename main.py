def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+ - * /): ")
            num2 = float(input("Enter second number: "))

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation.")
                continue

            print("\n---------")
            print(f"{num1} {op} {num2} = {result}")
            print("---------")

        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        again = input("Do you want to calculate again? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break

calculator()
