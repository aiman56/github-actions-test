import unittest

# Example function to test
def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # 
        self.assertEqual(add(-1, 1), 2)  # 

if __name__ == "__main__":
    unittest.main()
