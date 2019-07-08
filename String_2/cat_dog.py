'''
Return True if the string "cat" and "dog" appear the same number of times in the
 given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
'''
def cat_dog(str):
  couc = 0
  coud = 0
  for s in range(len(str) - 1):
    if str[s:s+3] == 'cat':
      couc = couc + 1
  for s in range(len(str) - 1):
    if str[s:s+3] == 'dog':
      coud = coud + 1

  if couc == coud:
    return True
  return False
    
