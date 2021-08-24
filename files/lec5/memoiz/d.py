d = dict(zip('hust', [1, 5, 20, 3]))
print(d)
tmp = [(v, k) for k, v in d.items()]
print(tmp)
tmp.sort(reverse = True)
print(tmp)