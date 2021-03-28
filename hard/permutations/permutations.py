"""
You have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Obs.: You have to create your own algorithm. Although it's a good practice don't use ready-to-use python packages to solve this problem. 

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
"""

def permutations(string): 
    return set(''.join(i) for i in permute(string))


def permute(string):
    if len(string) in (0, 1):
        return [string]
    else:
        perm, lst = [], list(string)
        for i in range(len(lst)):
            first, others = lst[i], lst[:i] + lst[i+1:] 
            for p in permute(others):
                perm.append([first] + p)
        return perm
