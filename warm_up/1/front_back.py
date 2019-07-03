'''
Given a string, return a new string where the first and last chars have been
exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
'''
#参考https://stackoverflow.com/questions/54578749/given-a-string-return-a-new-string-where-the-first-and-last-chars-have-been-exc
def front_back(str):
    size = len(str)
    if size == 1:
        return str
    elif size == 2:
        return str[1] + str[0]
    else:
        return str[size - 1] + str[1:size - 1] + str[0]


'''

Solution:

def front_back(str):
  if len(str) <= 1:
    return str

  mid = str[1:len(str)-1]  # can be written as str[1:-1]

  # last + mid + first
  return str[len(str)-1] + mid + str[0]
'''
