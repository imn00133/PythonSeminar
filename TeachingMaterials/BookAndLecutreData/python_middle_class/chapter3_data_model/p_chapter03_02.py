class Vector(object):
    def __init__(self, *args):
        """
        Create a vector,
        example = Vector(5, 10)
        :param args: x, y
        """
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        """
        :return: Return the vector information.
        """
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        """
        :param other: Vector
        :return: Return the vector addition of self and other
        """
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, factor):
        """
        :param factor: Vector
        :return: Return the multiple vector
        """
        return Vector(self._x * factor, self._y * factor)

    def __bool__(self):
        return bool(self._x) and bool(self._y)


v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)
print(bool(v1), bool(v2))
print(bool(v3))
