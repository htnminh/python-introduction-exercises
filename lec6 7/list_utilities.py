def max_num_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max
def flatten_nested_list(nested_lst):
    return [item for sublist in nested_lst for item in sublist]