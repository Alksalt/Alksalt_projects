x = input("Enter a number: ")

while len(x) > 1:
    lst = [int(i) for i in x]

    num1 = 1

    for num in lst:
        num1 *= num
    x = str(num1)
print(x)


