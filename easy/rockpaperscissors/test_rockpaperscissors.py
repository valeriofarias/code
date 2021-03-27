import unittest
from rockpaperscissors import play

class TestRPS(unittest.TestCase):
    def test_input_when_not_rock_paper_scissors(self):
        self.assertEqual(play('computer','paper'),'The options are rock, paper or scissors. Pick one of them and try again!')
        
    def test_input_should_not_be_empty(self):
        self.assertEqual(play('paper',''),'The options are rock, paper or scissors. Pick one of them and try again!')
        
    def test_if_draw_when_a_equals_to_b(self):
        self.assertEqual(play('paper','paper'), 'It ended in a draw! Try again.')
    
    
    def test_input_when_only_rock_paper_scissors(self): 
        self.assertNotEqual(play('paper','scissors'), 'The options are rock, paper or scissors. Pick one of them and try again!')
        
    def test_if_paper_vs_rock_paper_wins(self):
        self.assertEqual(play('paper', 'rock'), 'Player 01 won! - paper x rock => paper')

    def test_if_rock_vs_paper_paper_wins(self):
        self.assertEqual(play('rock', 'paper'), 'Player 02 won! - rock x paper => paper')
        
    def test_if_paper_vs_scissors_scissors_wins(self):
        self.assertEqual(play('paper', 'scissors'), 'Player 02 won! - paper x scissors => scissors')

    def test_if_scissors_vs_paper_scissors_wins(self):
        self.assertEqual(play('scissors', 'paper'), 'Player 01 won! - scissors x paper => scissors')
        
    def test_if_rock_vs_scissors_rock_wins(self):
        self.assertEqual(play('rock', 'scissors'), 'Player 01 won! - rock x scissors => rock')

    def test_if_scissors_vs_rock_rock_wins(self):
        self.assertEqual(play('scissors', 'rock'), 'Player 02 won! - scissors x rock => rock') 
    

        
        
