t ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(dir(t))

for c in t:
    print('>', c)

w = iter(t)

print(dir(w))

# print(next(w))

while True:
    try:
        print(next(w))
    except StopIteration:
        break

print()

print(hasattr(t, '__iter__'))

from collections import abc
print(isinstance(t, abc.Iterable))

print()


class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration')
        self._idx += 1
        return word

    def __repr__(self):
        return f'WordSplitter({self._text})'


wi = WordSplitter('Do today what you could do tomorrow')
print(wi)

print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))

print()


class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word
        # return 생략 가능
        return

    def __repr__(self):
        return f'WordSplitGenerator({self._text})'


wg = WordSplitGenerator('Do today what you could do tomorrow')
wt = iter(wg)

print(wt, wg)

print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))

