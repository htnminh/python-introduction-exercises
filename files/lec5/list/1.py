

a = [int(x) for x in input().split()]
exist = False

#if len(a) > 1:
for i in range(1, len(a)):
    if a[i - 1] < a[i]:
        print(str(a[i]) if exist == False else ' ' + str(a[i]), end = '')
        exist = True
        
if exist == False:
    print('NONE')