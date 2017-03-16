import aiohttp
import asyncio
import async_timeout

import sys


async def fetch(session, url, counter):
    resp = ''
    for x in range(0, counter):
        async with session.get(url) as response:
            resp = await response.text()
    return resp

async def main(loop):

    counter = 1
    try:
        counter = int(sys.argv[1])
    except:
        pass

    async with aiohttp.ClientSession(loop=loop) as session:
        html = await fetch(session, 'https://webdevelop.pro/', counter)
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
