def main():
    print("Upgraded Calculator Program")

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    input_choice()
    option_chooser(a, b)


def input_choice():
    print("Do you want calculator or indicer?")
    print("Type: calc or indicer")


def option_chooser(a, b):
    choice = input("Enter your choice: ").lower()

    if choice == "calc":
        calculator(a, b)

    elif choice == "indicer":
        indicer(a)

    else:
        print("Invalid choice")


def calculator(a, b):
    operation_choice_calc()

    op = int(input("Enter operation number: "))

    if op == 1:
        addition(a, b)

    elif op == 2:
        subtraction(a, b)

    elif op == 3:
        multiplication(a, b)

    elif op == 4:
        division(a, b)

    elif op == 5:
        remainder(a, b)

    else:
        print("No operation found")


def indicer(a):
    operation_choice_indicer()

    op = int(input("Enter operation number: "))

    if op == 1:
        square(a)

    elif op == 2:
        cube(a)

    elif op == 3:
        quad(a)

    else:
        print("No operation found")


def addition(a, b):
    print("Answer:", a + b)


def subtraction(a, b):
    print("Answer:", a - b)


def multiplication(a, b):
    print("Answer:", a * b)


def division(a, b):
    print("Answer:", a / b)


def remainder(a, b):
    print("Answer:", a % b)


def square(a):
    print("Square is:", pow(a, 2))


def cube(a):
    print("Cube is:", pow(a, 3))


def quad(a):
    print("Quad is:", pow(a, 4))


def operation_choice_calc():
    print("""
1] Addition (+)
2] Subtraction (-)
3] Multiplication (*)
4] Division (/)
5] Remainder (%)
""")


def operation_choice_indicer():
    print("""
1] Square
2] Cube
3] Quad
""")


main()
