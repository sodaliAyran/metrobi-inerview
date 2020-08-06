# TBH I'm not sure if this is true but here is my answer.

import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    l = ["a", "b", "c", "d"]
    delay = 1
    for item in l:
        print(f"started at {time.strftime('%X')}")
        await say_after(delay, item)
        print(f"finished at {time.strftime('%X')}\n")
        delay = delay * 2

asyncio.run(main())
