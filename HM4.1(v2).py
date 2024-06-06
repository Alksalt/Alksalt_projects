lst = [0,3,4,5,0,0,5,6,60,7,676]

zero_lst = lst.count(0)
new_lst = [i for i in lst if i !=0] + [0] * zero_lst
print(new_lst)

