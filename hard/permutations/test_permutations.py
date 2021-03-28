import unittest
from permutations import permutations

class TestPermutations(unittest.TestCase):

    def test_simplest_input(self):
        self.assertEqual(sorted(permutations('a')), ['a'])
    
    def test_2_digits_imput(self):
        self.assertEqual(sorted(permutations('ab')), ['ab', 'ba']) 
        
    def test_4_digits_input(self):
        self.assertEqual(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'] )
        
    def test_5_digits_input(self):
        self.assertEqual(sorted(permutations('aaabb')), ['aaabb', 'aabab', 'aabba', 'abaab', 'ababa', 'abbaa', 'baaab', 'baaba', 'babaa', 'bbaaa'] )
