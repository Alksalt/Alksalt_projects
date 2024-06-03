import random

lst = []
for i in range(random.randint(3,10)):
    lst.append(random.randint(10,1000))
new_list = [lst[0],lst[2],lst[-2]]
#new_list = [lst[0:3:2],lst[-2:-1:2]]
print(lst)
print(new_list)

lst1 = [random.randint(1,99) for i in range(random.randint(3,10)) ]
new_list1 = [lst1[0],lst1[2],lst1[-2]]
print(lst1)
print(new_list1)