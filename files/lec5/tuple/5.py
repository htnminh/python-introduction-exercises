lst1 = eval(input())
lst2 = eval(input())

cnt = 0
for tup in lst1:
    if tup in lst2 or (tup[1], tup[0]) in lst2:
        cnt += 1
print(cnt)