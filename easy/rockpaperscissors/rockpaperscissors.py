"""
Rock paper scissor is a Japanese game, where two players choose one of three possible items: Stone, Paper or Scissors.

The goal is to make a judge who, given the two players' move, informs the result of the match.

Winning Rules as follows:

Rock vs Paper: paper wins because paper covers rock.
Rock vs Scissors: rock wins because rock crushes scissors.
Paper vs Scissors: scissors wins because scissors cuts paper.
"""

def play(one, two):
    OPTIONS = ('rock', 'paper', 'scissors')
    if one not in OPTIONS or two not in OPTIONS: 
        return 'The options are rock, paper or scissors. Pick one of them and try again!'
    
    winner = ''
    if one == 'paper' and two == 'rock':
        winner = 'Player 01 won! - paper x rock => paper'
    if one == 'rock' and two == 'paper':
        winner = 'Player 02 won! - rock x paper => paper'
    if one == 'paper' and two == 'scissors':
        winner = 'Player 02 won! - paper x scissors => scissors'
    if one == 'scissors' and two == 'paper':
        winner = 'Player 01 won! - scissors x paper => scissors'
    if one == 'rock' and two == 'scissors':
        winner = 'Player 01 won! - rock x scissors => rock'
    if one == 'scissors' and two == 'rock':
        winner = 'Player 02 won! - scissors x rock => rock'
    
    
    if one == two:
        winner = 'It ended in a draw! Try again.'    

    return winner
