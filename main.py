def calculate(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return None

def calculator():
    valid_ops = {"+", "-", "*", "/"}
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Choose an operator (+, -, *, /): ").strip()
            if op not in valid_ops:
                print("Invalid operator. Please choose from +, -, *, /.")
                continue
            num2 = float(input("Enter second number: "))
            result = calculate(num1, op, num2)

            print("\n..............")
            print(f"{num1} {op} {num2} = {result}")
        except ValueError:
            print("Please enter a valid number.")
            continue

        again = input("Do you want to calculate again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break

calculator()
