import keyword
import string
str_punct =" !\"#$%&\')(*+,-./:;<=>?@\\][^`|}{~"

while True:
    variable = input("What's a name for variable?: ").lower()
    if variable[0].isdigit():
        print("Invalid")
        break
    if variable in keyword.kwlist:
        print("Invalid")
        break
    if any(i in str_punct for i in variable):
        print("Invalid")
        break
    #if len(variable) > 140:
        #variable = variable[:141]
    if variable[0] == "_" or variable[-1] == "_":
        print("Invalid")
        break
    if "__" in variable:
        print("Invalid")
        break


    print("Valid")
    print(variable)
    break