class string_utilities(object):
    def is_valid_parenthese(self, s):
        def is_pair(par_1, par_2):
            if (par_1 == '(' and par_2 == ')') or \
               (par_1 == '[' and par_2 == ']') or \
               (par_1 == '{' and par_2 == '}'):
                return True
            return False
        
        check_valid = ''

        if len(s) == 0:
            return True
        
        if len(s) % 2 == 1:
            return False

        for c in s:
            if check_valid == '':
                check_valid = check_valid + c
                #print('"%s"' % check_valid)
            elif is_pair(check_valid[-1], c):
                check_valid = check_valid[:-1]
                #print('"%s"' % check_valid)
            else:
                check_valid = check_valid + c
                
        return True if check_valid == '' else False
    
    def reverse_words(self, s):
        words = s.split()
        words.reverse()
        return ' '.join(words)

'''
print(string_utilities().is_valid_parenthese('{[(])]}'))
print(string_utilities().is_valid_parenthese('{[()(({}))]}'))
print(string_utilities().reverse_words('Bach khoa Ha Noi'))
'''