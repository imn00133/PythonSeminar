def closure_ex1():
    # Free variable
    # 클로저 영역
    series = []

    def averager(v):
        series.append(v)
        print(f'inner >> {series} / {len(series)}')
        return sum(series) / len(series)

    return averager


avg_closure1 = closure_ex1()
print(avg_closure1)

print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))

print()
print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))
print()
print(avg_closure1.__code__.co_freevars)
print()
print(dir(avg_closure1.__closure__))
print()
print(avg_closure1.__closure__[0].cell_contents)


def closure_ex2():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    return averager


avg_closuer2 = closure_ex2()
print(avg_closuer2(15))
print(avg_closuer2(35))
print(avg_closuer2(40))
