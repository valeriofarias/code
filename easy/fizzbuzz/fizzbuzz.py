"""
FizzBuzz rules

1. If position is multiple of 3 say fizz
2. If position is multiple of 5 say buzz
3. If position is multiple of 3 and 5 say fizzbuzz
4. For any other position say the number
"""

def robot(pos):
    
    say = str(pos)
    
    if pos % 3 == 0:
        say = 'fizz'
    if pos % 5 == 0:
        say = 'buzz'
    if pos % 5 == 0 and pos % 3 == 0:
        say = 'fizzbuzz'

    return say
