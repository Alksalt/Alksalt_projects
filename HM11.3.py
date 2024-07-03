
###1
#def is_even(digit):
#    last_str_digit = int(str(digit)[-1])
#    return bin(last_str_digit)[-1] == "0"

###2
def is_even(digit):
    last_str_digit = str(digit)[-1]
    return last_str_digit in "02468"






assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print("OK")