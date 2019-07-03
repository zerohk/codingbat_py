'''
Given a string and a non-negative int n, return a larger string that is n copies
of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
'''

def string_times(str, n):
    i = 0
    str1 = ''
    while i < n :
        str1 = str1 + str
        i = i + 1 #Python不能用i++形式
    return str
