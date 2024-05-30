main_list = [9,9,9,9,9,9]
x = len(main_list) // 2
y = len(main_list)
if y % 2 ==0:
    pass
else:
    x +=1
lst1 = main_list[:x]
lst2 = main_list[x:]
main_list = [lst1,lst2]
print(main_list)