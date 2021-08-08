def list_replacement(lst, k, new_list):
    res = list()
    for ele in lst:
        #res.append((e for e in new_list) if ele > k else ele)
        if ele <= k:
            res.append(ele)
        else:
            for e in new_list:
                res.append(e)
    return res