import unittest
from lab7 import build, find_match

class TestSubstring(unittest.TestCase):
    def test_build_pi(self):
        pattern = "ababababba"
        pi = build(pattern)
        self.assertEqual(pi[0], 0)
        self.assertEqual(pi[2], 1)
        self.assertEqual(pi[3], 2)
        self.assertEqual(pi[8], 0)

    def test_find_match(self):
        text = "aabbaa"
        pattern = "baa"
        pi = build(pattern)
        pos = find_match(text, pattern, pi)
        self.assertEqual(pos, 3)


if __name__ == '__main__':
    unittest.main()