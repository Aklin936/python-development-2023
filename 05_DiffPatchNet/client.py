import asyncio, sys

#define In, 0
#define Out, 1

async def main():
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 1337)

    server = asyncio.Queue()
    writer.write('hi'.encode())
    await writer.drain()
    send = asyncio.create_task(reader.readline())
    receive = asyncio.create_task(server.get())
    while not reader.at_eof():
        done, pending = await asyncio.wait([send, receive],
                                            return_when=asyncio.FIRST_COMPLETED)
        for q in done:
            if q is send:
                send = asyncio.create_task(reader.readline())
                print(q.result())
                await server.put(f" {q.result().decode().strip()}")
            elif q is receive:
                receive = asyncio.create_task(server.get())
                writer.write(f"{q.result()}\n".encode())
                await writer.drain()
    send.cancel()
    receive.cancel()
    writer.close()
    await writer.wait_closed()
asyncio.run(main())