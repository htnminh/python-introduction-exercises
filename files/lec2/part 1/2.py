#correct

a = int(input())
b = int(input())
c = int(input())
for num in [b,c]:
    if num > a: a = num
print(a)