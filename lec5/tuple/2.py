from functools import reduce

def sumoftup(tup):
    #return sum of all eles in tuple or return that value
    try:
        lst = list(tup)
        return reduce(lambda a, b: a + b, lst)
    except:
        return tup
    
def countoftup(tup):
    #return sum of all eles in tuple or return 1
    try:
        return len(tup)
    except:
        return 1
    
def sum_and_count(tt):
    
    for tup in tt:
        #print(tup)
        pass
    
    sum_list = [sumoftup(tup) for tup in tt]
    cnt_list = [countoftup(tup) for tup in tt]
    return sum_list, cnt_list
    

def main():
    inp = ((1,2,5), (3,7,5,10), (1))
    sum_list, cnt_list = sum_and_count(inp)
    print(*sum_list)
    print(*cnt_list)

#main()
