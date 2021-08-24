with open('test.inp') as f:
    d = dict()
    for line in f:
        for word in line.split(' '):
            d[word] = d.get(word, 0) + 1
    
    with open('test.out', 'w') as f:
        f.write(str(d))

with open('test.out', 'r') as f:
    all = f.read()
    print(all)
    
f.close()