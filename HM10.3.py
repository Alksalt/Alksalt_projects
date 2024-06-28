#def is_even(digit):
#    return digit % 2 == 0
def is_even(digit):
    binary_digit = str(bin(digit))
    return binary_digit[-1] == "0"

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
