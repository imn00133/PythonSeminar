import asyncio
import timeit
from urllib.request import urlopen
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import threading

start = timeit.default_timer()

urls = ['https://daum.net',
        'https://naver.com',
        'http://mlbpark.donga.com',
        'https://tistory.com',
        'https://front.wemakeprice.com'
        ]


async def fetch(url, executor):
    print('Thread Name: ', threading.current_thread().getName(), 'Start', url)
    response = await loop.run_in_executor(executor, urlopen, url)

    soup = BeautifulSoup(response.read(), 'html.parser')
    # print(soup.prettify())
    print('Thread Name: ', threading.current_thread().getName(), 'Done', url)
    result_data = soup.title
    return result_data


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
