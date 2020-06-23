from types import MappingProxyType

d = {'key1': 'value1'}

d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d))

# d_frozen['key2'] = 'value2'

d['key2'] = 'value2'
print(d, id(d))

s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
# s4 = {}
s4 = set()
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

s1.add('Melon')
print(s1)

# s5.add('Melon')

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

from dis import dis

print('-----')
dis('{10}')
dis('set([10])')

print('-----')

from unicodedata import name

print({name(chr(i), '') for i in range(0, 256)})
