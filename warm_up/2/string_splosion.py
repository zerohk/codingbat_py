'''
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''

def string_splosion(str):
  str1 = ''
  i = 0
  size = len(str)
  while i <= size:
    str1 = str1 + str[:i]
    i = i + 1
  return str1


'''
Solution:

def string_splosion(str):
  result = ""
  # On each iteration, add the substring of the chars 0..i
  for i in range(len(str)):
    result = result + str[:i+1]
  return result
'''
