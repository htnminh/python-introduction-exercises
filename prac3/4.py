valid_chars = {'b':'d',
               'd':'b',
               'i':'i',
               'o':'o',
               'p':'q',
               'q':'p',
               'v':'v',
               'w':'w',
               'x':'x'}

def valid(s):
    for character in s:
        if character not in valid_chars:
            return False
    return True
        
def mirror(s):
    if valid(s):
        return ''.join([valid_chars[c] for c in s[::-1]])
    return 'NOT POSSIBLE'
    
#print(mirror(input()))
