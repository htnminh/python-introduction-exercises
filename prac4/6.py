import pickle
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
# YOUR CODE HERE
with open('lists.pkl', 'wb') as f:
    pickle.dump((a, b), f)

with open('lists.pkl', 'rb') as f:
    c, d = pickle.load(f)
    
f.close()
result = [i + j for i, j in zip(c, d)]
print(result)