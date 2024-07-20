def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiple(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Cannot divide by zero."


def main():
    print(".....calculator.....")

    while True:
        try:
            number1 = float(input("Enter your A value: "))
            number2 = float(input("Enter your B value: "))
        except ValueError:
            print("\n....Error....\nPlease enter a valid input value")
            continue

        print("\nChoose option:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your option (1/2/3/4/5): ")

        if choice == '1':
            print(f"The result is: {add(number1, number2)}")
        elif choice == '2':
            print(f"The result is: {sub(number1, number2)}")
        elif choice == '3':
            print(f"The result is: {multiple(number1, number2)}")
        elif choice == '4':
            print(f"The result is: {divide(number1, number2)}")
        elif choice == '5':
            print("Exiting the calculator")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
