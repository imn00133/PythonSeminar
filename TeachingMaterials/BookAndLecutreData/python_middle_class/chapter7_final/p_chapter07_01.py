import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading

start = timeit.default_timer()

urls = ['https://daum.net',
        'https://naver.com',
        'http://mlbpark.donga.com',
        'https://tistory.com',
        'https://wemakeprice.com'
        ]


async def fetch(url, executor):
    print('Thread Name: ', threading.current_thread().getName(), 'Start', url)
    response = await loop.run_in_executor(executor, urlopen, url)
    print('Thread Name: ', threading.current_thread().getName(), 'Done', url)
    return response.read()[0:5]


async def main():
    executor = ThreadPoolExecutor(max_workers=10)

    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]

    result = await asyncio.gather(*futures)

    print()
    print('Result:', result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    duration = timeit.default_timer() - start
    print(f'Total Running Time:', duration)
