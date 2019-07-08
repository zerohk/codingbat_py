'''
Return the number of times that the string "hi" appears anywhere in the given string.

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
'''
def count_hi(str):
  count = 0
  if len(str) < 2:
    return count
  for i in range(len(str) -2):
    if str[i:i+2] == 'hi':
      count = count + 1
  if str[-2:] == 'hi':
    count = count + 1
  return count