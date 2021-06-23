import asyncio
import random
import websockets

number = 1000

async def randommultiplier() -> str:
    return "the product of {0} and {1} - a random number = {2} " \
              .format( str(number), 
                       str(random.random()), 
                       str(number * random.random())
              )

async def sockethandlder(websocket, path):
    while True:
        await websocket.send(await randommultiplier())
        await asyncio.sleep(random.random() * 3)

try:
    start_server = websockets.serve(sockethandlder, "127.0.0.1", 5678)
    print('server is up and listening to port 5678!')
except:
    print('server did not start.')

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()