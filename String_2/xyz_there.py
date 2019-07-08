'''
Return True if the given string contains an appearance of "xyz" where the xyz is
 not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
'''
def xyz_there(str):
    count = 0
    for i in range(len(str) - 1):
        if str[i:i+3] == 'xyz' and str[i - 1] != '.':
            return True
    return False
