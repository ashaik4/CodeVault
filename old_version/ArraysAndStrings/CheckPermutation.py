import unittest
"""
1.2 CTCI: Given two strings, write a method to decide if one is a permutation of other.
"""
def isPermutation(string1, string2):
    if len(string1) != len(string2):
        return False
    if sorted(list(string1)) == sorted(list(string2)):
        return True
    return False
print(isPermutation("ARSHAD", "DAHSRA"))

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(isPermutation("ARSHAD", "DAHSRA"), False)
        self.assertEqual(isPermutation(""))

if __name__ == '__main__':
    unittest.main()


