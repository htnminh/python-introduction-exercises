from list_utilities import *

lst = eval(input())
flated = flatten_nested_list(lst)
print(*flated)
print(max_num_in_list(flated))
