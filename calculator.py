def add(a, b):
    return round(a + b, 2)

def subtract(a, b):
    return round(a - b, 2)

def multiply(a, b):
    return round(a * b, 2)

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return round(a / b, 2)


print("Simple Calculator")

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose operation (1/2/3/4): ").strip()

    if choice not in ['1', '2', '3', '4']:
        print("Please enter a valid number (1-4)")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter numbers only")
        continue

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))

    break