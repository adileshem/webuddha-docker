import asyncio
import websockets

from webuddha import quotes

start_server = websockets.serve(quotes.generator, '127.0.0.1', 1337)

print('Webuddha is running on 127.0.0.1:1337')

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

