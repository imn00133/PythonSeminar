print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*(divmod(100, 9)))

print()

x, y, *rest = range(10)
print(x, y, rest)

x, y, *rest = range(2)
print(x, y, rest)

x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

print()

l1 = (15, 20, 25)
m1 = [15, 20, 25]

print(l1, id(l1))
print(m1, id(m1))

l1 = l1 * 2
m1 = m1 * 2

print(l1, id(l1))
print(m1, id(m1))

l1 *= 2
m1 *= 2

print(l1, id(l1))
print(m1, id(m1))

print()

f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print('sorted -', sorted(f_list))
print('sorted -', sorted(f_list, reverse=True))
print('sorted -', sorted(f_list, key=len))
print('sorted -', sorted(f_list, key=lambda x: x[-1]))
print('sorted -', sorted(f_list, reverse=True, key=lambda x: x[-1]))
print('sorted -', f_list)

print('sort -', f_list.sort(), f_list)
print('sort -', f_list.sort(reverse=True), f_list)
print('sort -', f_list.sort(key=len), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1]), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)
