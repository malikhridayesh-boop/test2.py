def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """
    Returns the division result of two numbers.
    Raises ZeroDivisionError internally if b is 0.
    """
    if b == 0:
        raise ZeroDivisionError
    return a / b
def main():
    print("=== Welcome to the Python Function Calculator ===")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    try:
        choice = input("\nChoose an operation (1/2/3/4): ").strip()
        if choice not in ['1', '2', '3', '4']:
            print("Error: Invalid operation choice! Please run the program again and select 1, 2, 3, or 4.")
            return
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
    except ValueError:
        print("Error: Invalid input! Please enter numbers only (letters/symbols are not allowed).")
        return
    try:
        if choice == '1':
            result = add(num1, num2)
            print(f"\nResult: {num1} + {num2} = {result}")
            
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"\nResult: {num1} - {num2} = {result}")
            
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"\nResult: {num1} * {num2} = {result}")
            
        elif choice == '4':
            result = divide(num1, num2)
            print(f"\nResult: {num1} / {num2} = {result}")
            
    except ZeroDivisionError:
        print("Error: Cannot divide by zero! Math operation is mathematically undefined.")
if __name__ == "__main__":
    main()
