def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    i = 0
    new_begin = begin
    while i < end:
        yield new_begin
        new_begin = func(new_begin)
        i += 1


    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """

from inspect import isgenerator
gen = some_gen(2, 4, pow)

assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
