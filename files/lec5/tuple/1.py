def sort_tuple(lst):
    rev_lst = [(float(v), v, k,) for (k, v) in lst]
    rev_lst.sort(reverse = True)
    return [(k, v) for (_, v, k) in rev_lst]

def main():
    tup = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
    print(sort_tuple(tup))
