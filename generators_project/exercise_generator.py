def prime_generator(bound):
    n = 2
    while n < bound:
        prime = True
        for x in range(2, n):
            if n % x == 0:
                prime = False
        if prime:
            yield n
        n += 1


class PrimeGenerator:
    def __init__(self, stop):
        self.stop = stop
        self.number = 2

    def __next__(self):
        if self.number < self.stop:
            current = self.number
            prime = False
            while not prime:
                self.number += 1
                for x in range(2, self.number):
                    if self.number % x == 0:
                        break
                else:
                    prime = True
            return current
        else:
            raise StopIteration()


my_prime = PrimeGenerator(11)

print(next(my_prime))
print(next(my_prime))
print(next(my_prime))
print(next(my_prime))
print(next(my_prime))