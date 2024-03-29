def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1


class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self

"""
print(sum(FirstHundredGenerator()))

for i in FirstHundredGenerator():
    print(i)
"""

class AnotherIterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Focus']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]

"""
for car in AnotherIterable():
    print(car)
"""


def starts_with_r(friend):
    return friend.startwith('R')


friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
starts_with_r = filter(starts_with_r, friends)