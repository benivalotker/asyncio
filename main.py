import time
import asyncio

'''
steps:
    - create event loop to handle coroutine
    - create coroutine function (async)
    - create await to this coroutine for async progress 

NOTE: do not use any sunc function in coroutine (EX - time.sleep())
'''

def is_prime(x):
    return not any(x//i == x/i for i in range(x-1, 1, -1))


async def higest_prime_below(x):
    print("Higerst prime below {}".format(x))

    for y in range(x-1, 1, -1):
        if is_prime(y):
            print(" --> Higest prime below {} is {}".format(x, y))
            return y
        
        await asyncio.sleep(0.01) 
        # time.sleep(0.01)
    return None


async def main():
    await asyncio.wait([
        higest_prime_below(100000),
        higest_prime_below(10000),
        higest_prime_below(1000),
        higest_prime_below(100),
        higest_prime_below(100000),
    ])
    

# create event loop to run coroutine function
loop = asyncio.get_event_loop()
loop.run_until_complete(main())