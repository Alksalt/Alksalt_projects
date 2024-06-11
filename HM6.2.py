while True:
    x = int(input("Введіть номер між 0 - 8640000: "))
    if 0 <= x <= 8640000:
        break
    else:
        print("Введіть коректний номер")

#converting
days, other1 = divmod(x, 86400)
hours, other2 = divmod(other1, 3600)
minutes, seconds = divmod(other2, 60)

#from in to str
minutes = str(minutes).zfill(2)
hours = str(hours).zfill(2)
#days = str(days).zfill(2)
seconds = str(seconds).zfill(2)

#day/days
if days < 21:
    if days == 1:
        print(f"Конвертований час: {days} день:{hours}:{minutes}:{seconds}")
    elif 1 < days < 5:
        print(f"Конвертований час: {days} дні:{hours}:{minutes}:{seconds}")
    else:
        print(f"Конвертований час: {days} днів:{hours}:{minutes}:{seconds}")
else:
    days_str = str(days)
    if days_str[-1] == "1":
        print(f"Конвертований час: {days} день:{hours}:{minutes}:{seconds}")
    elif days_str[-1] in "234":
        print(f"Конвертований час: {days} дні:{hours}:{minutes}:{seconds}")
    else:
        print(f"Конвертований час: {days} днів:{hours}:{minutes}:{seconds}")



# print(f"Converted time: {days} day:{hours}:{minutes}:{seconds}")