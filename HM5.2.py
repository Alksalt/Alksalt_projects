while True:
    try:
        x = float(input("Choose the first number: "))
        y = float(input("Choose the second number: "))
        z = input("Choose the arithmetic operator(+,-,/,*): ")
    except ValueError:
        print("Enter two numbers")
        continue
    if y == 0 and z == "/":
        print("We can not divide by 0")
        print("Try again")
    elif z == "+":
        print(x + y)
    elif z == "-":
        print(x - y)
    elif z == "*":
        print(x * y)
    elif z == "/":
        print(x / y)
    else:
        print("Try to enter correct operator(+,-,/,*)")
        print("Try again")

    new_it = input("Do you want to play again?(y/n): ").lower()
    if new_it != "y" and new_it != "yes":
        break