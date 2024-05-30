x = float(input("Choose the first number: "))
y = float(input("Choose the second number: "))
z = input("Choose the arithmetic operator(plus, minus, multiplication,division): ").lower()


if y == 0 and z == "division":
    print("We can not divide by 0")
    print("Try again")
elif z == "plus":
    print(x+y)
elif z == "minus":
    print(x-y)
elif z == "multiplication":
    print(x * y)
elif z == "division":
    print(x - y)
else:
    print("Try to enter correct operator(plus, minus, multiplication,division)")
    print("Try again")




