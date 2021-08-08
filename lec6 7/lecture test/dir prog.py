import mymodule
print(dir(mymodule), '\n')
myint = 5
print(dir(), '\n')
# When called without an argument, dir() lists all currently defined names

print(dir(myint), '\n')

print(myint.__round__)
print(type(myint.__round__))