def func_v1(a):
    print(a)
    print(b)


# func_v1(10)

b = 20


def func_v2(a):
    print(a)
    print(b)


func_v2(10)


c = 30


def func_v3(a):
    global c
    print(a)
    print(c)
    c = 40


print('>>', c)
func_v3(10)
print('>>>', c)

a = 100

print(a + 100)
print(a + 1000)

print(sum(range(1, 51)))
print(sum(range(51, 101)))


class Averager:
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print(f'inner >> {self._series} / {len(self._series)}')
        return sum(self._series) / len(self._series)


averager_cls = Averager()

print(dir(averager_cls))

print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(50))
print(averager_cls(70))
print(averager_cls(193))