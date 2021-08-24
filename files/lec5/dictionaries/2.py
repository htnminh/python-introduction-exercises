d = dict()

def process(s):
    words = s.split()
    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    
    
s = input()
while True:
    process(s)
    
    try:
        s = input()
    except:
        break

wordlist = [(word, d[word]) for word in d]
wordlist.sort()
wordlist.sort(reverse = True, key = lambda wordtup: wordtup[1])
for ele in wordlist:
    print(ele[0])