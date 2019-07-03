''''
Given a string and a non-negative int n, we'll say that the front of the string
is the first 3 chars, or whatever is there if the string is less than length 3.
 Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
'''

def front_times(str, n):
    size = len(str)
    if size == 0:
        return ''
    elif size <= 3:
        i = 0
        str1 = ''
        while i < n:
            str1 = str1 + str
            i = i + 1
        return str1
    else:
        str2 = ''
        str = str[:3]
        j = 0
        while j < n:
            str2 = str2 + str
            j = j + 1
        return str2

'''
Solution:

def front_times(str, n):
  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]

  result = ""
  for i in range(n):  #循环n次
    result = result + front
  return result
'''
