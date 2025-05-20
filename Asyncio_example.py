import asyncio
import aiohttp
import requests
import time

# 9 тестових URL
urls = [
    "https://www.google.com",
    "https://reqrestestststststs/api/users?page=2",
    "https://www.bing.com",
    "https://www.wikipedia.org",
    "https://www.python.org",
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://api.github.com",
    "https://reqres.in/api/users?page=2"
]

# Функція, яка завантажує сторінку
async def fetch(session, url):
    try:
        async with session.get(url) as response:
            status = response.status
            content = await response.text()
            print(f"✅ {url} - статус {status}, довжина контенту: {len(content)}")
    except Exception as e:
        print(f"❌ Помилка при завантаженні {url}: {e}")

def sync_request_all():
    print(f"\n Синхронний запуск:")
    response = None
    start_time = time.perf_counter()
    for url in urls:
        try:
            response = requests.get(url)
            print(f"✅ {url} - статус {response.status_code}, довжина контенту: {len(response.content)}, Час запиту: {response.elapsed.total_seconds()} сек.")
        except requests.exceptions.RequestException as e:
            print(f"❌ Помилка при завантаженні {url}: {e}, Час запиту: {response.elapsed.total_seconds()} сек.")

    end_time = time.perf_counter()
    print(f"\n⏱️ Загальний час виконання: {end_time - start_time:.2f} секунд")

# Головна асинхронна функція
async def main():
    print(f"\n Асинхронний запуск:")
    start_time = time.perf_counter()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)

    end_time = time.perf_counter()
    print(f"\n⏱️ Загальний час виконання: {end_time - start_time:.2f} секунд")


if __name__ == "__main__":
    # Асинхронне виконання запитів
    asyncio.run(main())

    # Синхронне виконання запитів
    sync_request_all()