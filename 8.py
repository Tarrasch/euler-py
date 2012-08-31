import operator

matrix = open('8.data', 'r').read().split('\n')
matrix = filter(None, matrix) # remove empty list
matrix = map(lambda row: map(lambda elem: int(elem), row), matrix)

def prod(xs):
  return reduce(operator.mul, xs)

def transpose(xss):
  return zip(*xss)

def check_matrix(matrix):
  return max(map(check_row, matrix))

def check_row(row):
  return max(map(lambda i: prod(row[i:i+5]), range(len(row)-4)))

print max(map(check_matrix, [matrix, transpose(matrix)]))

