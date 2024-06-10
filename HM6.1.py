import string
x = input("Enter 2 english letters(from - to): ")
str_all = string.ascii_letters
ind1 = x[0]
ind2 = x[2]
str_1 = str_all.find(ind1)
str_2 = str_all.find(ind2) + 1
print(str_all[str_1:str_2])