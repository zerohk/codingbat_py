'''
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'

'''

'''
def not_string(str):
    if str[0,2] == 'not':   #元组切片用冒号，而且[0:2]表示不包含2
        return str
    else:
        return 'not ' + str
'''
#看了答案修正，但是还得判断一下str长度
def not_string(str):
  if str[0:3] == 'not':
    return str
  else:
    return 'not ' + str

'''
def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str
  # str[:3] goes from the start of the string up to but not
  # including index 3
'''
