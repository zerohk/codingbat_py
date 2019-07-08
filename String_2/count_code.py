'''
Return the number of times that the string "code" appears anywhere in the given
string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
'''
def count_code(str):
    count = 0
    for s in range(len(str) - 3):
        if str[s:s+2] == 'co' and str[s+3] == 'e':
            count = count + 1
    return count
