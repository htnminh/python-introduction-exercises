d = dict()

def process(s):
    words = s.split()
    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
        print(d[word] - 1, end = ' ')
    
    
s = input()
while True:
    process(s)
    
    try:
        s = input()
    except:
        break