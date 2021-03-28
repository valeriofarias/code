"""
A happy number is a number defined by the following process: starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.

Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are sad numbers.

Write a function that takes n as parameter and return 'happy' if and only if n is an happy number, 'sad' otherwise.

Examples:

Is 7 happy?
square(7) = 49
square(4) + square(9) = 16 + 81 = 97
square(9) + square(7) = 81 + 49 = 130
square(1) + square(3) + square(0) = 1 + 9 + 0 = 10
square(1) + square(0) = 1 
Yeas, 7 is happy. 

Is 4 happy?
square(4) = 16
square(1) + square(6) = 1 + 36 = 37
square(3) + square(7) = 9 + 49 = 58
square(5) + square(8) = 25 + 64 = 89
square(8) + square(9) = 64 + 81 = 145
square(1) + square(4) + square(5) = 1 + 16 + 25 = 42
square(4) + square(2) = 16 + 4 = 20
square(2) + square(0) = 4 + 0 = 4
4 is sad.
"""

def happy(number):
    num, sum_ = str(number), 0
    for c in num:
        sum_ += int(c)**2    
    
    if sum_ in (1,7):
        return 'happy'
    elif sum_ in (2,3,4,5,8,9):
        return 'sad'
    else:
        return happy(sum_)
        
        
        
        
        
        
        
        
        
        
        
        
        
