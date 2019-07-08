'''
When squirrels get together for a party, they like to have cigars.
A squirrel party is successful when the number of cigars is between 40 and 60,
inclusive. Unless it is the weekend, in which case there is no upper bound on
the number of cigars. Return True if the party with the given values is
successful, or False otherwise.

cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True
'''
def cigar_party(cigars, is_weekend):
  return is_weekend and cigars >= 40 or (is_weekend == False and cigars >= 40 and cigars <= 60)

'''
def cigar_party(cigars, is_weekend):
  if is_weekend:
    return cigars >= 40
  else:
    return cigars >= 40 and cigars <= 60
'''

'''
Hint:
One approach begins with

if is_weekend:
  ...
else:
  ...

In each section, check cigars with >=, <= etc. to return True if cigars is in
range or else return False. Extra trick: for shorter code, note that "return
(x >= 50)" automatically returns True if x >= 50 and False if x < 50.
This works because the expression "(x >= 50)" evaluates to the value True or
False, and then that value is returned.
'''
