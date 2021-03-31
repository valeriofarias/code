"""
Practical problem 01: John and the most possible packs of cans

John is purchasing cold drinks for the upcoming party. He has 68 to spend. He can purchase bigger packs of can of 12 or smaller packs of can of 8. Find how many cans of each kind he can purchase and in how many ways if he spends all of his money.
12x + 8y = 68

Inspired on
https://www.youtube.com/watch?v=lDvPfC2lkT0 from Python tutorials


--------------------------------------------------------------------
Practical problem 02 from codewars: How much? (created by the user g964).

I always thought that my old friend John was rather richer than he looked, but I never knew exactly how much money he actually had. One day (as I was plying him with questions) he said:

    "Imagine I have between m and n Zloty..." (or did he say Quetzal? I can't remember!)
    "If I were to buy 9 cars costing c each, I'd only have 1 Zloty (or was it Meticals?) left."
    "And if I were to buy 7 boats at b each, I'd only have 2 Ringglets (or was it Zloty?) left."

Could you tell me in each possible case:

    how much money f he could possibly have ?
    the cost c of a car?
    the cost b of a boat?

So, I will have a better idea about his fortune. Note that if m-n is big enough, you might have a lot of possible answers.

Each answer should be given as ["M: f", "B: b", "C: c"] and all the answers as [ ["M: f", "B: b", "C: c"], ... ]. "M" stands for money, "B" for boats, "C" for cars.

Note: m, n, f, b, c are positive integers, where 0 <= m <= n or m >= n >= 0. m and n are inclusive.
Examples:

howmuch(1, 100)      => [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"]]
howmuch(1000, 1100)  => [["M: 1045", "B: 149", "C: 116"]]
howmuch(10000, 9950) => [["M: 9991", "B: 1427", "C: 1110"]]
howmuch(0, 200)      => [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"], ["M: 163", "B: 23", "C: 18"]]

Explanation of the results for howmuch(1, 100):

    In the first answer his possible fortune is 37:
    so he can buy 7 boats each worth 5: 37 - 7 * 5 = 2
    or he can buy 9 cars worth 4 each: 37 - 9 * 4 = 1
    The second possible answer is 100:
    he can buy 7 boats each worth 14: 100 - 7 * 14 = 2
    or he can buy 9 cars worth 11: 100 - 9 * 11 = 1

--------------------------------------------------------------------
In order to solve these problems let's underestand how to solve Linear Diophantine Equation.

Linear Diophantine Equation

A diophantine equation is a polynomial equaltion whose solutions are restricted to integers. A linear diophantine equation is one of the first degree equation. In linear diophantine equations only integral solutions are required. An integral solutions is a solutions such that all unkonw variables take only integer values. 

General form : ax + by = c
Example: 3x + 6y = 9
One integral solution, x = 1, y = 1


Condition for solution
Integral solutions of the linear diophantine equations exists if and only if, the GCD of the coefficients of the two variables divides the constant term perfectly.In other terms the integral solutions exist if, GCD(a,b) divides c.

Algorithm
Find GCD(a,b)
Check if c % GCD(a,b) == 0
If yes, them print possible
Else print not possible

Finding solutions of the linear Diophantine equations

form ax + by = c
problem: 3x + 6y = 9

Doing it mathematically:
Solving these equations on pen and paper gives
y = (c - ax)/ b
x = (c - by)/ a

Implementing in python
We will simply iterate through all possible values from 0 to c
as it cannot exceed c for the solution.

Problem O1: John's purchasing
"""
from math import gcd

def is_possible(a,b,c):
    """Detect if the diophantine equation has solution"""
    return (c % gcd(a,b) == 0)


def detect_solution(a,b,c):
    if is_possible(3,6,9):
        return 'solution exist'
    else:
        return 'No solution exist'


def solution(a,b,c):
    i = 0
    while i * a <= c:
        if(c - (a * i )) % b == 0:
            return f'x = {i}, y = {int((c - (a * i))/b)}'
        i += 1


def all_solutions(a,b,c):
    i, solution = 0, ''
    while i * a <= c:
        if(c - (a * i)) % b == 0:
            solution += f'(x = {i}, y = {int((c - (a * i))/b)}), '
        i += 1
    
    return solution
    
   
# Problem 02: How much?
def howmuch(begin, end):
    solutions = []
    iter_ = range(begin, end+1) if begin <= end else range(end, begin+1)

    for m in iter_:
        car  =  (m - 1)/9
        boat = (m - 2)/7
        if car.is_integer() and boat.is_integer():
                solutions.append([f'M: {m}' , f'B: {int(boat)}', f'C: {int(car)}'])
    return solutions

    
"""
Optimized solution done by Mercy Madmask from codewars
All the solutions I saw were so slow, iterating the whole m -> n
For M, the solutions are the 37 + 63k in [m, n]
You can find that with chinese remainder theorem, or just by looking at the examples Then just calculate B and C for each.
No need to waste time doing useless loops
"""
from math import ceil

def howmuch_optimized(m, n):
    m, n = min(m, n), max(m, n)
    x = max(0, ceil((m-37)/63))
    return [[f"M: {y}", f"B: {(y-2)//7}", f"C: {(y-1)//9}"] for y in range(37 + 63*x, n+1, 63)]
    
    

