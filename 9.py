from itertools import product
from math import sqrt
from sets import *

squares = ImmutableSet(map(lambda x: x*x, range(1000)))

for (a, b) in product(range(500), repeat=2):
  c2 = a*a + b*b
  if c2 not in squares:
    continue
  c = int(sqrt(c2) + 0.0001)
  if a + b + c == 1000:
    print a*b*c
