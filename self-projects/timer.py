import asyncio

minutes = int(input('How much your timer you want to be?'))
async def timer():
    for i in range(minutes-1,-1,-1):
        for j in range(59,0,-1):
            if j<10:
                print(f'{i}:0{j}')
            else:
                print(f'{i}:{j}')
            await asyncio.sleep(1)

asyncio.run(timer())

