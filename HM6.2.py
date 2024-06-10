while True:
    x = int(input("Enter a number between 0 - 8640000: "))
    if 0 <= x <= 8640000:
        break
    else:
        print("Enter a valid number")

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
if days == 1:
    print(f"Converted time: {days} day:{hours}:{minutes}:{seconds}")
else:
    print(f"Converted time: {days} days:{hours}:{minutes}:{seconds}")