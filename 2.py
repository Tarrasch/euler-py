def fibs():
  a = 1
  b = 1
  while True:
    yield b
    b, a = b + a, b

def even(seq):
  for x in seq:
    if x % 2 == 0:
      yield x

acc = 0
for x in even(fibs()):
  if x > 4000000: break
  acc += x

print acc


import itertools

print sum(x for x in itertools.takewhile(lambda x: x <= 4000000, fibs()) if x % 2 == 0)
