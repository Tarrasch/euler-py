c = 600851475143

i = 2
while i < c:
  if c % i == 0:
    print i
    c /= i
  else:
    i+= 1

print c
