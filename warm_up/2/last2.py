'''
Given a string, return the count of the number of times that a substring length
2 appears in the string and also as the last 2 chars of the string, so "hixxxhi"
 yields 1 (we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
'''

def last2(str):
    #少了一个字符串长度小于等于2的判断
  count = 0
  stand = str[-2:]
  result = ''
  for i in range(len(str) - 2):
    result = str[i:i+2]
    if result == stand:
      count = count + 1
  return count


  '''
Solution:

def last2(str):
  # Screen out too-short string case.
  if len(str) < 2:
    return 0

  # last 2 chars, can be written as str[-2:]
  last2 = str[len(str)-2:]
  count = 0

  # Check each substring length 2 starting at i
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count
  '''
