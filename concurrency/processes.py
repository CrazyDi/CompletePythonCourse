import time
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor


def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask_user, {time.time() - start}')


def complex_calculation():
    start = time.time()
    print('Started calculating...')
    [x**2 for x in range(20000000)]
    print(f'complex_calculation, {time.time() - start}')


if __name__ == "__main__":
    process1 = Process(target=complex_calculation)
    process2 = Process(target=complex_calculation)
    process1.start()
    process2.start()

    start = time.time()

    process1.join()
    process2.join()

    print(f'Two process total time: {time.time() - start}')

    start = time.time()

    with ProcessPoolExecutor(max_workers=2) as pool:
        pool.submit(complex_calculation)
        pool.submit(complex_calculation)

    print(f'Two process total time: {time.time() - start}')