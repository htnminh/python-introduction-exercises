def is_palindrome(s):
    s = s.replace(' ', '')
    # print(s)
    if s[0] != s[len(s) - 1]:
        return 'NO'
    if s == '' or len(s) == 1:
        return 'YES'
    return is_palindrome(s[1: len(s) - 1])