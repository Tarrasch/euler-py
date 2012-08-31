import fractions
import unittest

def lcm(a, b):
  return a*b/fractions.gcd(a, b)

class TestLcm(unittest.TestCase):

  def test_lcm(self):
    self.assertEqual(10, lcm(10, 5))
    self.assertEqual(40, lcm(10, 8))

# Uncomment to run tests
# if __name__ == '__main__':
#   unittest.main()

tot=1

print reduce(lcm, range(1,21))
