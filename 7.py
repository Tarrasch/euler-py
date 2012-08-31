import itertools
import sys

sys.setrecursionlimit(200000)

def irange(a, b):
  for x in xrange(a, b):
    yield x


def filter_divisibilty(xs, n):
  for x in xs:
    if x%n != 0: yield x

def primes():
  return sieve(itertools.count(2))

def sieve(xs):
  head = next(xs)
  yield head
  for x in sieve(filter_divisibilty(xs, head)):
    yield x

for x in itertools.islice(primes(), 10000, 10001):
  print x
