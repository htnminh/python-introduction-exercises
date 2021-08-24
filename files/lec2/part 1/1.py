#correct

a = int(input())
b = int(input())
if a%2==1: a += 1
if b%2==1: b -= 1
print((b-a)//2+1)