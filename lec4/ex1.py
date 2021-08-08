def reverse_string(s):
    if len(s) == 1: return s
    return s[len(s) - 1] + reverse_string(s[0 : (len(s) - 1)])

def remove_even(s):
    res = ''
    for i in range(len(s)):
        res += '' if i%2 == 0 else s[i]
    return res

def transform_string(s):
    if len(s) % 4 == 0:
        return reverse_string(s)
    return remove_even(s)

#print(transform_string('12341515'))
#print(transform_string('asbvcddg2'))