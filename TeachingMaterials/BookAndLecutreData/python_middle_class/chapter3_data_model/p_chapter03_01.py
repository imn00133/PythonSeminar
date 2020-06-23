print(int(10))
print(int)

print(dir(int))
print(dir(float))

n = 10
print(type(n))

print(n + 100)
print(n.__add__(100))
print(n.__doc__)
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))

print()


class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return f"Fruit Class Info: {self._name}, {self._price}"

    def __repr__(self):
        return f"Fruit({self._name}, {self._price})"

    def __add__(self, other):
        print('Called >> __add__')
        return self._price + other._price

    def __sub__(self, other):
        print('Called >> __sub__')
        return self._price - other._price

    def __le__(self, other):
        print('Called >> __le__')
        return self._price <= other._price

    def __ge__(self, other):
        print('Called >> __ge__')
        return self._price >= other._price


s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

print(s1._price + s2._price)
print(s1 + s2)

print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2)
print(s2 - s1)
print(s1)
print(s2)
