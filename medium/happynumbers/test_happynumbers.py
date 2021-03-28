import unittest
from happynumbers import happy

class TestHappyNumbers(unittest.TestCase):
    
    def test_is_7_happy(self):
        self.assertEqual(happy(7), 'happy')
    
    def test_is_1_happy(self):
        self.assertEqual(happy(1), 'happy')
        
    def test_is_10_happy(self):
        self.assertEqual(happy(10), 'happy')
        
        
    def test_is_4_happy(self):
        self.assertEqual(happy(4), 'sad')
        
    def test_is_20_happy(self):
        self.assertEqual(happy(20), 'sad')
        
    def test_is_42_happy(self):
        self.assertEqual(happy(42), 'sad')
        
        
        
