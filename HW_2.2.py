x = int(input("What's x? "))
#x =12345
piece1, piece2 = divmod(x,100)
a,piece3 = divmod(piece1,100)
b, c =divmod(piece3,10)
d,f = divmod(piece2,10)
a,b,c,d,f = f,d,c,b,a
#reversed_number = a * 10000 + b * 1000 + c * 100 + d * 10 + f

print(reversed_number)





