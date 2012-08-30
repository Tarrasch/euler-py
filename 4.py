import unittest

def is_palindrome(x):
  s = str(x)
  for i in range(len(s)):
    if s[i] != s[len(s)-i-1]: return False
  return True

class TestPal(unittest.TestCase):

  def test_trues(self):
    self.assertTrue(is_palindrome(1))
    self.assertTrue(is_palindrome(111))
    self.assertTrue(is_palindrome(1111))
    self.assertTrue(is_palindrome(165561))
    self.assertTrue(is_palindrome(124421))

  def test_falses(self):
    self.assertFalse(is_palindrome(13))
    self.assertFalse(is_palindrome(1211))
    self.assertFalse(is_palindrome(991999))
    self.assertFalse(is_palindrome(12323))

# Uncomment to run tests
# if __name__ == '__main__':
#   unittest.main()

def pals():
  for x in range(1000):
    for y in range(1000):
      p = x*y
      if is_palindrome(p): yield p

print max(pals())
