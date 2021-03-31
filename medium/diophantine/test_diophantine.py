import unittest
from diophantine import detect_solution, solution, all_solutions, howmuch, howmuch_optimized

class TestDiophantineEquation(unittest.TestCase):
    def test_when_has_solution(self):
        self.assertEqual(detect_solution(3,6,9), 'solution exist')
        
    def test_solution_369(self):
        self.assertEqual(solution(3,6,9), 'x = 1, y = 1')
        
    def test_John_purchasing_solution(self):
        self.assertEqual(solution(12,8,68), 'x = 1, y = 7')
        
    def test_all_solutions_for_john(self):
        self.assertEqual(all_solutions(12,8,68), '(x = 1, y = 7), (x = 3, y = 4), (x = 5, y = 1), ')
        
    
    
    def test_how_much_1_to_38(self):    
        self.assertEqual(howmuch(1, 38), [["M: 37", "B: 5", "C: 4"]])
    
    def test_how_much_1_to_100(self):    
        self.assertEqual(howmuch(1, 100), [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"]])
        
    def test_how_much_1_to_200(self):
        self.assertEqual(howmuch(1, 200), [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"], ["M: 163", "B: 23", "C: 18"]])
        
    def test_how_much_1000_to_1100(self):
        self.assertEqual(howmuch(1000, 1100), [["M: 1045", "B: 149", "C: 116"]])
        
    def test_how_much_10_000_to_9950(self):    
        self.assertEqual(howmuch(10000, 9950), [["M: 9991", "B: 1427", "C: 1110"]])

        
    
    def test_how_much_optimized_1_to_38(self):    
        self.assertEqual(howmuch_optimized(1, 38), [["M: 37", "B: 5", "C: 4"]])
    
    def test_how_much_optimized_1_to_100(self):    
        self.assertEqual(howmuch_optimized(1, 100), [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"]])
        
    def test_how_much_optimized_1_to_200(self):
        self.assertEqual(howmuch_optimized(1, 200), [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"], ["M: 163", "B: 23", "C: 18"]])
        
    def test_how_much_optimized_1000_to_1100(self):
        self.assertEqual(howmuch_optimized(1000, 1100), [["M: 1045", "B: 149", "C: 116"]])
        
    def test_how_much_optimized_10_000_to_9950(self):    
        self.assertEqual(howmuch_optimized(10000, 9950), [["M: 9991", "B: 1427", "C: 1110"]])    
        
