pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

length1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

print(length1)

from collections import namedtuple

Point = namedtuple('Point', 'x y')
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3, pt4)
print(pt3.x)
print(pt3[0])

length2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(length2)

Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True)

print(Point1, Point2, Point3, Point4)

p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)

print()

print(p1)
print(p2)
print(p3)
print(p4)

temp_dict = {'x': 75, 'y': 55}
p5 = Point1(**temp_dict)
print(p5)

print(p1[0] + p2[1])
print(p1.x + p2.y)

x, y = p1
print(x, y)

temp = [52, 38]
p4 = Point1._make(temp)
print(p4)

print(p1._fields, p2._fields, p3._fields)

print(p1._asdict())
print(p4._asdict())

Classes = namedtuple('Classes', ['rank', 'number'])

numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

print(numbers)
print(ranks)

students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))
print(students)

students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
             for number in [str(n) for n in range(1, 21)]
             ]

print(len(students2))
print(students2)

for s in students2:
    print(s)
