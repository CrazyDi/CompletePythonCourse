import time
import random

from threading import Thread


counter = 0


def increment_counter():
    global counter
    counter += 1
    print(f'New counter value: {counter}')
    print('---------')


if __name__ == "__main__":
    for x in range(10):
        t = Thread(target=increment_counter)
        time.sleep(random.random())
        t.start()
