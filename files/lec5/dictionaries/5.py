
n = int(input())
a = [int(x) for x in input().split()]
d = dict()
'''
n = 16
s = '17 -20 -21 11 39 23 -24 5 3 -32 38 22 -14 -40 9 32'
a = [int(x) for x in s.split()]
print(a)
'''
# subseq = considering subsequence

def successive(a, b): # check if a and b are 2 successive elements of a subseq
    if abs(a) < abs(b) and a * b < 0:
        return True
    return False

def longest_include(i): # find the length of the longest subseq that include i-th element
    
    if i in d:
        return d[i]
    
    res = 1
    for j in range(i): # run j from 0 to i - 1 to find
        if successive(a[j], a[i]): # if a j-th element (which is successive to i-th) is found,
            res = max(res, 1 + longest_include(j))
                  # if j-th is not in the final subseq, the result will be the same
                  # else the result will be increased by 1
    # if there is no j-th is found, the result is 1
    d[i] = res
    return res

def longest_all():
    arr = [longest_include(i) for i in range(n)]
    #print(arr)
    return max(arr)
    
print(longest_all())