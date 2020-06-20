def factorial(n):
    """
    Factorial Function -> n: int
    """
    if n == 1: # n < 2
        return 1
    return n * factorial(n - 1)


class A:
    pass


print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))
print(dir(factorial))

print(set(dir(factorial)) - set(dir(A)))
print(factorial.__name__)
print(factorial.__code__)

print()

var_func = factorial
print(var_func)
print(var_func(10))
print(list(map(var_func, range(1, 10))))

print(list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))
print([var_func(i) for i in range(1, 6) if i % 2])

print()

from functools import reduce
from operator import add

print(reduce(add, range(1, 11)))
print(sum(range(1, 11)))

print(reduce(lambda x, t: x + t, range(1, 11)))

print()

print(callable(str), callable(A), callable(var_func), callable(factorial), callable(list), callable(3.14))

print()

from operator import mul
from functools import partial

print(mul(10, 10))
five = partial(mul, 5)
six = partial(five, 6)

print(five)
print(five(10))
print(five(100))

print(six())
# print(six(10))

print([five(i) for i in range(1, 11)])
print(list(map(five, range(1, 11))))
