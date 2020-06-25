import os
import time
from concurrent import futures

WORK_LIST = [10 ** 5, 10 ** 6, 10 ** 7, 10 ** 8]


def sum_generator(n):
    return sum(n for n in range(n+1))


def main():
    worker = min(10, len(WORK_LIST))

    start_tm = time.time()

    with futures.ProcessPoolExecutor() as executor:
        result = executor.map(sum_generator, WORK_LIST)

    end_tm = time.time() - start_tm

    msg = '\n Result -> {} time: {:.2f}s'
    print(msg.format(list(result), end_tm))


if __name__ == '__main__':
    main()