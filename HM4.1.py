lst = [0,3,4,5,0,0,5,6,60,7,676]

for i in lst:
    if i == 0:
        lst.remove(0)
        lst.append(i)
print(lst)