'''
Given two strings, return True if either of the strings appears at the very end
 of the other string, ignoring upper/lower case differences (in other words, the
 computation should not be "case sensitive"). Note: s.lower() returns the
 lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
'''
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    sa = len(a)
    sb = len(b)
    if sa >= sb:
        if a[-sb:] == b:
            return True
    if sa < sb:
        if b[-sa:] == a:
            return True
    return False

    '''

Hint:
In Python s1.endswith(s2) tests if string s1 ends with string s2 -- makes
this much easier!
    '''


    '''
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    sa = len(a)
    sb = len(b)
    if sa >= sb:
        return a.endswith(b)
    if sa < sb:
        return b.endswith(a)
    '''
