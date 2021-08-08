n = int(input())

for i in range(n):
    print('_' * (n - i - 1) 
          + '/' 
          + ' ' * i * 2
          + '\\' 
          + '_' * (n - i - 1) )