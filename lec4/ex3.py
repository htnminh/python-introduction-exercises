def second_largest(lst):
    lst.sort(reverse = True)
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]:
            return lst[i]
    return lst[0]