# correct
# 0 1 ...
n = int(input()) # n>=0
if n==0:
    res = 0
elif n==1:
    res = 1
else:
    pre = 0
    next = 1
    for i in range(n-1):
        res = pre + next
        pre = next
        next = res
print (res)


