def coroutine1():
    print('>>> coroutine stated.')
    i = yield
    print('>> coroutine received : {}'.format(i))


# main routine
cr1 = coroutine1()
print(cr1, type(cr1))

next(cr1)
# next(cr1)
# cr1.send(100)

cr2 = coroutine1()
cr2.send(None)

print()


def coroutine2(x):
    print('>>> coroutine stated: {}'.format(x))
    y = yield x
    print('>>> coroutine received: {}'.format(y))
    z = yield x + y
    print('>>> coroutine received: {}'.format(z))


cr3 = coroutine2(10)

from inspect import getgeneratorstate

print(getgeneratorstate(cr3))

print(next(cr3))
print(getgeneratorstate(cr3))

print(cr3.send(100))
print(getgeneratorstate(cr3))

print()


def generator1():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y


t1 = generator1()

print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))

t2 = generator1()
print(list(t2))

print()


def generator2():
    yield from 'AB'
    yield from range(1, 4)


t3 = generator2()
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
