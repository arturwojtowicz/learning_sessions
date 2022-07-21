
# async and await
print("----------- async and await -----------")
import asyncio
import time

def count_sleep():
    print("One")
    time.sleep(1)
    print("Two")

def main_sleep():
    for _ in range(3):
        count_sleep()

s = time.perf_counter()
main_sleep()
elapsed = time.perf_counter() - s
print(f"{__file__} executed in {elapsed:0.2f} seconds.")

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

s = time.perf_counter()
asyncio.run(main())
elapsed = time.perf_counter() - s
print(f"{__file__} executed in {elapsed:0.2f} seconds.")
