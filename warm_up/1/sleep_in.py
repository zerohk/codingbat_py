'''
The parameter weekday is True if it is a weekday, and the parameter vacation is
True if we are on vacation. We sleep in if it is not a weekday or we're on vacation.
Return True if we sleep in.

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
'''
#我的解法
def sleep_in(weekday, vacation):
  if weekday == False or vacation == True:
    return True
  else:
    return False

#Solution:
'''
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
  # This can be shortened to: return(not weekday or vacation)
'''
