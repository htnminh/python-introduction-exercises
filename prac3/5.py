def remove_duplicates(lst):
    new_lst = list()
    
    first_check = True
    for ele in lst:
        if first_check:
            first_check = False
            prev = ele
            new_lst.append(ele)
        else:
            if prev != ele:
                new_lst.append(ele)
            prev = ele
    return new_lst

#print(remove_duplicates([1, 1, 1, 0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4, 5, 5]))
