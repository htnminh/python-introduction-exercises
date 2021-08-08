d = dict()

def info(s):
    lst = s.split()
    #print(lst)
    #print({'sur': lst[-2], 'vote': int(lst[-1])})
    return {'sur': lst[-2], 'vote': int(lst[-1])}

s = input()
while True:
    if info(s)['sur'] not in d:
        d[info(s)['sur']] = info(s)['vote']
    else:
        d[info(s)['sur']] += info(s)['vote']
    
    try:
        s = input()
    except:
        break
        
lst = [(k, v) for (k, v) in d.items()]
lst.sort()
#print(lst)
for ele in lst:
    print(ele[0], ele[1])
