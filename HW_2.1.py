x = int(input("What's x? "))

part1, part2 = divmod(x,100)
first,second = divmod(part1,10)
third, forth = divmod(part2,10)
print(first)
print(second)
print(third)
print(forth)