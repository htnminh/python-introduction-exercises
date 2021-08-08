def dictionary_convert(s):
    # YOUR CODE HERE
    d = dict()
    for char in s:
        d[char] = d.get(char, 0) + 1 
    return d
#print(dictionary_convert('edcbaabcd'))
