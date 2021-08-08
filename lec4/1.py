def check(s):
    count = 0
    for i in range(4):
        if s[i].isupper():
            count += 1
            # print(count)
            if count == 2:
                return True
    return False

def to_uppercase(s):
    return s.upper() if check(s) else s