def lastchar_repeat(s):
    c = s[len(s) - 1]
    res = s.find(c) 
    return c if res != len(s) - 1 else None

def last_repeat(s):
    s = s.replace(' ', '')
    if s == '':
        return None
    if lastchar_repeat(s) == None:
        return last_repeat(s[0:len(s) - 1])
    return lastchar_repeat(s)