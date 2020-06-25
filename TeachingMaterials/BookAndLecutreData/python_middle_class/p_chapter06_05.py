import os
import time
from concurrent import futures

WORK_LIST = [10 ** 6, 10 ** 5, 10 ** 7, 10 ** 8]


def sum_generator(n):
    return sum(n for n in range(n+1))


def main():
    worker = min(10, len(WORK_LIST))

    start_tm = time.time()
    futures_list = []

    with futures.ProcessPoolExecutor() as executor:
        for work in WORK_LIST:
            future = executor.submit(sum_generator, work)
            futures_list.append(future)
            print(f'Scheduled for {work}: {future}')

        result = futures.wait(futures_list, timeout=6)
        print('Completed Task:', str(result.done))
        print('Pending ones after waiting for 6 second: ', str(result.not_done))
        print([future.result() for future in result.done])

    end_tm = time.time() - start_tm
    msg = '\ntime: {:.2f}s'
    print(msg.format(end_tm))


def main2():
    worker = min(10, len(WORK_LIST))

    start_tm = time.time()
    futures_list = []

    with futures.ProcessPoolExecutor() as executor:
        for work in WORK_LIST:
            future = executor.submit(sum_generator, work)
            futures_list.append(future)
            print(f'Scheduled for {work}: {future}')

        for future in futures.as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled()

            print(f'Future Result: {result}, Done: {done}')
            print(f'Future Cancelled: {cancelled}')

    end_tm = time.time() - start_tm
    msg = '\ntime: {:.2f}s'
    print(msg.format(end_tm))


if __name__ == '__main__':
    main2()