
def simple_gen(n):
    for i in range(n):
        yield i


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

def squares(n):
    for i in range(n):
        yield i * i


def reverse_string(s):
    for char in reversed(s):
        yield char


def countdown(n):
    while n > 0:
        yield n
        n -= 1


def primes(limit):
    for num in range(2, limit):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num


gen_expr = (x * 2 for x in range(5))


class MyIterator:
    def init(self, limit):
        self.limit = limit
        self.current = 0

    def iter(self):
        return self

    def next(self):
        if self.current < self.limit:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration


def yield_from_example(n):
    yield from range(n)