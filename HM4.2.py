lst = [1,2,3,4,2,3,5,6,7]
even_lst = lst[::2]
num = 0
for i in even_lst:
    num += i
if len(lst) > 0:
    final_num = num * lst[-1]
else:
    final_num = 0
print(final_num)
