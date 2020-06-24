def generator_ex1():
    print('start')
    yield 'A Point'
    print('Continue')
    yield 'B Point'
    print('End')


temp = iter(generator_ex1())

print(temp)
print(next(temp))
print(next(temp))
# print(next(temp))

print()

for v in generator_ex1():
    print(v)


temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())

print(temp2)
print(temp3)

for i in temp2:
    print(i)

for i in temp3:
    print(i)

print()

import itertools

gen1 = itertools.count(1, 2.5)
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))

gen2 = itertools.takewhile(lambda n: n < 1000, itertools.count(1, 2.5))
for v in gen2:
    pass
    # print(v)
print()

gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])
for v in gen3:
    print(v)

gen4 = itertools.accumulate([x for x in range(101)])
for v in gen4:
    print(v)

gen5 = itertools.chain('ABCDE', range(1, 11, 2))
print(list(gen5))

gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6))

gen7 = itertools.product('ABCDE')
print(list(gen7))

gen8 = itertools.product('ABCDE', repeat=2)
print(list(gen8))

gen9 = itertools.groupby('AAABBCCCCDDEEE')
# print(list(gen9))
for chr, group in gen9:
    print(chr, ':', list(group))