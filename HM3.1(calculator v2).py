x = float(input("Choose the first number: "))
y = float(input("Choose the second number: "))
z = input("Choose the arithmetic operator(+,-,/,*): ")


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
    print("Try to enter correct operator(plus, minus, multiplication,division)")
    print("Try again")