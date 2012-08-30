sum = 0
for a in range(1, 1000):
  sum += a if (a % 3 == 0) or (a % 5 == 0) else 0

print sum
