def remove_duplicates(a):
    count = list()
    distinct = list()
    for i in range(len(a)):
        value = a[i]
        if value != None:
            distinct.append(a[i])
            count.append(1)
            a[i] = None
        for j in range(i + 1, len(a)):
            if a[j] == value and value != None :
                count[len(count) - 1] += 1
                a[j] = None
    res = list()
    for i in range(len(distinct)):
        if count[i] == 1:
            res.append(distinct[i])
    return res