'''
Given a string, return a string where for every char in the original, there are
two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
'''
def double_char(str):
  result = ''
  for s in str:
    result = result + s + s
  return result



  '''
In Python, the loop "for i in range(len(str)):"
loops i through each index in the string, 0, 1, 2, .. len-1.
  '''


  '''
def double_char(str):
  result = ''
  for i in range(len(str)):
    result = result + str[i] + str[i]
  return result
  '''
